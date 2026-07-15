# SOC Analyst Scripts

Python and PowerShell automation tools for SOC analyst tasks.
Every script has a Python (.py) and PowerShell (.ps1) version.

## Usage

```bash
# IP triage — enriches an IP with VirusTotal, AbuseIPDB, and Shodan
python3 soc-toolkit.py ip-triage 1.2.3.4

# Hash lookup — checks a file hash on VirusTotal
python3 soc-toolkit.py hash-lookup d41d8cd98f00b204e9800998ecf8427e

# Email header parser — extracts origin IP from email headers
python3 soc-toolkit.py email-parse suspicious-email.eml
```

## API Keys Required

Set these as environment variables before running:

```bash
export VT_KEY="your_virustotal_api_key"
export ABUSE_KEY="your_abuseipdb_api_key"
export SHODAN_KEY="your_shodan_api_key"
```

Get free keys at: virustotal.com · abuseipdb.com · account.shodan.io

## Scripts

| File | Language | Purpose |
|------|----------|---------|
| soc-toolkit.py | Python | Main CLI toolkit |
| ip-enricher.py | Python | IP reputation (VT + AbuseIPDB + Shodan) |
| hash-lookup.py | Python | File hash lookup via VirusTotal |
| email-header-parser.py | Python | Extract origin IP from email headers |
| incident-report-gen.py | Python | Generate HTML report from Splunk results |
| powershell-full-triage.ps1 | PowerShell | Full Windows triage — all 8 Event IDs |
| powershell-ip-enricher.ps1 | PowerShell | IP reputation via AbuseIPDB |
| powershell-vol-runner.ps1 | PowerShell | Auto-run all Volatility3 plugins |
