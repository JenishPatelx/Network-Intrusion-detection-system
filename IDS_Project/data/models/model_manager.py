import os
import pickle

MODEL_DIR = "data/models/"

class ModelManager:
    def __init__(self, model_dir=MODEL_DIR):
        self.model_dir = model_dir
        os.makedirs(self.model_dir, exist_ok=True)

    def save_model(self, model, filename):
        """
        Save a machine learning model as a pickle file.
        :param model: Trained model object.
        :param filename: Name of the file to save.
        """
        filepath = os.path.join(self.model_dir, filename)
        with open(filepath, "wb") as file:
            pickle.dump(model, file)
        print(f"Model saved to {filepath}")

    def load_model(self, filename):
        """
        Load a machine learning model from a pickle file.
        :param filename: Name of the file to load.
        :return: Loaded model object.
        """
        filepath = os.path.join(self.model_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Model file {filepath} does not exist.")
        with open(filepath, "rb") as file:
            return pickle.load(file)

    def list_models(self):
        """
        List all model files in the directory.
        :return: List of file names.
        """
        return [f for f in os.listdir(self.model_dir) if f.endswith(".pkl")]

