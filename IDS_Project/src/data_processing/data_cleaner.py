import pandas as pd

class DataCleaner:
    """Cleans and preprocesses raw data for IDS."""
    
    def __init__(self, raw_data: pd.DataFrame):
        """
        Initializes the DataCleaner with raw data (either a list of dictionaries or a DataFrame).
        """
        if isinstance(raw_data, pd.DataFrame):
            self.df = raw_data  # If raw_data is already a DataFrame, use it directly
        else:
            self.df = pd.DataFrame(raw_data)  # Otherwise, convert it to DataFrame

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Removes duplicate rows from the DataFrame.
        """
        return self.df.drop_duplicates()

    def handle_missing_values(self) -> pd.DataFrame:
        """
        Fills missing values with 'Unknown'.
        """
        return self.df.fillna("Unknown")

    def clean_data(self) -> pd.DataFrame:
        """
        Perform full cleaning process: remove duplicates and handle missing values.
        """
        self.df = self.remove_duplicates()
        self.df = self.handle_missing_values()
        return self.df

# Example function to load raw data (e.g., from a CSV file)
def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a given file path (CSV, JSON, etc.) and returns it as a DataFrame.
    """
    return pd.read_csv(file_path)  # Change this if you want to load data from another format (e.g., JSON)

def main():
    # Load your raw data from a file (CSV for this example)
    file_path = "your_data_file.csv"  # Replace with your file path
    raw_data = load_data(file_path)

    # Instantiate the DataCleaner with the loaded raw data
    cleaner = DataCleaner(raw_data)

    # Clean the data
    cleaned_data = cleaner.clean_data()

    # Now you can proceed with the cleaned data
    print(cleaned_data.head())  # Just to verify it worked

if __name__ == "__main__":
    main()
