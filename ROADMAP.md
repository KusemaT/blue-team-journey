# Blue Team SOC Analyst Roadmap
> 3-Month Rapid Sprint · Security+ → BTL1 → SC-200 · Start: 1 June 2026
> 
> **Usage:** Run `python3 roadmap_updater.py complete "Task name"` to mark tasks done and auto-push to GitHub.

---

## Legend
- `[ ]` Not started
- `[x]` Complete
- `[~]` In progress

---

## MONTH 1 — Foundations + Security+ Exam
> Target: Security+ passed by Week 3 · Dual-SIEM lab running · 10+ detection rules

### Week 1 — Lab Setup + Security+ Study Begin

#### Day 1 — Monday 1 June
- [ ] Enrol on Professor Messer Security+ SY0-701 (free): go to professormesser.com → Study Materials → SY0-701 → create account
- [ ] Watch 1.1 Security Controls: note 4 control types (Technical, Managerial, Operational, Physical) and 6 functions (Preventive, Detective, Corrective, Deterrent, Compensating, Directive)
- [ ] Watch 1.2 Fundamental Security Concepts: note CIA Triad definitions and non-repudiation
- [ ] Create Quizlet set "Security+ Domain 1": go to quizlet.com → Create → Generate with AI → type "Security+ control types and CIA Triad flashcards" → review and save
- [ ] Download VirtualBox from virtualbox.org → install with default settings
- [ ] Download Kali Linux OVA from kali.org/get-kali → Virtual Machines → VirtualBox (3.5GB — start immediately)
- [ ] Create GitHub repo: github.com → New Repository → name "blue-team-journey" → Public → tick Add README → Create
- [ ] Edit README.md: add your name, cert plan table, skills section, link to roadmap

#### Day 2 — Tuesday 2 June
- [ ] Import Kali OVA: VirtualBox → File → Import Appliance → select OVA → Import → Start → login kali/kali
- [ ] Take Kali snapshot: Machine → Take Snapshot → name "Clean Install"
- [ ] Create Azure free account: portal.azure.com → Start free → use personal Microsoft account → confirm $200 credit
- [ ] Create Sentinel workspace: Azure portal → search "Microsoft Sentinel" → Create → New Log Analytics workspace → Resource Group: SOC-Lab → Name: soc-lab-workspace → Region: UK South → Review + Create → Create
- [ ] Wait 2 minutes for deployment → click Go to Resource → Add Microsoft Sentinel
- [ ] Run first KQL query: Sentinel → Logs → paste below → press Shift+Enter
  ```kql
  SecurityEvent
  | where EventID == 4625
  | summarize FailedLogons=count() by Account
  | sort by FailedLogons desc
  ```
- [ ] Commit to GitHub: create detection-rules/kql-failed-logon-4625.md with query, ATT&CK T1110, FP notes, response actions

#### Day 3 — Wednesday 3 June
- [ ] Watch Professor Messer 2.1 Threat Actors: note APT/nation-state, insider threat, cybercriminal, hacktivist, script kiddie
- [ ] Watch Professor Messer 2.2 Threat Vectors: note phishing (email/smishing/vishing), USB drop, supply chain
- [ ] Watch Professor Messer Symmetric vs Asymmetric Encryption: AES-256 = symmetric (one key, fast), RSA = asymmetric (key pair, slower)
- [ ] Watch Professor Messer PKI: Certificate Authorities bind public keys to identities — underpins every HTTPS connection
- [ ] Watch Professor Messer Firewall types: packet filter → stateful → NGFW (deep packet inspection)
- [ ] Watch Professor Messer IDS vs IPS: IDS = passive/alerts, IPS = inline/blocks
- [ ] Read 10 min about AI in SOC 2026: search "Microsoft Security Copilot SOC 2026" → note 3 bullet points in GitHub docs/ai-in-soc-notes.md
- [ ] Generate Quizlet AI cards: "Threat actors, cryptography, firewall types, IDS vs IPS"

#### Day 4 — Thursday 4 June
- [ ] Download Windows 10 evaluation ISO: microsoft.com/en-us/evalcenter → Windows 10 Enterprise → 64-bit (5GB — start immediately)
- [ ] Create Windows 10 VM: VirtualBox → New → Name: Win10-Lab → Type: Microsoft Windows → Version: Windows 10 64-bit → RAM: 4096MB → Create VHD → VDI → Dynamically allocated → 50GB → Settings → System → Processor → 2 CPUs → Storage → attach ISO → Start
- [ ] Install Windows 10: Install Now → No product key → Windows 10 Pro → Custom → accept disk → wait 15-20 min → create local account (no Microsoft account)
- [ ] Take snapshot: "Post-Install Clean"
- [ ] Download Sysmon: learn.microsoft.com/sysinternals/downloads/sysmon
- [ ] Download SwiftOnSecurity config: github.com/SwiftOnSecurity/sysmon-config → sysmonconfig.xml → Raw → save file
- [ ] Install Sysmon: Windows VM → PowerShell as Administrator → cd to download folder → run: `.\Sysmon64.exe -accepteula -i sysmonconfig.xml`
- [ ] Verify Sysmon: Event Viewer → Applications and Services Logs → Microsoft → Windows → Sysmon → Operational → confirm events appearing
- [ ] Memorise 8 key Event IDs (write on sticky note): 4624=logon, 4625=failed logon, 4634=logoff, 4740=lockout, 4720=new user, 4732=priv group add, 7045=new service, 7036=service state
- [ ] Commit: docs/event-id-reference.md with all 8 Event IDs, ATT&CK techniques, and detection sources

