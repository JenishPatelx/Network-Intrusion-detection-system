import os
import json
from datetime import datetime

RAW_DATA_DIR = "data/raw/"

class RawDataHandler:
    def __init__(self, raw_data_dir=RAW_DATA_DIR):
        self.raw_data_dir = raw_data_dir
        os.makedirs(self.raw_data_dir, exist_ok=True)

    def save_raw_data(self, data, filename_prefix="capture"):
        """
        Save raw data to a timestamped JSON file.
        :param data: Raw data (list or dictionary).
        :param filename_prefix: Prefix for the file name.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.json"
        filepath = os.path.join(self.raw_data_dir, filename)
        with open(filepath, "w") as file:
            json.dump(data, file)
        print(f"Raw data saved to {filepath}")

    def list_raw_files(self):
        """
        List all raw data files in the directory.
        :return: List of file names.
        """
        return [f for f in os.listdir(self.raw_data_dir) if f.endswith(".json")]

    def load_raw_data(self, filename):
        """
        Load raw data from a JSON file.
        :param filename: Name of the file to load.
        :return: Data from the file.
        """
        filepath = os.path.join(self.raw_data_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} does not exist.")
        with open(filepath, "r") as file:
            return json.load(file)

