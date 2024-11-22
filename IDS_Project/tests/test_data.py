from data.raw.raw_data_handler import RawDataHandler
from data.processed.processed_data_handler import ProcessedDataHandler
from data.models.model_manager import ModelManager
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Test Raw Data Handler
raw_handler = RawDataHandler()
raw_data = [{"source_ip": "192.168.1.1", "destination_ip": "10.0.0.2", "protocol": "TCP"}]
raw_handler.save_raw_data(raw_data, filename_prefix="traffic")
print("Raw files:", raw_handler.list_raw_files())
print("Loaded raw data:", raw_handler.load_raw_data(raw_handler.list_raw_files()[0]))

# Test Processed Data Handler
processed_handler = ProcessedDataHandler()
df = pd.DataFrame(raw_data)
processed_handler.save_processed_data(df, "processed_traffic.csv")
print("Processed files:", processed_handler.list_processed_files())
print("Loaded processed data:\n", processed_handler.load_processed_data("processed_traffic.csv"))

# Test Model Manager
model_manager = ModelManager()
clf = RandomForestClassifier()
model_manager.save_model(clf, "random_forest_model.pkl")
loaded_model = model_manager.load_model("random_forest_model.pkl")
print("Loaded Model:", loaded_model)