#### Day 5 — Friday 5 June
- [ ] Watch Professor Messer IAM: MFA factors (know/have/are/location/behaviour), SSO, Active Directory, RBAC, least privilege, PAM
- [ ] Watch Professor Messer GRC: NIST CSF 5 functions (Identify/Protect/Detect/Respond/Recover), ISO 27001, risk management
- [ ] Study UK GDPR: 72-hour breach notification to ICO required — this is law, not guidance
- [ ] Study Cyber Essentials: 5 controls — firewalls, secure configuration, user access control, malware protection, patch management — required for UK government contracts
- [ ] Watch YouTube "ServiceNow Security Incident Response overview" (15 min): note incident fields (Priority, Category, Assignment Group, Short Description, Resolution Code)
- [ ] Generate Quizlet AI cards: "IAM, GRC, NIST CSF, UK GDPR, Cyber Essentials"

#### Day 6 — Saturday 6 June (3 hours Deep Work)
- [ ] Install Wireshark: wireshark.org → download for your OS → install with defaults
- [ ] Capture live traffic: Wireshark → select active network adapter → blue shark fin → browse 5 websites → stop after 2 min
- [ ] Apply dns filter: note 3-5 domain lookups you see
- [ ] Apply http filter: find GET request → right-click → Follow → HTTP Stream → read User-Agent header
- [ ] Commit: writeups/wireshark-first-capture.md — what you saw, what the User-Agent was, what surprised you
- [ ] Read MITRE ATT&CK T1566 Phishing in full: attack.mitre.org/techniques/T1566 — all 3 sub-techniques, detection section
- [ ] Read MITRE ATT&CK T1543.003 Windows Service in full: maps to EventID 7045
- [ ] Install Splunk Enterprise free: splunk.com/en_us/download → Splunk Enterprise → Windows → install → access at http://localhost:8000 → set admin password
- [ ] Configure Splunk data input: Settings → Data Inputs → Local Event Log Collection → Add New → select Microsoft-Windows-Sysmon/Operational → Save
- [ ] Verify Splunk ingestion: Search & Reporting → run: `index=* EventCode=1 | table _time, Image, CommandLine | head 20`
- [ ] Write 3 SPL detection rules and commit to detection-rules/:
  - `index=* EventCode=4625 | stats count by Account_Name | sort -count` (T1110)
  - `index=* EventCode=1 Image=*powershell* (CommandLine="*-ExecutionPolicy Bypass*" OR CommandLine="*-EncodedCommand*") | table _time, CommandLine` (T1059.001)
  - `index=* EventCode=7045 | table _time, Service_Name, Service_File_Name | where NOT like(Service_Name,"%Windows%")` (T1543.003)
- [ ] Enrol CrowdStrike Falcon Fundamentals (free): university.crowdstrike.com → Falcon Fundamentals → complete all modules (~2 hours)
- [ ] Update LinkedIn headline: "Cybersecurity Student | Blue Team | Splunk · Sentinel KQL · MITRE ATT&CK | Building in public"
- [ ] Post LinkedIn Week 1 update with screenshot of Splunk dashboard

#### Day 7 — Sunday 7 June (45 min Review)
- [ ] Quizlet AI: generate cards for weakest topic from this week
- [ ] Run Security+ practice: 30 questions on professormesser.com/practice-exams → record domain scores
- [ ] Write Week 1 GitHub commit: README.md — what you built, what surprised you, what comes next
- [ ] Apply to 2-3 UK junior SOC positions: Bridewell / e2e-assure / Quorum Cyber / Littlefish / NCC Group

---

### Week 2 — Splunk + Sentinel Dual Detection + Volatility3

#### Day 8 — Monday 9 June
- [ ] Watch Professor Messer Vulnerability Management: CVSS scoring Critical 9-10 (24hrs), High 7-8.9 (7 days), Medium 4-6.9 (30 days)
- [ ] Watch Professor Messer PICERL IR lifecycle: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned
- [ ] Watch Professor Messer Order of Volatility: RAM first (lost on power off) → running processes → disk → backups
- [ ] Watch Professor Messer Chain of Custody: documentation proving evidence not tampered with
- [ ] Watch Professor Messer EDR vs AV: AV matches signatures, EDR detects behaviour — CrowdStrike Falcon, SentinelOne, MDE are top UK EDR platforms
- [ ] Generate Quizlet AI cards: "CVSS, PICERL, order of volatility, EDR vs AV"

#### Day 9 — Tuesday 10 June
- [ ] Create Splunk brute force alert: Search → `index=* EventCode=4625 | bin _time span=10m | stats count by Account_Name,_time | where count>=5` → Save As Alert → run every 5 min → Add to Triggered Alerts
- [ ] Test Splunk alert: wrong password 6 times on Windows VM → Activity → Triggered Alerts → confirm fires
- [ ] Create Sentinel Analytics Rule: Sentinel → Analytics → Create → Scheduled query rule → paste KQL:
  ```kql
  SecurityEvent
  | where EventID == 4625
  | bin TimeGenerated span=10m
  | summarize FailedCount=count() by Account, bin(TimeGenerated,10m)
  | where FailedCount >= 5
  ```
  → Schedule every 5 min → threshold > 0 → Create
