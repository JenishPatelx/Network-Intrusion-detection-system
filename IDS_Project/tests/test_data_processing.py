import pandas as pd
from src.data_processing.data_cleaner import DataCleaner
from src.data_processing.feature_extractor import FeatureExtractor

def test_data_cleaner():
    cleaner = DataCleaner()
    raw_data = pd.DataFrame({"ip": ["192.168.1.1", "192.168.1.1", None]})
    cleaned_data = cleaner.remove_duplicates(raw_data)
    assert len(cleaned_data) == 2
    cleaned_data = cleaner.handle_missing_values(cleaned_data)
    assert "Unknown" in cleaned_data["ip"].values

def test_feature_extractor():
    extractor = FeatureExtractor()
    raw_data = pd.DataFrame({"timestamp": ["2024-11-22 10:00:00"], "protocol": ["TCP"]})
    processed_data = extractor.add_time_features(raw_data)
    assert "hour" in processed_data.columns
    processed_data = extractor.add_protocol_flags(processed_data)
    assert "is_tcp" in processed_data.columns

