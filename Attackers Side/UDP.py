from scapy.all import IP, UDP, send
import time

dest_ip = "172.20.10.6"
duration = 60  # Duration of sending packets in seconds

start_time = time.time()
while time.time() - start_time < duration:
    udp_packet = IP(dst=dest_ip) / UDP()
    send(udp_packet, verbose=True)