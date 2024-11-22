from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    """Detects anomalies in network traffic."""
    
    def __init__(self):
        self.model = IsolationForest()

    def train(self, features):
        self.model.fit(features)

    def detect(self, features):
        return self.model.predict(features)

