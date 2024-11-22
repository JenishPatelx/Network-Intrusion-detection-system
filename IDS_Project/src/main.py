import pandas as pd
from data_processing.data_cleaner import DataCleaner
from data_processing.feature_extractor import FeatureExtractor
from detection.hybrid_model import HybridDetector
from loging.event_logger import EventLogger
from monitoring.packet_sniffer import PacketSniffer

def main():
    # Initialize components
    sniffer = PacketSniffer()
    
    # Capture packets
    packets = sniffer.sniff_traffic(interface="eth0", count=5)
    print("Captured packets:", packets)

    # Convert packets to a DataFrame for cleaning and processing
    packets_df = pd.DataFrame(packets)

    # Initialize DataCleaner with the captured data
    cleaner = DataCleaner(packets_df)

    # Clean data
    cleaned_packets = cleaner.remove_duplicates()  # No need to pass 'packets_df' now
    print("Cleaned packets:", cleaned_packets)

    # Initialize other components
    extractor = FeatureExtractor(df=cleaned_packets)
    detector = HybridDetector()
    logger = EventLogger("logs/alerts.log")

    # Run detection (assuming features are processed)
    alerts = detector.detect(data=cleaned_packets)  # Example
    logger.log_event(f"Alerts: {alerts}")

if __name__ == "__main__":
    main()
