import pandas as pd

class FeatureExtractor:
    """Extracts features from processed data."""

    def __init__(self, df: pd.DataFrame):
        """
        Initializes the FeatureExtractor with the processed data.
        """
        self.df = df  # Store the DataFrame

    def add_time_features(self) -> pd.DataFrame:
        """
        Adds time-based features (e.g., hour) to the DataFrame.
        Assumes the DataFrame has a 'timestamp' column in datetime format.
        """
        if 'timestamp' in self.df.columns:
            # Ensure 'timestamp' is in datetime format
            self.df['timestamp'] = pd.to_datetime(self.df['timestamp'], errors='coerce')

            # Extract the hour from the 'timestamp' column
            self.df['hour'] = self.df['timestamp'].dt.hour
        else:
            print("Warning: 'timestamp' column not found. Time features cannot be added.")
        
        return self.df

    def add_protocol_flags(self) -> pd.DataFrame:
        """
        Adds protocol flags (e.g., is_tcp) to the DataFrame.
        Assumes the DataFrame has a 'protocol' column.
        """
        if 'protocol' in self.df.columns:
            self.df['is_tcp'] = (self.df['protocol'] == 'TCP').astype(int)
        else:
            print("Warning: 'protocol' column not found. Protocol features cannot be added.")
        
        return self.df

    def extract_features(self) -> pd.DataFrame:
        """
        Combines all feature extraction methods into one process.
        """
        self.add_time_features()  # Add time-based features
        self.add_protocol_flags()  # Add protocol flags
        return self.df
