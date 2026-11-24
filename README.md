# Blue Team Journey 🛡️

**Tadiwanashe Kusema** | BSc Cyber Security, University of Derby | Coventry, UK

Hands-on blue team practice for UK SOC analyst roles: detection engineering, incident response, and threat hunting, built in a home lab. This repo holds the detection rules, scripts, and write-ups behind that work.

Items marked *planned* are not yet in the repo. Open to graduate SOC and detection roles in the UK, and open to relocation.

---

## 🔧 Home Lab (target stack)

| Component | Tool | Purpose |
|-----------|------|---------|
| Hypervisor | VirtualBox | Runs all VMs on an isolated network |
| Attacker | Kali Linux | Controlled attack simulation |
| Endpoint | Windows 10 or 11 + Sysmon | Endpoint telemetry |
| SIEM 1 | Splunk Enterprise (free licence) | SPL detection rules |
| SIEM 2 | Microsoft Sentinel (Azure) | KQL detection rules |
| AD lab | Windows Server + lab.local | Attack path simulation |
| Network IDS | Security Onion + Zeek *(planned)* | Network visibility |
| Memory forensics | Volatility3 *(planned)* | RAM analysis |
| Disk forensics | KAPE + EZ Tools *(planned)* | Artefact collection |

---

## 📁 Repository Structure

```
blue-team-journey/
├── detection-rules/   # SPL + KQL detection rules with ATT&CK mapping
├── sigma-rules/       # Vendor-agnostic Sigma YAML rules, converted by CI
├── scripts/           # Python SOC tools (PowerShell planned)
├── writeups/          # CTF write-ups (first one is a draft)
├── tickets/           # Mock incident tickets for practice (templates)
├── docs/              # Interview preparation notes
├── reports/           # Forensic investigation reports (planned)
├── ad-lab/            # Active Directory lab notes (planned)
└── .github/workflows/ # CI pipeline that converts Sigma rules
```

---

## 🎯 Skills Shown in This Repo

**Detection:** Splunk SPL · Microsoft Sentinel KQL · Sigma rule format · MITRE ATT&CK mapping

**Windows event IDs used:** 4624 · 4625 · 4720 · 4732 · 4740 · 4769 · 7045 · Sysmon 1 and 10

**Scripting:** Python (threat-intelligence API enrichment, HTML triage reports)

**Frameworks:** MITRE ATT&CK · UK GDPR · Cyber Essentials (study)

**Learning in progress:** Microsoft Entra ID and Sentinel identity detections · Defender for Endpoint · AI-assisted alert triage (planned)

**EDR awareness:** CrowdStrike Falcon Fundamentals (CrowdStrike University, free course)

---

## 📊 Plan and Progress

| Month | Focus | Output |
|-------|-------|--------|
| Month 1 | Lab build and detection rules | Lab running; first detection rule and CTF write-up in progress |
| Month 2 | Identity detections and DFIR depth | Further detections and write-ups (planned) |
| Month 3 | Capstone project and job search | Capstone project (planned) |
