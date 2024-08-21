from scapy.all import sniff, IP

def packet_filter(packet):
    if IP in packet and packet[IP].src == "172.20.10.2":
        print("Dropping packet from source IP:", packet.summary())
        return None
    return None

sniff(filter="", prn=packet_filter)