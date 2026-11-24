# Blue Team Journey 🛡️

**Tadiwanashe Kusema** | BSc Cyber Security, University of Derby | Aspiring Blue Team Analyst

Hands-on blue team practice for UK SOC analyst roles: detection engineering, DFIR, and incident response, built in a home lab.
No certifications held yet.

---

## 🔧 Home Lab Stack

| Component | Tool | Purpose |
|-----------|------|---------|
| Hypervisor | VirtualBox | Runs all VMs |
| Attacker | Kali Linux | Attack simulation |
| Target | Windows 10 + Sysmon | Endpoint telemetry |
| SIEM 1 | Splunk Enterprise (free) | SPL detection rules |
| SIEM 2 | Microsoft Sentinel (Azure) | KQL detection rules |
| Network IDS | Security Onion + Zeek | Network visibility |
| Memory forensics | Volatility3 | RAM analysis |
| Disk forensics | KAPE + EZ Tools | Artefact collection |
| AD lab | Windows Server + lab.local | Attack path simulation |

---

## 📁 Repository Structure
blue-team-journey/
├── detection-rules/       # SPL + KQL detection rules with ATT&CK mapping
├── sigma-rules/           # Vendor-agnostic Sigma YAML rules
├── scripts/               # Python + PowerShell SOC automation tools
├── writeups/              # CTF writeups with ATT&CK + detection queries
├── tickets/               # Mock incident tickets (ServiceNow + Jira format)
├── reports/               # Professional forensic investigation reports
├── docs/                  # Supporting documentation
└── ad-lab/                # Active Directory lab notes and findings
---

## 🎯 Skills

**SIEM:** Splunk SPL · Microsoft Sentinel KQL · Detection rule authoring · Sigma CI/CD pipeline

**Windows Event IDs:** 4624 · 4625 · 4634 · 4740 · 4720 · 4732 · 7045 · 7036

**Scripting:** Python (IOC enrichment, SOAR automation, Jinja2 reports) · PowerShell (log queries, forensic triage)

**DFIR:** Volatility3 · KAPE · PECmd · LECmd · RECmd · Autopsy

**Frameworks:** MITRE ATT&CK · PICERL · Cyber Kill Chain · UK GDPR · Cyber Essentials

**EDR awareness:** CrowdStrike Falcon Fundamentals (CrowdStrike University)

---

## 📊 Plan and Progress

| Month | Focus | Output |
|-------|-------|-----------|
| Month 1 | Lab build and detection rules | Lab running; first detection rules and one CTF writeup in progress |
| Month 2 | DFIR depth | Further CTF writeups and forensic reports (planned) |
| Month 3 | Capstone project and job search | Capstone project (planned) |
