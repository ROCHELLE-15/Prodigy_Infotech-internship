!pip install scapy tqdm

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from tqdm import tqdm

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"TCP: {tcp_layer.sport} -> {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"UDP: {udp_layer.sport} -> {udp_layer.dport}")
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"ICMP: {icmp_layer.type} -> {icmp_layer.code}")
        if Raw in packet:
            print(f"Payload: {packet[Raw].load}")
        print("\n")

# Sniff packets
print("Starting packet capture. Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
