import os
import logging
import sys


sys.path.append(os.path.abspath('./src'))



from data_processing.data_cleaner import DataCleaner
from data_processing.feature_extractor import FeatureExtractor
from detection.signature_based import SignatureBasedDetector
from src.logging.event_logger import EventLogger
from monitoring.packet_sniffer import PacketSniffer





def ensure_logs_directory_exists():
    """Ensure that the logs directory exists, create it if not."""
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

def test_full_integration():
    """
    Full integration test for the IDS:
    1. Processes data
    2. Detects intrusion
    3. Logs events
    4. Monitors system/network activity
    """
    
    # Set up logging to capture the sniffed traffic
    logging.basicConfig(level=logging.INFO)
    
    # 1. Ensure the logs directory exists
    ensure_logs_directory_exists()
    
    # 2. Simulate incoming raw data (raw network traffic or logs)
    raw_data = [{'source_ip': '192.168.1.1', 'destination_ip': '10.0.0.2', 'protocol': 'TCP'}]
    
    # 3. Process the raw data (clean and extract features)
    cleaner = DataCleaner(raw_data)
    cleaned_data = cleaner.clean_data()
    
    feature_extractor = FeatureExtractor(cleaned_data)
    features = feature_extractor.extract_features()
    
    # 4. Detect any intrusions using a detection method (Signature-based in this case)
    detector = SignatureBasedDetector()
    detection_results = detector.detect_intrusion(features)
    
    # 5. Log the detection results
    log_file = "logs/test_integration.log"
    logger = EventLogger(log_file)
    for result in detection_results:
        logger.log_event(result)
    
    # 6. Simulate packet sniffing and monitor the network
    sniffer = PacketSniffer()
    sniffed_traffic = sniffer.sniff_traffic()  # Simulate sniffing traffic
    
    # Optionally, assert that sniffed traffic exists
    assert len(sniffed_traffic) > 0, "No traffic sniffed"
    print("Sniffed Traffic:", sniffed_traffic)
    
    # 7. Assert that log entries have been created
    assert os.path.exists(log_file), f"Log file {log_file} was not created"
    
    # Check if the log file has content (i.e., an event has been logged)
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert len(log_content) > 0, f"Log file {log_file} is empty"
    
    # 8. Assert on the content of the log file
    # Adjusted to match the actual log content
    assert "Intrusion detected at index 0" in log_content, "Intrusion detection event was not captured correctly"
    
# Running the full integration test
test_full_integration()
