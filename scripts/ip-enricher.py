#!/usr/bin/env python3
"""
IP Enricher — queries VirusTotal, AbuseIPDB, and Shodan for an IP address
and outputs a formatted triage report.

Usage: python3 ip-enricher.py 1.2.3.4
"""

import requests
import os
import sys
import json
from datetime import datetime

VT_KEY = os.environ.get("VT_KEY", "")
ABUSE_KEY = os.environ.get("ABUSE_KEY", "")
SHODAN_KEY = os.environ.get("SHODAN_KEY", "")


def check_virustotal(ip: str) -> dict:
    """Query VirusTotal for IP reputation."""
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VT_KEY}
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code == 200:
        stats = r.json()["data"]["attributes"]["last_analysis_stats"]
        return {
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "clean": stats.get("undetected", 0),
        }
    return {"error": f"HTTP {r.status_code}"}


def check_abuseipdb(ip: str) -> dict:
    """Query AbuseIPDB for IP abuse confidence score."""
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    headers = {"Key": ABUSE_KEY, "Accept": "application/json"}
    r = requests.get(url, params=params, headers=headers, timeout=10)
    if r.status_code == 200:
        data = r.json()["data"]
        return {
            "abuse_score": data.get("abuseConfidenceScore", 0),
            "total_reports": data.get("totalReports", 0),
            "country": data.get("countryCode", "Unknown"),
            "isp": data.get("isp", "Unknown"),
        }
    return {"error": f"HTTP {r.status_code}"}


def check_shodan(ip: str) -> dict:
    """Query Shodan for open ports and organisation info."""
    try:
        import shodan
        api = shodan.Shodan(SHODAN_KEY)
        info = api.host(ip)
        return {
            "org": info.get("org", "Unknown"),
            "ports": [str(s["port"]) for s in info.get("data", [])],
            "hostnames": info.get("hostnames", []),
        }
    except Exception as e:
        return {"error": str(e)}


def calculate_verdict(vt: dict, abuse: dict) -> str:
    """Determine verdict based on enrichment results."""
    vt_mal = vt.get("malicious", 0)
    abuse_score = abuse.get("abuse_score", 0)
    if vt_mal > 3 or abuse_score > 50:
        return "MALICIOUS"
    elif vt_mal > 0 or abuse_score > 10:
        return "SUSPICIOUS — INVESTIGATE"
    else:
        return "CLEAN"


def generate_html_report(ip: str, vt: dict, abuse: dict, shodan: dict) -> str:
    """Generate a formatted HTML triage report."""
    verdict = calculate_verdict(vt, abuse)
    colour = {"MALICIOUS": "#ef4444", "SUSPICIOUS — INVESTIGATE": "#f97316", "CLEAN": "#22c55e"}
    return f"""<!DOCTYPE html>
<html><head><title>IP Triage: {ip}</title>
<style>body{{font-family:Arial;max-width:800px;margin:40px auto;padding:20px}}
h1{{color:#1e293b}}table{{width:100%;border-collapse:collapse;margin:20px 0}}
th,td{{border:1px solid #e2e8f0;padding:10px;text-align:left}}th{{background:#f8fafc}}
.verdict{{font-size:1.4em;font-weight:bold;color:{colour.get(verdict,"#64748b")};padding:10px;border:2px solid currentColor;display:inline-block;margin:10px 0}}</style>
</head><body>
<h1>IP Triage Report: {ip}</h1>
<p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}</p>
<div class="verdict">{verdict}</div>
<h2>VirusTotal</h2>
<table><tr><th>Malicious</th><th>Suspicious</th><th>Clean</th></tr>
<tr><td>{vt.get("malicious","N/A")}</td><td>{vt.get("suspicious","N/A")}</td><td>{vt.get("clean","N/A")}</td></tr></table>
<h2>AbuseIPDB</h2>
<table><tr><th>Abuse Score</th><th>Total Reports</th><th>Country</th><th>ISP</th></tr>
<tr><td>{abuse.get("abuse_score","N/A")}/100</td><td>{abuse.get("total_reports","N/A")}</td>
<td>{abuse.get("country","N/A")}</td><td>{abuse.get("isp","N/A")}</td></tr></table>
<h2>Shodan</h2>
<table><tr><th>Organisation</th><th>Open Ports</th><th>Hostnames</th></tr>
<tr><td>{shodan.get("org","N/A")}</td><td>{", ".join(shodan.get("ports",[]) or ["None"])}</td>
<td>{", ".join(shodan.get("hostnames",[]) or ["None"])}</td></tr></table>
</body></html>"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ip-enricher.py <ip_address>")
        sys.exit(1)
    ip = sys.argv[1]
    print(f"Enriching {ip}...")
    vt = check_virustotal(ip)
    abuse = check_abuseipdb(ip)
    shodan_info = check_shodan(ip)
    verdict = calculate_verdict(vt, abuse)
    print(f"\nVerdict: {verdict}")
    print(f"VT Malicious: {vt.get('malicious', 'N/A')}")
    print(f"AbuseIPDB Score: {abuse.get('abuse_score', 'N/A')}/100")
    print(f"Shodan Org: {shodan_info.get('org', 'N/A')}")
    html = generate_html_report(ip, vt, abuse, shodan_info)
    filename = f"{ip.replace('.', '-')}-triage.html"
    with open(filename, "w") as f:
        f.write(html)
    print(f"HTML report saved to {filename}")
