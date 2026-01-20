import nmap
import sublist3r
from tabulate import tabulate
import json

def run_recon(domain):
    print(f"[*] Starting Reconnaissance on: {domain}")

    #Stage1: Sub-Domain Enumeration
    #This finds hidden entry points in a domain like all the subdomains under the domain
    print("[+] Enumerating Sub-Domains...")
    subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)

    if not subdomains:
        print("[!] No subdomains found or an error occurred.")
        subdomains = []

    recon_results = {}

    #Stage2: Port Scanning & Service Detection
    nm = nmap.PortScanner()
    
    try:
        for sub in subdomains:
            print(f"[+] Scanning {sub}...")
            # -sV: service version detection | -T4: Faster execution
            nm.scan(sub, arguments="-sV -T4")
    
            if sub in nm.all_hosts():
                recon_results[sub] = []
                for proto in nm[sub].all_protocols():
                    ports = nm[sub][proto].keys()
                    for port in ports:
                        service = nm[sub][proto][port]
                        recon_results[sub].append({
                            "port": port,
                            "name": service['name'],
                            "product": service['product'],
                            "version": service['version']
                            })
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Saving partial results...")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}. Printing partial results...")

    #Stage3: Print Findings to Terminal
    print("\n[+] Reconnaissance Report")
    print("=" * 60)
    
    table_data = []
    if recon_results:
        for sub, services in recon_results.items():
            if not services:
                table_data.append([sub, "N/A", "No Open Ports found", "N/A", "N/A"])
                continue
            for service in services:
                table_data.append([
                    sub,
                    service['port'],
                    service['name'],
                    service['product'],
                    service['version']
                ])
        
        headers = ["Subdomain", "Port", "Service", "Product", "Version"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("No results found.")
    
    print("\n[!] Recon Complete.")

if __name__ == "__main__":
    target = input("Enter target domain (e.g., example.com): ")
    run_recon(target)