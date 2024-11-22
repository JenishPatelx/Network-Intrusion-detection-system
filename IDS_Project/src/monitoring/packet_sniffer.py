import logging
from scapy.all import sniff

class PacketSniffer:
    """Simulates network packet sniffing and traffic monitoring."""
    
    def __init__(self):
        # List to store sniffed data (simulated network traffic)
        self.sniffed_data = []
    
    def sniff_traffic(self, interface, count):
        """Simulate packet sniffing and log the captured traffic."""
        # This method uses Scapy to sniff network traffic
        def packet_handler(packet):
            # Check if the packet has an IP layer and extract source/destination IPs
            if packet.haslayer('IP'):
                sniffed_packet = {
                    "source_ip": packet['IP'].src,  # Correct field for source IP
                    "destination_ip": packet['IP'].dst,  # Destination IP
                    "protocol": packet['IP'].proto  # Protocol type
                }
                self.sniffed_data.append(sniffed_packet)
                logging.info(f"Sniffed traffic: {sniffed_packet}")
        
        # Sniff packets using the specified interface and count
        sniff(iface=interface, count=count, prn=packet_handler)
        return self.sniffed_data
