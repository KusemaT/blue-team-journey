# Detection Rules

Each rule includes its ATT&CK technique, a Splunk SPL query and a Microsoft Sentinel KQL query (where written), false positive notes, and response actions.

## Rules Library

| # | Rule Name | EventID | ATT&CK | Severity | Status |
|---|-----------|---------|--------|----------|--------|
| 01 | Brute Force — Failed Logon Threshold | 4625 | T1110 | Medium | In repo |
| 02 | New User Account Created | 4720 | T1136.001 | High | Planned |
| 03 | User Added to Privileged Group | 4732 | T1078.002 | High | Planned |
| 04 | New Service Installed | 7045 | T1543.003 | High | Planned |
| 05 | Kerberoasting — RC4 Ticket Request | 4769 | T1558.003 | High | In repo as Sigma (`/sigma-rules`) |
| 06 | Pass-the-Hash — NTLM Network Logon | 4624 | T1550.002 | Critical | Planned |
| 07 | Suspicious PowerShell Execution | 1 (Sysmon) | T1059.001 | High | Planned |
| 08 | LSASS Memory Access | 10 (Sysmon) | T1003.001 | Critical | Planned |
