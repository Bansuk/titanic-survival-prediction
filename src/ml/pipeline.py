import pickle


class Pipeline:

    def __init__(self):
        self.pipeline = None

    def load_pipeline(self, path: str):

        with open(path, 'rb') as file:
            self.pipeline = pickle.load(file)
        return self.pipeline