- [ ] Write PowerShell failed logon script: Windows VM PowerShell as Admin:
  ```powershell
  Get-WinEvent -LogName Security -MaxEvents 200 |
  Where-Object {$_.Id -eq 4625} |
  Select-Object TimeCreated, @{N="Account";E={$_.Properties[5].Value}}, @{N="Source";E={$_.Properties[19].Value}} |
  Export-Csv failed-logons.csv -NoTypeInformation
  ```
- [ ] Commit: detection-rules/brute-force-4625.md (SPL + KQL + ATT&CK T1110 + FP notes + response actions), scripts/powershell-soc-basics.ps1

#### Day 10 — Wednesday 11 June
- [ ] Watch Professor Messer Cloud Security: IaaS/PaaS/SaaS shared responsibility, S3 misconfiguration risks, IAM excessive permissions
- [ ] Watch Professor Messer OWASP Top 10: SQL injection, XSS, broken authentication, IDOR
- [ ] Study SOAR concepts: alert fires → auto-enrich IOC → auto-ticket → analyst reviews pre-enriched case
- [ ] Generate Quizlet AI cards: "cloud security, OWASP, SOAR concepts"

#### Day 11 — Thursday 12 June
- [ ] Install Active Directory on Windows VM: Server Manager → Add Roles and Features → Active Directory Domain Services → Install → Promote to domain controller → Add new forest → Root domain: lab.local → DSRM password → Install → reboot
- [ ] Create 3 AD test accounts: Active Directory Users and Computers → right-click Users → New → User:
  - jsmith / Password1 (standard user)
  - hradmin / Password1 (HR admin)
  - svc_backup / Password1 (service account — tick Password never expires)
- [ ] Install Python 3 on Mac: already installed — verify with `python3 --version` in terminal
- [ ] Get free API keys: virustotal.com (sign up → profile → API Key), abuseipdb.com (sign up → API → Create Key)
- [ ] Write Python IP enricher: save as scripts/ip-enricher.py:
  ```python
  import requests, os, sys
  VT_KEY = os.environ.get("VT_KEY","")
  ABUSE_KEY = os.environ.get("ABUSE_KEY","")
  ip = sys.argv[1] if len(sys.argv)>1 else "8.8.8.8"
  vt = requests.get(f"https://www.virustotal.com/api/v3/ip_addresses/{ip}",
      headers={"x-apikey":VT_KEY}).json()
  abuse = requests.get("https://api.abuseipdb.com/api/v2/check",
      params={"ipAddress":ip},
      headers={"Key":ABUSE_KEY,"Accept":"application/json"}).json()
  mal = vt["data"]["attributes"]["last_analysis_stats"]["malicious"]
  score = abuse["data"]["abuseConfidenceScore"]
  verdict = "MALICIOUS" if mal>3 or score>50 else "SUSPICIOUS" if mal>0 or score>10 else "CLEAN"
  print(f"IP: {ip} | VT Malicious: {mal} | AbuseScore: {score}/100 | Verdict: {verdict}")
  ```
- [ ] Run it: `export VT_KEY="your_key" && export ABUSE_KEY="your_key" && python3 scripts/ip-enricher.py 1.2.3.4`
- [ ] Commit: ad-lab/lab-setup.md (AD config, 3 test accounts), scripts/ip-enricher.py

#### Day 12 — Friday 13 June
- [ ] Install Volatility3 on Kali: open Kali terminal → `pip3 install volatility3`
- [ ] Download practice memory image: github.com/volatilityfoundation/volatility3/wiki/Memory-Samples → download any Windows sample
- [ ] Run 4 core Volatility3 plugins:
  ```bash
  python3 vol.py -f memory.dmp windows.pslist
  python3 vol.py -f memory.dmp windows.netscan
  python3 vol.py -f memory.dmp windows.cmdline
  python3 vol.py -f memory.dmp windows.malfind
  ```
- [ ] Note what each shows: pslist=running processes, netscan=network connections, cmdline=full command lines, malfind=injected code (PAGE_EXECUTE_READWRITE + MZ header)
- [ ] Write Python Volatility3 auto-runner: scripts/volatility-auto.py:
  ```python
  import subprocess, os, sys
  mem = sys.argv[1] if len(sys.argv)>1 else "memory.dmp"
  plugins = ["windows.pslist","windows.netscan","windows.cmdline","windows.malfind"]
  os.makedirs("vol-output", exist_ok=True)
  for p in plugins:
      with open(f"vol-output/{p.replace('.', '-')}.txt","w") as f:
          subprocess.run(["python3","vol.py","-f",mem,p], stdout=f, stderr=subprocess.DEVNULL)
      print(f"Done: {p}")
  print("All plugins complete. Results in vol-output/")
  ```
- [ ] Run it: `python3 scripts/volatility-auto.py memory.dmp`
- [ ] Commit: docs/volatility3-findings.md, scripts/volatility-auto.py

