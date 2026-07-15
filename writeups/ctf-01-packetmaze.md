# CTF #01 — CyberDefenders PacketMaze

**Platform:** CyberDefenders
**Difficulty:** Easy
**Date:** Jun 2026
**Category:** Network Forensics (PCAP analysis)

---

## Overview

A PCAP capture containing suspicious network traffic. The investigation revealed
[describe what you found — C2 communication / data exfiltration / credential theft etc].

---

## Tools Used

- Wireshark — protocol analysis and stream following
- Python (scapy) — packet-level inspection
- VirusTotal — IP and domain reputation

---

## Methodology

1. Opened PCAP in Wireshark → Statistics → Protocol Hierarchy to understand traffic composition
2. Applied display filter `dns` to identify all domain lookups — noted unusual domains
3. Applied `http` filter to find unencrypted web traffic
4. Identified suspicious connection → right-click → Follow → TCP Stream
5. Analysed content of the stream

---

## Findings

| Finding | Evidence | ATT&CK Technique |
|---------|----------|-----------------|
| [Finding 1] | Packet #XXX — [description] | TXXXX — [name] |
| [Finding 2] | [log excerpt] | TXXXX — [name] |

---

## MITRE ATT&CK Mapping

- **TXXXX — [Technique Name]:** [1-2 sentences explaining how the evidence maps to this technique]

---

## Detection: Splunk SPL

```spl
index=* [relevant search based on what you found]
| table _time, src_ip, dest_ip, [other relevant fields]
| eval attck="TXXXX"
```

---

## Detection: Microsoft Sentinel KQL

```kql
[TableName]
| where [relevant filter]
| project TimeGenerated, [relevant fields]
| extend ATT_CK = "TXXXX — [Technique Name]"
```

---

## Mock Incident Ticket (Jira Format)

**Summary:** [HIGH/MEDIUM] [Attack Type] Detected — [Brief Description]
**Priority:** High
**ATT&CK Technique:** TXXXX — [Name]
**Evidence:** [One log excerpt or packet description]
**Immediate Actions:**
1. [First action]
2. [Second action]
**Escalation Decision:** [Tier 1 close / Escalate to Tier 2] — because [reason]

---

## Lessons Learned

[One paragraph: what this CTF taught you that you did not know before, or confirmed about detection]
