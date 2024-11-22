import pandas as pd
from detection.signature_based import SignatureBasedDetector

class HybridDetector:
    """Hybrid detector combining multiple detection techniques."""
    
    def __init__(self):
        # Initialize with the SignatureBasedDetector
        self.signature_detector = SignatureBasedDetector()
    
    def detect(self, data: pd.DataFrame) -> list:
        """
        Run signature-based detection on the data.
        """
        # Call the detect_intrusion method of SignatureBasedDetector
        alerts = self.signature_detector.detect_intrusion(data)
        return alerts