#### Day 13 — Saturday 14 June (3 hours)
- [ ] Run Security+ full mock exam: 90 questions, 90 minutes, no notes — professormesser.com/practice-exams
- [ ] Record domain scores — identify weakest domain
- [ ] Download KAPE: ericzimmerman.github.io → KAPE → download and extract
- [ ] Run KAPE on Windows VM: Admin command prompt → `kape.exe --tsource C: --tdest C:\kape-output --tflush --target !BasicCollection`
- [ ] Parse prefetch with PECmd: `PECmd.exe -d C:\kape-output\C\Windows\Prefetch --csv C:\prefetch-output.csv`
- [ ] Open prefetch CSV: note every program that ran, when it last ran, how many times
- [ ] Write 5 more detection rules bringing library to 8+ total (one per remaining Event ID): detection-rules/new-user-4720.md, detection-rules/priv-group-add-4732.md, detection-rules/account-lockout-4740.md, detection-rules/kerberoasting-4769.md, detection-rules/pass-the-hash-4624.md
- [ ] Apply to 3 UK positions — tailored cover paragraphs mentioning dual-SIEM lab

#### Day 14 — Sunday 15 June (45 min)
- [ ] Quizlet AI: generate cards for weakest Security+ domain from Saturday mock
- [ ] Drill 40 targeted questions on weakest domain only
- [ ] Commit: detection-rules/ — verify all 8+ rules have ATT&CK IDs, FP notes, response actions
- [ ] Apply to 2 more positions

---

### Week 3 — Security+ Exam + Sigma CI/CD + Kerberoasting Lab

#### Day 15 — Monday 16 June
- [ ] Drill weakest Security+ domain: 40 targeted questions — professormesser.com/practice-exams with domain filter
- [ ] For each wrong answer: Quizlet → Create → Generate with AI → type the specific concept → review cards
- [ ] Set up Sigma rules folder in GitHub: create sigma-rules/README.md
- [ ] Create first Sigma rule: sigma-rules/brute-force.yml:
  ```yaml
  title: Brute Force - Failed Logon Threshold
  status: experimental
  description: Detects 5+ failed logons for same account indicating brute force
  tags: [attack.credential_access, attack.t1110]
  logsource:
      product: windows
      service: security
  detection:
      selection:
          EventID: 4625
      condition: selection
  falsepositives: [User forgot password, IT testing lockout policy]
  level: medium
  ```
- [ ] Create .github/workflows/sigma-convert.yml:
  ```yaml
  name: Convert Sigma Rules
  on:
    push:
      paths: ['sigma-rules/*.yml']
  jobs:
    convert:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - run: pip install sigma-cli
        - run: sigma plugin install splunk
        - run: sigma plugin install microsoft365defender
        - run: mkdir -p detection-rules/auto-converted
        - run: sigma convert -t splunk sigma-rules/ > detection-rules/auto-converted/converted-splunk.txt
        - run: sigma convert -t microsoft365defender sigma-rules/ > detection-rules/auto-converted/converted-kql.txt
        - uses: actions/upload-artifact@v3
          with: {name: converted-rules, path: detection-rules/auto-converted/}
  ```
- [ ] Push to GitHub → check Actions tab → verify workflow runs green

#### Day 16 — Tuesday 17 June
- [ ] Book Security+ exam: home.pearsonvue.com/comptia → CompTIA → Security+ SY0-701 → Online Proctored → choose date this week → pay ~£350
- [ ] Book BTL1 exam: securityblue.team/b1 → purchase (~£399) → book exam for Month 2 Week 4
- [ ] Simulate Kerberoasting:
  - Windows VM PowerShell: `Set-ADUser svc_backup -ServicePrincipalNames @{Add="MSSQLSvc/db.lab.local:1433"}`
  - Kali terminal: `python3 /usr/share/doc/python3-impacket/examples/GetUserSPNs.py lab.local/jsmith:Password1 -dc-ip [WIN-VM-IP] -request`
  - You should see a ticket hash printed for svc_backup
- [ ] Detect Kerberoasting in Splunk: `index=* EventCode=4769 Ticket_Encryption_Type=0x17 | table _time, Account_Name, Service_Name`
- [ ] Detect in Sentinel:
  ```kql
  SecurityEvent
  | where EventID == 4769
  | where TicketEncryptionType == "0x17"
  | project TimeGenerated, Account, ServiceName, Computer
  ```
- [ ] Write mock Jira ticket: tickets/kerberoasting-jira.md — Summary: [HIGH] Kerberoasting Detected — svc_backup, ATT&CK T1558.003, Immediate Action: reset svc_backup password
- [ ] Commit: detection-rules/kerberoasting-4769.md (SPL + KQL), tickets/kerberoasting-jira.md

#### Day 17 — Wednesday 18 June
- [ ] Complete first LetsDefend investigation: letsdefend.io → Sign Up → Alert tab → pick any alert → check IOCs on VirusTotal + AbuseIPDB → verdict → reasoning → submit → compare to official answer
- [ ] Write Python email header parser: scripts/email-header-parser.py:
  ```python
  import email, re, sys
  def parse_email(path):
      msg = email.message_from_file(open(path))
      rx = msg.get_all("Received", [])
      ips = [re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",h).group()
             for h in rx if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",h)]
      print(f"Subject: {msg['Subject']}")
      print(f"From: {msg['From']}")
      print(f"Origin IPs (oldest first): {ips[::-1]}")
  if __name__ == "__main__":
      parse_email(sys.argv[1])
  ```
- [ ] Commit: scripts/email-header-parser.py, writeups/letsdefend-investigation-01.md

#### Day 18 — Thursday 19 June
- [ ] Simulate Pass-the-Hash:
  - Kali: `python3 /usr/share/doc/python3-impacket/examples/secretsdump.py lab.local/jsmith:Password1@[WIN-IP]`
  - Copy NT hash from output
  - Kali: `python3 /usr/share/doc/python3-impacket/examples/smbclient.py lab.local/administrator@[WIN-IP] -hashes aad3b435b51404eeaad3b435b51404ee:[NT-HASH]`
