import os
import pandas as pd

PROCESSED_DATA_DIR = "data/processed/"

class ProcessedDataHandler:
    def __init__(self, processed_data_dir=PROCESSED_DATA_DIR):
        self.processed_data_dir = processed_data_dir
        os.makedirs(self.processed_data_dir, exist_ok=True)

    def save_processed_data(self, dataframe, filename):
        """
        Save processed data to a CSV file.
        :param dataframe: Pandas DataFrame to save.
        :param filename: Name of the output file.
        """
        filepath = os.path.join(self.processed_data_dir, filename)
        dataframe.to_csv(filepath, index=False)
        print(f"Processed data saved to {filepath}")

    def list_processed_files(self):
        """
        List all processed data files in the directory.
        :return: List of file names.
        """
        return [f for f in os.listdir(self.processed_data_dir) if f.endswith(".csv")]

    def load_processed_data(self, filename):
        """
        Load processed data from a CSV file.
        :param filename: Name of the file to load.
        :return: Pandas DataFrame.
        """
        filepath = os.path.join(self.processed_data_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} does not exist.")
        return pd.read_csv(filepath)

