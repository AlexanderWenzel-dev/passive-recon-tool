import dns.resolver
import requests
import sys

def get_dns_records(domain):
    """Fragt die wichtigsten DNS-Einträge einer Domain ab."""
    record_types = ['A', 'MX', 'TXT', 'NS']
    print(f"\n[+] Starte DNS-Aufklärung für: {domain}")
    print("-" * 50)
    
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"[{record}-Einträge]:")
            for rdata in answers:
                print(f"  -> {rdata}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"[{record}-Einträge]: Keine Funde oder Domain existiert nicht.")
        except Exception as e:
            print(f"[-] Fehler bei {record}-Abfrage: {e}")

def check_social_media(domain_prefix):
    """Prüft gängige Social-Media-Plattformen auf den Namen der Domain."""
    platforms = {
        "GitHub": f"https://github.com{domain_prefix}",
        "Twitter/X": f"https://x.com{domain_prefix}",
        "Instagram": f"https://instagram.com{domain_prefix}"
    }
    
    print(f"\n[+] Starte Social-Media-Enumeration für Username: '{domain_prefix}'")
    print("-" * 50)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"[FOUND] {platform}: {url}")
            elif response.status_code == 404:
                print(f"[NOT FOUND] {platform}")
            else:
                print(f"[?] {platform}: Status Code {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"[-] {platform}: Verbindung fehlgeschlagen.")

if _name_ == "_main_":
    if len(sys.argv) < 2:
        print("Benutzung: python recon_tool.py <domain.de>")
        sys.exit(1)
        
    target_domain = sys.argv[1]
    # Extrahiert den Namen vor dem Punkt für die Social-Media-Suche (z.B. "google" aus "google.com")
    name_prefix = target_domain.split('.')[0]
    
    get_dns_records(target_domain)
    check_social_media(name_prefix)