- [ ] Detect Pass-the-Hash in Splunk: `index=* EventCode=4624 Logon_Type=3 Logon_Process=NtLmSsp | stats count by Account_Name,Workstation_Name | where count>2`
- [ ] Detect in Sentinel:
  ```kql
  SecurityEvent
  | where EventID == 4624
  | where LogonType == 3
  | where AuthenticationPackageName == "NTLM"
  | summarize count() by Account, Computer, IpAddress
  | where count_ > 2
  ```
- [ ] Write mock Jira ticket: tickets/pass-the-hash-jira.md — [CRITICAL], ATT&CK T1550.002, Immediate Action: isolate source machine
- [ ] Commit: detection-rules/pass-the-hash-4624.md, tickets/pass-the-hash-jira.md

#### Day 19 — Friday 20 June
- [ ] Light Quizlet review only — all sets, no new material
- [ ] Read Security+ exam objectives PDF: comptia.org/certifications/security → download objectives → tick every confident topic → Quizlet AI cards for any unticked topic
- [ ] Prepare exam environment: clear desk, test webcam and microphone, have government photo ID ready, confirm stable internet connection
- [ ] Read Pearson VUE online proctored exam requirements: home.pearsonvue.com/test-taker/security — no notes, no second monitors, no phone visible

#### Day 20 — Saturday 21 June (3 hours)
- [ ] SECURITY+ SY0-701 EXAM DAY — sit the exam
- [ ] Post result on LinkedIn immediately after
- [ ] Update README.md cert table with result
- [ ] Build Splunk SOC dashboard: Splunk → Dashboards → Create New → add 4 panels:
  - Panel 1: `index=* EventCode=4625 | timechart span=1h count` (title: Failed Logons Over Time)
  - Panel 2: `index=* EventCode=4720 earliest=-24h | table _time, Account_Name` (title: New Accounts Today)
  - Panel 3: `index=* EventCode=7045 earliest=-24h | table _time, Service_Name, Service_File_Name` (title: New Services Today)
  - Panel 4: `index=* EventCode=4732 earliest=-7d | table _time, Account_Name, Group_Name` (title: Privileged Group Changes)
- [ ] Install BloodHound on Kali: `sudo apt install bloodhound`
- [ ] Run SharpHound on Windows AD VM: download SharpHound.exe from github.com/SpecterOps/SharpHound → run `SharpHound.exe --CollectionMethods All` → copy ZIP to Kali
- [ ] Import to BloodHound: start neo4j → start bloodhound → drag ZIP → run "Shortest Paths to Domain Admins"
- [ ] Document one attack path: ad-lab/bloodhound-analysis.md

#### Day 21 — Sunday 22 June (45 min)
- [ ] Quizlet AI: generate cards for any exam topics that came up unexpectedly
- [ ] Write post-exam reflection in docs/: what topics appeared most, what surprised you
- [ ] Apply to 3 positions with updated CV showing Security+ passed

---

### Week 4 — Deep Lab + BTL1 Modules 1-6 + Portfolio Polish

#### Day 22 — Monday 23 June
- [ ] Complete BTL1 Module 1 (Security Fundamentals): fast review, concepts already covered
- [ ] Complete BTL1 Module 2 (Phishing Analysis): time yourself — full triage (header → origin IP → AbuseIPDB → URLScan → verdict) target under 18 minutes
- [ ] Build Sentinel SOAR playbook: Sentinel → Automation → Create playbook → Logic Apps designer → trigger: incident created → HTTP GET to https://api.abuseipdb.com/api/v2/check?ipAddress=[incident IP] → headers: Key=YOUR_KEY, Accept=application/json → Parse JSON → Add comment to incident with abuse score
- [ ] Create Sentinel Automation Rule to trigger playbook on all new incidents
- [ ] Commit: docs/btl1-module-1-2-notes.md, sentinel-playbooks/ip-enricher-playbook.md

#### Day 23 — Tuesday 24 June
- [ ] Complete BTL1 Module 3 (Threat Intelligence): IOC types (hash/IP/domain/URL), STIX/TAXII, TIP platforms (MISP, ThreatConnect)
- [ ] Write 5 more Sigma rules (library now 10+):
  - sigma-rules/lateral-movement-4624.yml (T1550.002)
  - sigma-rules/scheduled-task-4698.yml (T1053.005)
  - sigma-rules/powershell-encoded-command.yml (T1059.001)
  - sigma-rules/lsass-access-sysmon10.yml (T1003.001)
  - sigma-rules/large-outbound-transfer.yml (T1048)
- [ ] Push all 5 → verify CI/CD converts each to SPL and KQL in Actions tab
- [ ] Commit: sigma-rules/ (5 new files), confirm auto-converted/ updated

#### Day 24 — Wednesday 25 June
- [ ] Complete BTL1 Module 4 (SIEM Investigation): work through all Splunk scenarios — time yourself, target 4-hour budget
- [ ] Complete BTL1 Module 5 (Digital Forensics): disk imaging concepts, KAPE artefact collection, Volatility3 memory analysis
- [ ] Build Sentinel Workbook: Sentinel → Workbooks → New → add 4 KQL panels:
  - Panel 1: `SecurityEvent | where EventID==4625 | summarize count() by bin(TimeGenerated,1h) | render timechart`
  - Panel 2: `SecurityEvent | where EventID in (4720,7045) | project TimeGenerated,EventID,Account,Computer`
  - Panel 3: `SecurityEvent | where EventID==4732 | project TimeGenerated,Account,TargetUserName`
  - Panel 4: `SecurityEvent | where EventID==4769 | where TicketEncryptionType=="0x17"`
