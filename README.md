Recon Tool
Show Image
Show Image

A Python-based network reconnaissance tool designed to automate the subdomain enumeration and port scanning phases of penetration testing.

⚠️ Disclaimer
This tool is intended for authorized security testing only. Unauthorized port scanning and reconnaissance may be illegal in your jurisdiction. Always obtain proper authorization before scanning networks or systems you do not own.

🎯 Current Features
-Subdomain Enumeration: Discovers subdomains using Sublist3r
-Port Scanning: Automated nmap scanning of discovered subdomains
-Service Detection: Identifies running services and their versions
-Formatted Output: Clean, tabulated results for easy analysis
-Error Handling: Graceful handling of interruptions and errors
🚧 Project Status
✅ Working Features
 -Subdomain discovery
 -Multi-subdomain port scanning
 -Service version detection
 -Terminal-based output with tabulate
 -Keyboard interrupt handling
📋 Planned Features
- TBA
📦 Installation
Prerequisites
Python 3.6 or higher
nmap installed on your system
Root/Administrator privileges (required for certain nmap scans)
System Dependencies
Linux (Debian/Ubuntu):

bash
sudo apt-get update
sudo apt-get install nmap
macOS:

bash
brew install nmap
Windows: Download and install from nmap.org

Python Dependencies
bash
# Clone the repository
git clone https://github.com/yourusername/recon-tool.git
cd recon-tool

# Install required packages
pip install -r requirements.txt
🚀 Usage
Basic Usage
bash
python recon.py
When prompted, enter the target domain:

Enter target domain (e.g., example.com): example.com
Example Output
[*] Starting Reconnaissance on: example.com
[+] Enumerating Sub-Domains...
[+] Scanning mail.example.com...
[+] Scanning www.example.com...

[+] Reconnaissance Report
============================================================
╒═══════════════════╤════════╤═══════════╤═══════════╤═══════════╕
│ Subdomain         │   Port │ Service   │ Product   │ Version   │
╞═══════════════════╪════════╪═══════════╪═══════════╪═══════════╡
│ mail.example.com  │     80 │ http      │ nginx     │ 1.18.0    │
├───────────────────┼────────┼───────────┼───────────┼───────────┤
│ mail.example.com  │    443 │ https     │ nginx     │ 1.18.0    │
╘═══════════════════╧════════╧═══════════╧═══════════╧═══════════╛

[!] Recon Complete.
🛠️ Technical Details
Scan Process
Subdomain Enumeration: Uses Sublist3r to query multiple search engines and DNS databases
Port Scanning: Performs nmap service version detection (-sV) with aggressive timing (-T4)
Data Collection: Stores port, service name, product, and version information
Report Generation: Displays results in a formatted table
Default Scan Parameters
Nmap Arguments: -sV -T4
-sV: Service version detection
-T4: Aggressive timing template (faster scans)
🤝 Contributing
This project is in active development. Contributions, bug reports, and feature requests are welcome!

Reporting Issues
Please include:

Your operating system and Python version
Complete error messages
Steps to reproduce the issue
📄 License
[Choose your license - MIT recommended for open source]

🔮 Future Roadmap
Short-term (v0.2)
Export results to JSON/CSV/HTML
Custom port range selection
Configuration file support
Long-term (v1.0+)
Integration with vulnerability scanners
Automated finding documentation tool
Web-based interface
API for integration with other tools
📚 Related Projects
This tool is part of a planned suite of penetration testing utilities:

Recon Tool (current) - Network reconnaissance
Finding Documentation Tool (planned) - Automated pentest report generation
⚠️ Known Limitations
Requires root/sudo for some nmap scan types
Scan speed depends on network conditions and target responsiveness
Sublist3r may miss subdomains not indexed in public databases
No current support for authenticated scans
👤 Author
[M Srinivasa Aditya]

🙏 Acknowledgments
Sublist3r by Ahmed Aboul-Ela
python-nmap
tabulate
Remember: Always obtain proper authorization before performing security assessments.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
