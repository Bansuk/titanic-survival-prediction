"""
Test script for the Titanic SVM model pipeline.

Loads a pre-trained pipeline, preprocesses the test dataset,
makes predictions, and asserts that model accuracy meets a minimum threshold.
"""

from ml.pipeline import Pipeline
from ml.preprocessor import PreProcessor
import pandas as pd
from sklearn.metrics import accuracy_score


dataset = pd.read_csv('./src/data/test_dataset_titanic.csv')


def test_model_svm():
    """
    Test the Titanic SVM model pipeline.

    Steps:
    - Load the pre-trained model and preprocessing bundle.
    - Extract model and preprocessor.
    - Preprocess test features.
    - Make predictions on the test data.
    - Compute accuracy score.
    - Assert that the model's accuracy is at least 80%.

    Raises:
        AssertionError: If model accuracy is below the required threshold.
    """

    pipeline = Pipeline()
    preprocessor = PreProcessor()

    bundle = pipeline.load_pipeline('./src/ml/titanic_model_bundle.pkl')

    model = bundle['model']
    pp = bundle['preprocessor']

    X = dataset.iloc[:, 0:-1]
    y = dataset.iloc[:, -1]

    X = preprocessor.scale_data(X, pp)

    predictions = model.predict(X)

    acuracia_lr = accuracy_score(y, predictions)

    assert acuracia_lr >= 0.8, f"Model accuracy too low: {acuracia_lr:.4f}"
