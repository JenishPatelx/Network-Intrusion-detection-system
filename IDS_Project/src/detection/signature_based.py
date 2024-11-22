import pandas as pd

class SignatureBasedDetector:
    """Detects intrusions based on predefined signatures (rules)."""
    
    def __init__(self, signatures=None):
        """
        Initializes the detector with a set of signatures (rules).
        If no signatures are provided, a default set can be used.
        """
        # Default signatures could be a list of IP pairs or protocols to detect
        self.signatures = signatures if signatures is not None else [
            {'source_ip': '192.168.1.1', 'destination_ip': '10.0.0.2', 'protocol': 'TCP'}
        ]
    
    def detect_intrusion(self, features):
        """
        Detects intrusions based on the features and predefined signatures.
        """
        detection_results = []
        
        # Iterate through the feature set and compare with signatures
        for index, feature in features.iterrows():
            for signature in self.signatures:
                if (feature['source_ip'] == signature['source_ip'] and
                    feature['destination_ip'] == signature['destination_ip'] and
                    feature['protocol'] == signature['protocol']):
                    detection_results.append(f"Intrusion detected at index {index}: {feature.to_dict()}")
        
        return detection_results
