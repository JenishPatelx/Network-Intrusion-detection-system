from src.detection.signature_based import SignatureBasedDetector
from src.detection.anomaly_detection import AnomalyDetector

def test_signature_based_detector():
    detector = SignatureBasedDetector()
    mock_data = [{"signature": "malware_signature"}, {"signature": "unknown"}]
    alerts = detector.detect(mock_data)
    assert len(alerts) == 1

def test_anomaly_detector():
    detector = AnomalyDetector()
    features = [[1, 2], [2, 3], [3, 4]]
    detector.train(features)
    predictions = detector.detect(features)
    assert len(predictions) == 3