- [ ] Screenshot workbook → commit to docs/sentinel-workbook-screenshot.md

#### Day 25 — Thursday 26 June
- [ ] Complete BTL1 Module 6 (Dark Web): Tor onion routing, ransomware leak sites, credential marketplaces
- [ ] Write first professional forensic report: reports/memory-forensics-report-01.md
  - Executive Summary (2 non-technical sentences)
  - Investigation Timeline (table: Timestamp | Source | Event | ATT&CK)
  - Technical Findings (each with evidence, ATT&CK ID, interpretation)
  - IOC Summary Table
  - Recommendations (numbered immediate actions)
- [ ] Write CTF writeup template: writeups/ctf-01-packetmaze.md (complete with findings from PacketMaze CTF)
- [ ] Commit: reports/memory-forensics-report-01.md, writeups/ctf-01-packetmaze.md

#### Day 26 — Friday 27 June
- [ ] Full portfolio audit — open GitHub repo as a hiring manager:
  - [ ] README.md: clear skills section, cert plan table, portfolio video link
  - [ ] detection-rules/: 10+ rules, all with ATT&CK IDs, FP notes, response actions, SPL + KQL
  - [ ] sigma-rules/: 5+ rules, CI/CD converting automatically (check Actions tab)
  - [ ] scripts/: ip-enricher.py, email-header-parser.py, volatility-auto.py, powershell-soc-basics.ps1, each with README
  - [ ] tickets/: kerberoasting-jira.md, pass-the-hash-jira.md, phishing-servicenow.md
  - [ ] writeups/: 1+ CTF writeup
  - [ ] reports/: 1 professional forensic report
  - [ ] docs/: event-id-reference.md, btl1-exam-strategy.md, interview-star-stories.md
- [ ] Fix any gaps identified in audit
- [ ] Apply to 5 UK positions with updated profile

#### Day 27 — Saturday 28 June (3 hours)
- [ ] BTL1 full practice run — all 5 domains timed:
  - Phishing: target 90 min
  - Threat Intelligence: target 60 min
  - SIEM Investigation: target 240 min
  - Incident Response: target 180 min
  - Digital Forensics: target 180 min
- [ ] Record time per domain in docs/btl1-speed-log.md
- [ ] Identify slowest domain → schedule extra drilling in Month 2 Week 1
- [ ] Commit: docs/btl1-speed-log.md

#### Day 28 — Sunday 29 June (45 min)
- [ ] Write Month 1 retrospective: docs/month-1-retrospective.md — what completed, what was hard, what surprised you, Month 2 priority
- [ ] Quizlet AI: generate cards for any BTL1 weak areas found in practice run
- [ ] Apply to 3 positions — pipeline should now have 15+ applications in progress

---

## MONTH 2 — BTL1 Preparation + Deep DFIR + Job Hunt
> Target: BTL1 exam passed Week 4 · 10-15 applications/week · Professional forensic reports

### Week 5 — BTL1 Speed Drills + Advanced Detection

- [ ] Monday: BTL1 phishing speed drills — 5 cases, time each, target under 15 min per case
- [ ] Monday: Write 5 advanced KQL hunting queries in Sentinel Hunting Notebook (admin outside hours, Office spawning shell, lateral movement, scheduled task, LSASS access)
- [ ] Tuesday: BTL1 SIEM scenarios timed — 4-hour budget, try to complete in 3h 45m
- [ ] Tuesday: Volatility3 advanced plugins — `windows.dlllist`, `windows.handles`, `windows.dumpfiles --pid [PID] -o dumped/`
- [ ] Tuesday: Write 2 Jira mock tickets from Volatility3 findings — tickets/vol-injection-jira.md, tickets/vol-persistence-jira.md
- [ ] Wednesday: BTL1 DFIR scenarios timed — 3-hour budget
- [ ] Wednesday: Build Python Jinja2 incident report generator: `pip install jinja2 splunk-sdk` → create templates/incident-report.html.j2 → scripts/incident-report-gen.py that reads Splunk REST API and generates HTML report
- [ ] Thursday: CyberDefenders CTF #2 — Intermediate difficulty — full writeup with ATT&CK + SPL + KQL + Jira ticket
- [ ] Thursday: Simulate Pass-the-Hash and write advanced multi-stage SPL correlation: `index=* EventCode=4625 | stats count by Account_Name,src | where count>=5 | join Account_Name [search index=* EventCode=4624]`
- [ ] Friday: BTL1 TI + Dark Web timed — combined under 90 min
- [ ] Friday: 10 applications this week — track every one in docs/application-tracker.md
- [ ] Saturday: BTL1 full practice run #2 — compare times to Week 4 run, record in docs/btl1-speed-log.md
- [ ] Saturday: Write LinkedIn post #2: "BTL1 preparation — what the 24-hour exam actually tests"
- [ ] Sunday: Review times, identify slowest domain, plan Week 6 drills

### Week 6 — BTL1 Intensive + Mock Interviews + SOAR

