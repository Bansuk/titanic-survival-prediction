"""
Route module for Passenger routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.passenger_schema import PassengerSchema, PassengerViewSchema
from schemas.passenger_dataclass import PassengerData
from business.passenger_business import create_passenger
from repositories.passenger_repository import get_all_passengers
from routes.docs.passenger_doc import (
    GET_PASSENGER_SUMMARY,
    GET_PASSENGER_DESCRIPTION,
    POST_PASSENGER_SUMMARY,
    POST_PASSENGER_DESCRIPTION,
    passenger_responses,
)

passenger_bp = SmorestBlueprint(
    'Passenger', __name__, description='Operações em Passageiros(as)')


@passenger_bp.route('/passenger', methods=['POST'])
@passenger_bp.arguments(PassengerSchema)
@passenger_bp.response(201, PassengerViewSchema, description='Passageiro(a) cadastrado(a) com sucesso.')
@passenger_bp.doc(summary=POST_PASSENGER_SUMMARY, description=POST_PASSENGER_DESCRIPTION,
                  responses=passenger_responses)
def add_passenger(passenger_data):
    """
    Handles the creation of a new passenger.

    This endpoint processes a form submission (JSON) to create a new passenger record.

    Receives a JSON payload with 'name', 'ticket_class', 'sex', 'age', 'number_siblings_spouses',
    'number_parents_children', 'ticket', 'fare', 'cabin', 'embarked', 
    calls the business logic to create a passenger,
    and returns an appropriate response.

    Returns:
        JSON response:
        - 201 (Created): Passenger created successfully.
        - 400 (Bad Request): Invalid body JSON format.
        - 422 (Unprocessable Entity): Validation error.
    """

    data = PassengerData(**passenger_data)
    return create_passenger(data)


@passenger_bp.route('/passengers', methods=['GET'])
@passenger_bp.response(200, PassengerViewSchema(many=True))
@passenger_bp.doc(summary=GET_PASSENGER_SUMMARY, description=GET_PASSENGER_DESCRIPTION)
def get_passengers():
    """
    Retrieve a list of all passengers.

    This endpoint returns a collection of passenger records in JSON format.

    Responses:         
        JSON response:
        - 200 (OK): Successfully retrieved the list of passengers.                                                     
    """

    return get_all_passengers()
