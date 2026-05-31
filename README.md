# Passive Reconnaissance & OSINT Automation Tool

A lightweight Python script designed for the initial information gathering phase (Reconnaissance) during an authorized Red Teaming engagement or OSINT investigation.

## Features
- **DNS Enumeration:** Automatically fetches A, MX, TXT, and NS records for a given target domain using the `dnspython` library.
- **Social Media OSINT:** Scans popular platforms (GitHub, X, Instagram) to identify potential brand profiles or naming patterns matching the target.
- **Passive & Legal:** The tool only utilizes public DNS servers and standard HTTP requests, ensuring 100% passive data collection without interacting with the target's direct infrastructure.

## Requirements
- Python 3.x
- `dnspython` library
- `requests` library

## Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com
cd passive-recon-tool
pip install -r requirements.txt
```

## Usage
Run the script from the command line by passing the target domain as an argument:
```bash
python recon_tool.py example.com
```

## Disclaimer
This tool is strictly for educational, OSINT research, and authorized security auditing purposes only. 
