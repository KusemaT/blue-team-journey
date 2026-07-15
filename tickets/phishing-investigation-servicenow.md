# Incident Ticket — Phishing Investigation (ServiceNow Format)

**Incident Number:** INC0000001
**Category:** Security
**Subcategory:** Phishing
**Priority:** 2 — High
**State:** In Progress
**Assigned To:** SOC Tier 1

---

**Short Description:** Suspected phishing email targeting finance team — malicious URL detected

**Description:**
A phishing email was received by [user] in the finance department at [timestamp].
The email claimed to be from [legitimate-looking sender] and contained a link
to [suspicious domain].

**Investigation Steps Taken:**

1. Examined email headers — true origin IP identified as [IP] via Received headers (bottom to top)
2. Checked origin IP on AbuseIPDB — score: [X]/100 ([X] reports)
3. Submitted URL to URLScan.io — [result: malicious/benign/suspicious]
4. Submitted URL to VirusTotal — [X] malicious detections
5. Checked if any users clicked the link — [result]

**ATT&CK Technique:** T1566.002 — Phishing: Spearphishing Link

**Verdict:** True Positive — Malicious phishing email

**Immediate Actions Taken:**
- Email deleted from user mailbox
- URL submitted to email security vendor for blocking
- User informed and reminded of phishing reporting procedure

**Resolution Code:** True Positive — Malicious
**Resolution Notes:** Origin IP scored [X]/100 on AbuseIPDB. URL confirmed malicious via URLScan and VirusTotal. No credentials entered by user (confirmed via interview).
