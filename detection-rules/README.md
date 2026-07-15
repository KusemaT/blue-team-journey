# Detection Rules

All rules cover both Splunk SPL and Microsoft Sentinel KQL.
Each rule includes: ATT&CK technique, false positive notes, and response actions.

## Rules Library

| # | Rule Name | EventID | ATT&CK | Severity |
|---|-----------|---------|--------|----------|
| 01 | Brute Force — Failed Logon Threshold | 4625 | T1110 | Medium |
| 02 | New User Account Created | 4720 | T1136.001 | High |
| 03 | User Added to Privileged Group | 4732 | T1078.002 | High |
| 04 | New Service Installed | 7045 | T1543.003 | High |
| 05 | Kerberoasting — RC4 Ticket Request | 4769 | T1558.003 | High |
| 06 | Pass-the-Hash — NTLM Network Logon | 4624 | T1550.002 | Critical |
| 07 | Suspicious PowerShell Execution | 1 (Sysmon) | T1059.001 | High |
| 08 | LSASS Memory Access | 10 (Sysmon) | T1003.001 | Critical |
