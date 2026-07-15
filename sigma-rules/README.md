# Sigma Rules

Vendor-agnostic detection rules in YAML format.
GitHub Actions CI/CD pipeline automatically converts each rule to Splunk SPL and Microsoft Sentinel KQL on every push.

## CI/CD Pipeline

Push a new .yml file to this folder → GitHub Actions runs sigma-cli → converted rules appear in `detection-rules/auto-converted/`

## Rules

| File | Technique | ATT&CK |
|------|-----------|--------|
| brute-force.yml | Failed logon threshold | T1110 |
| new-service.yml | New Windows service installed | T1543.003 |
| powershell-bypass.yml | PowerShell execution policy bypass | T1059.001 |
| kerberoasting.yml | RC4-encrypted Kerberos ticket request | T1558.003 |
| lsass-access.yml | LSASS memory access | T1003.001 |
