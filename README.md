# 🛡️ Advanced Passive Reconnaissance & CTI Framework

An advanced, lightweight Python 3 security framework engineered for the initial information-gathering phase (Reconnaissance) during authorized Red Teaming engagements and Cyber Threat Intelligence (CTI) workflows.

This framework is built from the ground up with a strict focus on **Operational Security (OPSEC)**. It leverages advanced anti-bot evasion techniques to gather intelligence entirely out-of-band, ensuring zero direct interaction with the target network infrastructure.

---

## Key Features & Architectural Overview

### 1. DNS-over-HTTPS (DoH) Core
Standard DNS queries reveal intent to local network monitors and upstream Internet Service Providers (ISPs). This framework encapsulates all DNS requests inside encrypted HTTPS tunnels routed directly to Cloudflare's secure Anycast DNS (`1.1.1.1`). 
* **OPSEC Benefit:** Eliminates DNS leaking, local logging, and network-level eavesdropping.

### 2. JA3/JA4 TLS Fingerprint Impersonation
Modern Web Application Firewalls (WAFs) like Cloudflare, Akamai, and DataDome block standard automation scripts by analyzing the TLS handshake. This tool replaces the default Python networking stack with `curl_cffi`.
* **OPSEC Benefit:** Spoofs the cryptographic signature (JA3/JA4 fingerprints), TLS frames, and HTTP/2 settings to perfectly mimic a legitimate **Google Chrome (v124)** browser session.

### 3. Out-of-Band Subdomain Harvesting & ASN Mapping
Instead of actively brute-forcing subdomains via brute-force pinging, the tool extracts historical data from public Certificate Transparency (CT) logs via `crt.sh`. Discovered domains are dynamically cross-referenced against public routing tables.
* **CTI Benefit:** Automatically maps out the target's cloud perimeter (e.g., AWS, Azure, DigitalOcean) and Autonomous System Numbers (ASN) without sending a single packet to the victim.

### 4. Automated OSINT Intelligence & Identity Mapping
Pre-configured, time-delayed search engine dorks systematically comb through indexed data to find exposed employees on professional platforms.
* **Red Team Benefit:** Maps out high-value targets (System Administrators, HR, IT-Staff, Management) on LinkedIn to prepare for simulated social engineering or spear-phishing campaigns.

### 5. Native OS Browser Injection
Includes a practical automation hook that seamlessly triggers the host operating system's default web browser to launch verified intelligence links. This allows the operator to instantly review data leaks during critical operational windows.

---

## Terminal Execution Example

When executed against a target domain, the framework provides a structured, actionable output:

```text
\$ python recon_tool.py target-company.com

[+] Starte verschlüsselte DNS-over-HTTPS (DoH) Aufklärung für: target-company.com
---------------------------------------------------------------------------
[A-Einträge]:
  -> 93.184.216.34
[MX-Einträge]:
  -> 10 ://target-company.com
[TXT-Einträge]:
  -> v=spf1 include:_://google.com ~all

[+] Passive Subdomain-Discovery & ASN-Mapping für: target-company.com
---------------------------------------------------------------------------
[FOUND] 3 Subdomains ermittelt. Starte IP-Mapping...
  -> ://target-company.com | Hoster: Amazon.com, Inc. (United States)
  -> ://target-company.com   | Hoster: Microsoft Corporation (Ireland)
  -> ://target-company.com   | Hoster: Cloudflare, Inc. (United States)

[+] Passiver Tech-Stack-Scan (Software-Erkennung) für: target-company.com
---------------------------------------------------------------------------
[*] Bekannte historische Infrastruktur-Daten abgerufen.
  -> Details einsehbar unter: https://threatminer.org

[+] Starte passives LinkedIn-Employee-Scraping für: 'target-company'
---------------------------------------------------------------------------
[FOUND] Potenzielle Zielpersonen im Bereich 'Administrator' identifiziert!
  -> Öffne Suchergebnisse direkt im Webbrowser...

[*] Scan erfolgreich abgeschlossen. Alle Abfragen wurden zu 100% passiv durchgeführt.
```

---

##  Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd passive-recon-tool
   ```

2. **Install High-Stealth Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Execute the framework from your terminal by passing the target root domain as an argument:

```bash
python recon_tool.py target-company.com
```

---

## Core Code Layout
* `get_doh_dns_records()`: Handles encrypted cloud-dns queries via JSON APIs.
* `get_stealth_subdomains_and_map()`: Parses certificate logs and correlates Geo-IP/ASN metrics.
* `passive_tech_stack_scan()`: Queries passive CTI intelligence feeds.
* `linkedin_employee_scraping()`: Controls dork automation and triggers native OS `webbrowser` tabs.

---

## Legal & Ethical Disclaimer
This framework is strictly developed for educational purposes, OSINT research, and authorized security auditing under formal engagement rules. The author assumes no liability for any unauthorized use, malicious activities, or damages caused by this program.