- [ ] Monday: BTL1 slowest domain intensive — 3 timed sessions back-to-back
- [ ] Monday: Write 5 STAR interview stories: docs/interview-star-stories.md (suspicious logon investigation, alert prioritisation, CrowdStrike knowledge, learning quickly, why blue team)
- [ ] Tuesday: Speak STAR stories aloud — record on phone → listen back → revise weak answers
- [ ] Tuesday: Write detection pipeline document: docs/detection-pipeline.md (ATT&CK → Sigma → CI/CD → Splunk alert → Jira ticket — full workflow with screenshots)
- [ ] Wednesday: 90-min mock technical assessment — CyberDefenders Medium challenge not seen before, no hints, timer running
- [ ] Wednesday: Python SOC toolkit v2 — refactor scripts/soc-toolkit.py with argparse CLI: `python3 soc-toolkit.py ip-triage 1.2.3.4` / `python3 soc-toolkit.py hash-lookup [hash]` / `python3 soc-toolkit.py email-parse email.eml`
- [ ] Thursday: CyberDefenders CTF #3 — Hard difficulty — full writeup
- [ ] Thursday: Research UK SOC salaries: glassdoor.co.uk + totaljobs.com → docs/salary-research.md (floor and target)
- [ ] Friday: BTL1 final full practice run — all 5 domains, real exam conditions
- [ ] Friday: Record 3-minute portfolio video walking through GitHub: Splunk dashboard → one detection rule → one Python script running → one CTF writeup → link from README
- [ ] Saturday: Full mock interview recorded (45 min): STAR stories + investigation walkthrough + CrowdStrike question + AI in SOC question
- [ ] Saturday: 15 applications this week — strongest tailored applications yet
- [ ] Sunday: Review mock interview recording, revise weak answers

### Week 7 — BTL1 Pre-Exam + SC-200 Begin

- [ ] Monday: BTL1 phishing speed target — 5 cases under 12 minutes each
- [ ] Monday: Start SC-200 Microsoft Learn path: learn.microsoft.com → SC-200 → complete Introduction to Sentinel and Connect Data to Sentinel modules
- [ ] Tuesday: BTL1 SIEM scenarios — 2 full scenarios under 3-hour budget each
- [ ] Tuesday: Write Python Splunk REST API integration: `pip install splunk-sdk` → scripts/splunk-api-query.py → `splunklib.client.connect` → `jobs.oneshot` → `ResultsReader`
- [ ] Wednesday: BTL1 DFIR + IR scenarios — both under 3-hour budget
- [ ] Wednesday: SC-200 module: Create and manage analytics rules (Scheduled vs NRT vs Anomaly types)
- [ ] Thursday: CyberDefenders CTF #4 — Hard difficulty
- [ ] Thursday: BloodHound remediation — identify one risky path → write PowerShell fix → commit ad-lab/bloodhound-remediation-01.md
- [ ] Friday: BTL1 exam day reference prep: create docs/btl1-exam-day-reference.md (Volatility3 plugin names, Splunk commands, AbuseIPDB/VirusTotal/URLScan/Shodan URLs, PICERL phases)
- [ ] Friday: Test all API keys: VT ✓ AbuseIPDB ✓ Shodan ✓
- [ ] Saturday: 10 more applications + direct outreach to 5 MSSP hiring managers via LinkedIn connection requests
- [ ] Sunday: Light review only — no new material, rest and prepare exam workspace

### Week 8 — BTL1 24-Hour Exam + SC-200 Sprint

- [ ] Monday: BTL1 exam day logistics — clear desk, two monitors if available, snacks, plan 15.5 hours active work within 24-hour window
- [ ] Monday–Tuesday: SIT BTL1 24-HOUR EXAM — time budget: Phishing 90min, TI 60min, SIEM 240min, IR 210min, DFIR 210min
- [ ] Post BTL1 result on LinkedIn immediately
- [ ] Update README.md cert table with BTL1 result
- [ ] Wednesday: SC-200 Defender XDR module — MDE + MDO + MDI correlation, automated investigation and response
- [ ] Wednesday: Write professional forensic report #2: reports/credential-attack-report-01.md (Kerberoasting + Pass-the-Hash campaign, full timeline, ATT&CK chain, IOC table)
- [ ] Thursday: CyberDefenders CTF #5 — Expert difficulty
- [ ] Thursday: Write all 10 SC-200 KQL queries from memory (no reference) — verify against sentinel-rules/
- [ ] Friday: SC-200 automation module — automation rules (in-Sentinel, simple, fast) vs playbooks (Logic Apps, external API, complex)
- [ ] Friday: 15 applications this week — pipeline should be generating interview invitations now
- [ ] Saturday: Full mock interview #2 recorded — incorporate feedback from first recording
- [ ] Sunday: Review interview recording, write docs/month-2-retrospective.md

---

## MONTH 3 — SC-200 Exam + Capstone Project + Signed Offer
> Target: SC-200 passed Week 2 · Capstone project published · Signed offer by end of month

### Week 9 — SC-200 Exam Prep + Job Hunt Peak

