# Sigma Rules

Vendor-agnostic detection rules in YAML (Sigma format).

## Rules in this folder

| File | Technique | ATT&CK | Status |
|------|-----------|--------|--------|
| kerberoasting.yml | RC4-encrypted Kerberos ticket request | T1558.003 | In repo (experimental) |
| brute-force.yml | Failed logon threshold | T1110 | Planned |
| new-service.yml | New Windows service installed | T1543.003 | Planned |
| powershell-bypass.yml | PowerShell execution policy bypass | T1059.001 | Planned |
| lsass-access.yml | LSASS memory access | T1003.001 | Planned |

## CI/CD pipeline

On a push that changes a file in this folder, GitHub Actions:

1. Installs sigma-cli with the Splunk and Microsoft 365 Defender backends.
2. Converts the rules to Splunk SPL and to Microsoft 365 Defender (Advanced Hunting) queries.
3. Writes the output to `detection-rules/auto-converted/` and commits it.

The workflow produces Defender Advanced Hunting queries, not Sentinel analytics rules. Sentinel rules are written by hand in `detection-rules/`.
