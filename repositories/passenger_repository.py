"""
Repository module for Passenger queries.
"""

from typing import List
from database.models.passenger import Passenger
from database.db_setup import db


def get_all_passengers() -> List[Passenger]:
    """
    Retrieves all registered passengers.

    Returns:
        List[Passenger]: A list of registered passengers.
    """

    return db.session.query(Passenger).all()