- [ ] Monday: SC-200 final revision — write all 10 KQL queries from memory in 15 minutes
- [ ] Monday: Book SC-200 exam: microsoft.com/en-us/learning/exam-sc-200 → Online Proctored → this week → ~£125
- [ ] Tuesday: Company-specific interview prep for all scheduled interviews — read JD, company blog, Glassdoor, LinkedIn team
- [ ] Tuesday: Write UK sector threat intel report: reports/uk-sector-threat-intel-2026.md (current threats to your target employer sector)
- [ ] Wednesday: SC-200 final revision — automation rules vs playbooks distinction written in own words
- [ ] Wednesday: Full mock interview #3 — 45 minutes, recorded
- [ ] Thursday: CyberDefenders CTF #6
- [ ] Thursday: Start capstone project: docs/capstone-attack-detection.md — plan 6-stage attack chain
- [ ] Friday: 15 applications this week — personalised cover paragraph for each
- [ ] Saturday: SC-200 exam prep — complete any remaining Microsoft Learn modules
- [ ] Sunday: Light review, apply to 3 more

### Week 10 — SC-200 Exam + Capstone Project

- [ ] Monday: SC-200 KQL final confidence check — all 10 queries from memory
- [ ] Tuesday: SIT SC-200 EXAM — 40-60 questions, 120 minutes, 700/1000 to pass
- [ ] Post SC-200 result on LinkedIn immediately
- [ ] Update README.md cert table with SC-200 result
- [ ] Wednesday: AWS GuardDuty: aws.amazon.com → free account → search GuardDuty → Enable → Settings → Generate sample findings → investigate one finding
- [ ] Wednesday: Capstone Stage 1 — phishing initial access: document EventID, SPL, KQL, ATT&CK T1566.002
- [ ] Thursday: Capstone Stages 2-3 — PowerShell execution (T1059.001) + C2 beacon (T1071.001)
- [ ] Friday: Capstone Stages 4-6 — Kerberoasting (T1558.003) + lateral movement (T1550.002) + exfiltration (T1048)
- [ ] Friday: Publish capstone: docs/capstone-attack-detection.md — full 6-stage chain with ATT&CK for every stage, SPL + KQL, forensic artefacts, IOC table, recommendations
- [ ] Saturday: 15 applications + post capstone on LinkedIn with detailed breakdown
- [ ] Sunday: Update README linking capstone prominently

### Week 11 — Interview Execution + Offer Pipeline

- [ ] Monday: Attend scheduled interviews — execute STAR stories + investigation walkthrough + CrowdStrike question
- [ ] Monday: Send thank-you emails within 24 hours of each interview
- [ ] Tuesday: Build Python SOAR end-to-end pipeline: scripts/soar-pipeline.py — `run_pipeline(alert_ip, alert_type)` → enrich VT + AbuseIPDB + Shodan → score risk → generate HTML → generate Jira ticket
- [ ] Wednesday: Build Sentinel Hunting Notebook: Sentinel → Hunting → New query for each of your 10 KQL queries, add ATT&CK tactic and entity mapping to each
- [ ] Wednesday: Screenshot hunting notebook → commit sentinel-rules/hunting-notebook-10-queries.md
- [ ] Thursday: CyberDefenders CTF #7 — final CTF of the programme, best writeup yet
- [ ] Thursday: Evaluate any offers received against salary research (floor and target)
- [ ] Friday: Negotiate offers using prepared script: "Based on my research and the three certifications I am bringing — Security+, BTL1, and SC-200 — I was hoping we could discuss £[target]"
- [ ] Friday: 15 applications — keep pipeline wide even if interviews are active
- [ ] Saturday: Final portfolio audit — docs/graduate-readiness-checklist.md — all items checked
- [ ] Sunday: Apply to 5 more — do not stop until signed contract

### Week 12 — Signed Offer + Programme Close

- [ ] Monday: CV final version: Security+, BTL1, SC-200 in certifications. Skills: Splunk SPL, Sentinel KQL, Python, PowerShell, Sigma CI/CD, MITRE ATT&CK, 8 Windows Event IDs, CrowdStrike Falcon
- [ ] Tuesday: Direct outreach to 10 hiring managers if no offer yet — LinkedIn connection request with GitHub link and portfolio video
- [ ] Wednesday: Write docs/year-1-cert-plan.md — BTL2 vs GCIA vs CrowdStrike CCFR vs CySA+, employer training budget business case
- [ ] Thursday: If signed: research new employer sector threats, team structure, tools used — docs/first-role-prep.md
- [ ] Friday: Write docs/3-month-retrospective.md — what completed, what was hardest, what surprised you, 1-year plan
- [ ] Saturday: Write final LinkedIn post: "3 months, 3 certs, one home SOC lab"
- [ ] Saturday: Update README — all 3 certs, capstone linked, portfolio video linked
- [ ] Sunday: SIGNED OFFER RECEIVED AND ACCEPTED — update all platforms

---

## Portfolio Checklist (verify before every application)

- [ ] README.md: skills section, cert table, GitHub URL, portfolio video link
- [ ] detection-rules/: 15+ rules, all with ATT&CK ID + SPL + KQL + FP notes + response actions
- [ ] sigma-rules/: 5+ rules, CI/CD converting automatically on every push
- [ ] scripts/: Python + PowerShell both, README with usage examples
- [ ] tickets/: 10+ mock tickets in both Jira and ServiceNow format
- [ ] writeups/: 7+ CTF writeups with ATT&CK + SPL + KQL + mock ticket each
- [ ] reports/: 2 forensic reports + 1 threat intel report
- [ ] docs/: capstone project, interview STAR stories, salary research, employer research, BTL1 exam strategy
- [ ] Commit activity: green squares every week in GitHub activity graph
