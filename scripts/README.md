# SOC Analyst Scripts

Python tools for SOC analyst tasks. PowerShell versions are planned.

## ip-enricher.py

Checks an IP address against VirusTotal and AbuseIPDB, optionally adds Shodan data, gives a triage verdict, and writes an HTML report.

### Setup

```bash
pip install -r requirements.txt
export VT_KEY="your_virustotal_api_key"
export ABUSE_KEY="your_abuseipdb_api_key"
export SHODAN_KEY="your_shodan_api_key"   # optional
```

Free keys: virustotal.com · abuseipdb.com · account.shodan.io

### Usage

```bash
python3 ip-enricher.py 1.2.3.4
```

This prints the verdict and saves `1-2-3-4-triage.html` in the current folder.

### Verdict thresholds

| Verdict | Condition |
|---------|-----------|
| MALICIOUS | VirusTotal malicious count above 3, or AbuseIPDB score above 50 |
| SUSPICIOUS | VirusTotal malicious count above 0, or AbuseIPDB score above 10 |
| CLEAN | Neither condition met |

These thresholds are my starting values. They have not yet been tested against labelled data.

## Planned

- hash-lookup.py (file hash lookup)
- email-header-parser.py (origin IP from email headers)
- PowerShell versions of the scripts
