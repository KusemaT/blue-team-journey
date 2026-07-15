# Brute Force — Failed Logon Threshold

**ATT&CK Technique:** T1110 — Brute Force
**EventID:** 4625 (Windows Security Log — Failed Logon)
**Severity:** Medium
**Data Source:** Windows Security Event Log

---

## Detection Logic

**Trigger:** 5 or more failed logon attempts for the same account within a 10-minute window.

### Splunk SPL

```spl
index=* EventCode=4625
| bin _time span=10m
| stats count by Account_Name, _time
| where count >= 5
| eval attck_technique="T1110"
| table _time, Account_Name, count, attck_technique
```

### Microsoft Sentinel KQL

```kql
SecurityEvent
| where EventID == 4625
| bin TimeGenerated span=10m
| summarize FailedCount=count() by Account, bin(TimeGenerated, 10m)
| where FailedCount >= 5
| extend ATT_CK = "T1110 - Brute Force"
| project TimeGenerated, Account, FailedCount, ATT_CK
```

---

## False Positives

- User genuinely forgot their password — check if lockout (EventID 4740) followed
- IT helpdesk testing lockout policy — filter by known IT admin workstations
- Automated script with hardcoded credentials after a password change

## Response Actions

1. Check whether any EventID 4624 (successful logon) followed the failed attempts for the same account — if yes, escalate immediately (brute force may have succeeded)
2. Check the source workstation or IP — is it internal or external?
3. Check the target account — is it a privileged account (admin, service account)?
4. If external source IP: check on AbuseIPDB and VirusTotal
5. If no successful logon followed: document as attempted brute force, close as low priority
6. If successful logon followed from suspicious source: escalate to Tier 2, consider account suspension
