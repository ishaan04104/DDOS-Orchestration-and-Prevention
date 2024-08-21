from scapy.all import IP, UDP, DNS, DNSQR, send
import time

dns_server_ip = "172.20.10.6"  # IP address of a DNS server
domain_name = "google.com"  # Domain name to query

# Construct DNS query packet
dns_query = IP(dst=dns_server_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname=domain_name))

# Send DNS query packet for 60 seconds
start_time = time.time()
while time.time() - start_time < 60:
    send(dns_query, verbose=True)
