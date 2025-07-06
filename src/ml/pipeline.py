"""
Pipeline loader module.

This module provides a `Pipeline` class to load a serialized machine
 learning pipeline from disk using pickle.
"""

import pickle


class Pipeline:
    """
    Pipeline handler for loading a pre-trained model pipeline.

    This class provides a method to load a serialized pipeline
    from disk using pickle.
    """

    def __init__(self):
        self.pipeline = None

    def load_pipeline(self, path: str):
        """
        Load a pre-trained model pipeline from a pickle file.

        Args:
            path (str): Path to the pickled pipeline file.

        Returns:
            Any: The deserialized pipeline object.
        """

        with open(path, 'rb') as file:
            self.pipeline = pickle.load(file)
        return self.pipeline
