"""
Dataclass module for the Passenger.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class PassengerData:
    """
    Represents a passenger.

    Attributes:
        name (str): The name of the passenger.
        ticket_class (int): The passenger's ticket class.
        sex (str): The passenger's gender.
        age (float): The passenger's age.
        number_siblings_spouses (int): The number of siblings and/or
        spouses related to the passenger aboard of the Titanic.
        number_parents_children (int): The number of parents and/or
        children related to the passenger aboard of the Titanic.
        ticket (str): The number of the passenger's ticket.
        fare (float): The price of the passenger's ticket.
        cabin (str): The ticket's designated cabin.
        embarked (str): The passenger's boarding port.
    """

    name: str
    ticket_class: int
    sex: str
    number_siblings_spouses: int
    number_parents_children: int
    ticket: str
    fare: float
    age: Optional[float] = None
    cabin: Optional[str] = None
    embarked: Optional[str] = None
