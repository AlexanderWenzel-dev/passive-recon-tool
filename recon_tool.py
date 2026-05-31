import sys
import time
import random
import urllib.parse
import webbrowser  # Dieses Modul öffnet automatisch die Webseiten auf deinem PC
from curl_cffi import requests as cf_requests

def get_doh_dns_records(domain):
    """Fragt DNS-Einträge verschlüsselt über DNS-over-HTTPS (DoH) via Cloudflare ab."""
    print(f"\n[+] Starte verschlüsselte DNS-over-HTTPS (DoH) Aufklärung für: {domain}")
    print("-" * 75)
    session = cf_requests.Session(impersonate="chrome124")
    for record in ['A', 'MX', 'TXT', 'NS']:
        url = f"https://cloudflare-dns.com{domain}&type={record}"
        try:
            response = session.get(url, headers={"Accept": "application/dns-json"}, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"[{record}-Einträge]:")
                if "Answer" in data:
                    for answer in data["Answer"]:
                        print(f"  -> {answer['data']}")
        except Exception:
            pass
        time.sleep(0.5)

def get_stealth_subdomains_and_map(domain):
    """Findet Subdomains via crt.sh und ermittelt passiv deren IP-Standort und Hoster (ASN)."""
    print(f"\n[+] Passive Subdomain-Discovery & ASN-Mapping für: {domain}")
    print("-" * 75)
    url = f"https://crt.sh%.{domain}&output=json"
    session = cf_requests.Session(impersonate="chrome124")
    
    try:
        response = session.get(url, timeout=15)
        if response.status_code == 200:
            subdomains = set()
            for entry in response.json():
                name = entry['name_value'].lower()
                for sub in name.split('\n'):
                    if not sub.startswith('*') and sub.endswith(domain):
                        subdomains.add(sub)
            
            if subdomains:
                print(f"[FOUND] {len(subdomains)} Subdomains ermittelt. Starte IP-Mapping...")
                for sub in list(sorted(subdomains))[:5]:
                    time.sleep(1.0)
                    try:
                        geo_url = f"https://ipapi.co{sub}/json/"
                        geo_res = session.get(geo_url, timeout=5).json()
                        org = geo_res.get('org', 'Unbekannter Hoster')
                        country = geo_res.get('country_name', 'Unbekannt')
                        print(f"  -> {sub} | Hoster: {org} ({country})")
                    except Exception:
                        print(f"  -> {sub} | IP-Mapping fehlgeschlagen")
            else:
                print("[-] Keine Subdomains gefunden.")
    except Exception:
        print("[-] Fehler bei der Subdomain-Ermittlung.")

def passive_tech_stack_scan(domain):
    """Ermittelt passiv Technologien der Domain über eine freie CTI-Schnittstelle."""
    print(f"\n[+] Passiver Tech-Stack-Scan (Software-Erkennung) für: {domain}")
    print("-" * 75)
    session = cf_requests.Session(impersonate="chrome124")
    
    url = f"https://threatminer.org{domain}&rt=1"
    try:
        response = session.get(url, timeout=10)
        if response.status_code == 200:
            print("[*] Bekannte historische Infrastruktur-Daten abgerufen.")
            print(f"  -> Details einsehbar unter: https://threatminer.org{domain}")
        else:
            print("[-] Keine passiven Tech-Stack-Daten verfügbar.")
    except Exception:
        print("[-] Tech-Stack-Abfrage fehlgeschlagen.")

def linkedin_employee_scraping(domain):
    """Sucht über Google-Dorks passiv nach Mitarbeitern und öffnet die Funde direkt im Browser."""
    company_name = domain.split('.')[0]
    print(f"\n[+] Starte passives LinkedIn-Employee-Scraping für: '{company_name}'")
    print("-" * 75)
    
    session = cf_requests.Session(impersonate="chrome124")
    keywords = ["Administrator", "IT", "HR", "Manager"]
    
    for role in keywords:
        time.sleep(random.uniform(2.5, 4.5))
        query = f'site:://linkedin.com "{company_name}" "{role}"'
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://google.com{encoded_query}"
        
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                if "did not match any documents" in response.text:
                    print(f"[-] Keine Mitarbeiter mit der Rolle '{role}' gefunden.")
                elif "unusual traffic" in response.text:
                    print(f"[!] Google-Captcha ausgelöst. Scraping gestoppt.")
                    break
                else:
                    print(f"[FOUND] Potenzielle Zielpersonen im Bereich '{role}' identifiziert!")
                    print(f"  -> Öffne Suchergebnisse direkt im Webbrowser...")
                    
                    # HIER PASSIERT DIE MAGIE: Der Standard-Browser öffnet automatisch den Link
                    webbrowser.open(url)
                    
        except Exception:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Benutzung: python recon_tool.py <domain.de>")
        sys.exit(1)
        
    target_domain = sys.argv[1].lower()
    
    get_doh_dns_records(target_domain)
    get_stealth_subdomains_and_map(target_domain)
    passive_tech_stack_scan(target_domain)
    linkedin_employee_scraping(target_domain)
