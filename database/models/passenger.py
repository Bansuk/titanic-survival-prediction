"""
This module defines the Passenger model for the database.
"""

from datetime import datetime, timezone
from database.db_setup import db


class Passenger(db.Model):
    """
    Represents a passenger entity in the database.

    Attributes:
        id (int): Primary key identifier.
        name (str): Name of the passenger.
        ticket_class (int): Class of the ticket.
        sex (str): Gender of the passenger.
        age (float): Age of the passenger.
        number_siblings_spouses (int): Number of siblings and/or spouses aboard.
        number_parents_children (int): Number of parents and/or children aboard.
        ticket (int): Number of the ticket.
        fare (float): Price of the ticket.
        cabin (str): Number of the cabin.
        embarked (str): Passenger's boarding port.
        survived (int): The fate of the passenger after the collision.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """

    __tablename__ = 'passenger'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ticket_class = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Float, nullable=False)
    number_siblings_spouses = db.Column(db.Integer, nullable=False)
    number_parents_children = db.Column(db.Integer, nullable=False)
    ticket = db.Column(db.Integer, nullable=False)
    fare = db.Column(db.Float, nullable=False)
    cabin = db.Column(db.String(3), nullable=False)
    embarked = db.Column(db.String(11), nullable=False)
    survived = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


def __init__(
    self,
    name: str,
    ticket_class: int,
    sex: str,
    age: float,
    number_siblings_spouses: int,
    number_parents_children: int,
    ticket: int,
    fare: float,
    cabin: str,
    embarked: str,
    survived: int
) -> None:
    self.name = name
    self.ticket_class = ticket_class
    self.sex = sex
    self.age = age
    self.number_siblings_spouses = number_siblings_spouses
    self.number_parents_children = number_parents_children
    self.ticket = ticket
    self.fare = fare
    self.cabin = cabin
    self.embarked = embarked
    self.survived = survived
