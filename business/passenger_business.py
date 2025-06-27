"""
Business module for Passenger entities.
"""

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
                          survived=True)

    try:
        db.session.add(passenger)
        db.session.commit()

        return passenger
    except Exception as error:
        db.session.rollback()
        raise error
