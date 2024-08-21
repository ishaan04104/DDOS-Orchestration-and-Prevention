from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp
import time

start_time = time.time()
while time.time() - start_time < 60:
    dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(chaddr="01\x02\x03\x04\x05", xid=12345) / DHCP(options=[("message-type", "discover")])
    sendp(dhcp_discover, verbose=True)