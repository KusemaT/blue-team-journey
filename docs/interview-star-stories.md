# Interview STAR Stories

Five prepared answers for common UK SOC analyst interview questions.
Format: Situation → Task → Action → Result

---

## Q1: "Walk me through how you would investigate a suspicious logon alert."

**Situation:** In my home lab, I created a Splunk alert that fires when 5 or more
failed logons occur for the same account within 10 minutes (EventID 4625 — ATT&CK T1110).

**Task:** When the alert fired during testing, I needed to determine whether this
was a genuine brute force attempt or a false positive.

**Action:** I ran my SPL query to see the source IP, time window, and account name.
I checked whether any EventID 4624 (successful logon) followed the failed attempts
from the same source. I checked the source IP on AbuseIPDB and VirusTotal using
my Python enrichment script. I checked whether the target account was privileged.

**Result:** In my test case, I detected that 6 failed logons for the jsmith account
were followed by a successful logon from the same IP — indicating brute force success.
I escalated this as a True Positive and documented it in a Jira-format mock incident
ticket with the ATT&CK technique (T1110.001) and immediate response actions.

---

## Q2: "How do you prioritise multiple alerts firing simultaneously?"

**Situation:** In my home lab Splunk dashboard, I monitor detection rules covering
8 different Windows Event IDs simultaneously.

**Task:** If multiple alerts fired at once, I would need to triage them quickly
without missing the most critical one.

**Action:** I prioritise using three factors: (1) Severity — a Kerberoasting alert
(T1558.003) or LSASS access alert (T1003.001) gets priority over a single failed
logon because the potential impact of credential theft is higher than one failed
password attempt. (2) Account type — a privilege escalation alert targeting an
admin account is higher priority than the same alert for a standard user. (3)
Correlated indicators — if a brute force alert and a new service installed alert
fire for the same host within minutes, that correlation elevates priority even if
each alert is individually medium severity.

**Result:** I document this prioritisation logic in my detection rule response
actions — each rule has a numbered escalation decision tree that a Tier 1 analyst
can follow at 3am without needing to think it through from scratch.

---

## Q3: "What do you know about CrowdStrike Falcon?"

**Situation:** I completed the CrowdStrike Falcon Fundamentals course on CrowdStrike
University — a free course available without a Falcon licence.

**Task:** I wanted to understand the #1 EDR platform deployed in UK enterprise.

**Action:** The course covered: the sensor architecture (a lightweight kernel-level
agent that streams telemetry — process starts, network connections, file writes,
registry changes — to the cloud for real-time analysis, rather than running heavy
on-device scanning), the detection types (indicator-based for known malware,
behaviour-based for suspicious patterns regardless of whether the file is known,
and AI/ML-based models that score activity), and the Falcon console workflow
(how analysts triage detections, read process trees, and investigate incidents).

**Result:** I can now discuss Falcon architecture confidently in interviews. I
understand why Falcon catches fileless malware and zero-days that traditional AV
misses: it analyses behaviour in the cloud rather than matching file signatures
on the device. Charlotte AI, CrowdStrike's built-in AI assistant, helps analysts
understand detections and suggests investigation steps.

---

## Q4: "Tell me about a time you learned something new quickly."

**Situation:** I built a dual-SIEM home lab from scratch over 3 months while studying
for certifications.

**Task:** I had to learn Splunk SPL and Microsoft Sentinel KQL simultaneously —
two different query languages with different syntax but similar logical structure.

**Action:** I wrote the same detection for each Windows Event ID in both languages
side by side in a GitHub document (detection-rules/spl-vs-kql-comparison.md).
By always writing the KQL equivalent immediately after the SPL query, I learned
to translate between them rather than learning each in isolation. I also set up
a GitHub Actions CI/CD pipeline that auto-converts my Sigma rules to both SPL
and KQL, which gave me immediate feedback when my syntax was wrong.

**Result:** After two weeks I was comfortable writing detections in both languages.
By the end of Month 1 I had 10+ detection rules in both SPL and KQL, each with
ATT&CK technique IDs, false positive notes, and response actions.

---

## Q5: "Why blue team rather than red team or development?"

**Situation:** When choosing my specialisation in cybersecurity, I considered
penetration testing, development, and blue team SOC work.

**Task:** I needed to identify where my skills and interests genuinely aligned.

**Action:** I researched what each role actually does day-to-day. Blue team work
appealed to me because it combines real-time problem solving (investigating live
alerts), analytical thinking (correlating evidence across multiple log sources),
and direct impact (you are protecting real organisations and real people). I also
found the UK job market for blue team roles to be strong — the NCSC reports a
consistent skills gap in defensive security roles.

**Result:** I committed to blue team and built a structured 3-month programme
covering detection engineering, DFIR, and the certifications UK employers look
for. Security+ and BTL1 give me credentials. The home lab gives me demonstrable
practical experience. The GitHub portfolio shows the work publicly.
