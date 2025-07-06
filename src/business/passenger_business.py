"""
Business module for Passenger entities.
"""

from ml.pipeline import Pipeline
from ml.preprocessor import PreProcessor
from schemas.passenger_dataclass import PassengerData
from database.models.passenger import Passenger
from database.db_setup import db


def create_passenger(data: PassengerData) -> Passenger:
    """
    Creates a new passenger and determines if he/she survived the collision.

    Args:
        data (PassengerData): Information about the passenger.

    Returns:
        Passenger: Created passenger with survival outcome.
    """

    survived = get_passenger_survival_prediction(data)

    passenger = Passenger(name=data.name,
                          ticket_class=data.ticket_class,
                          sex=data.sex,
                          age=data.age,
                          number_siblings_spouses=data.number_siblings_spouses,
                          number_parents_children=data.number_parents_children,
                          ticket=data.ticket,
                          fare=data.fare,
                          cabin=data.cabin,
                          embarked=data.embarked,
                          survived=survived)

    try:
        db.session.add(passenger)
        db.session.commit()

        return passenger
    except Exception as error:
        db.session.rollback()
        raise error


def get_passenger_survival_prediction(data: PassengerData) -> bool:
    """
    Utilizes a trained model to predict the passenger survival outcome.

    Args:
        data (PassengerData): Information about the passenger.

    Returns:
        bool: Survival outcome of the provided passenger.
    """

    pipeline = Pipeline()
    preprocessor = PreProcessor()

    bundle = pipeline.load_pipeline("src/ml/titanic_model_bundle.pkl")

    model = bundle['model']
    pp = bundle['preprocessor']

    df = preprocessor.dataclass_to_dataframe(data)
    X_scaled = preprocessor.preprocess_new_data(df, pp)
    prediction = model.predict(X_scaled)

    return prediction[0]
