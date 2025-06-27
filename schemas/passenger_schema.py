"""
Schema module for Passenger entities.
"""

from marshmallow import Schema, fields, validate

NAME_METADATA = metadata = {
    'example': 'Fulano de Tal'}
NAME_DESCRIPTION = 'Nome do(a) Passageiro(a)'
TICKET_CLASS_METADATA = metadata = {
    'example': 1}
TICKET_CLASS_DESCRIPTION = 'Classe do Ticket do(a) Passageiro(a)'
SEX_METADATA = metadata = {
    'example': 'female'}
SEX_DESCRIPTION = 'Gênero do(a) Passageiro(a)'
AGE_METADATA = metadata = {
    'example': 30}
AGE_DESCRIPTION = 'Idade do(a) Passageiro(a)'
NUMBER_SIBLINGS_SPOUSES_METADATA = metadata = {
    'example': 0}
NUMBER_SIBLINGS_SPOUSES_DESCRIPTION = 'Número de irmãos/irmãs e/ou cônjuges ' \
    'do(a) Passageiro(a) a bordo do Titanic'
NUMBER_PARENTS_CHILDREN_METADATA = metadata = {
    'example': 1}
NUMBER_PARENTS_CHILDREN_DESCRIPTION = 'Número de pais e/ou filhos(as) ' \
    'do(a) Passageiro(a) a bordo do Titanic'
TICKET_METADATA = metadata = {
    'example': 'PC 17569'}
TICKET_DESCRIPTION = 'Número do ticket do(a) Passageiro(a)'
FARE_METADATA = metadata = {
    'example': 21.30}
FARE_DESCRIPTION = 'Número do ticket do(a) Passageiro(a)'
CABIN_METADATA = metadata = {
    'example': 'C85'}
CABIN_DESCRIPTION = 'Cabine do(a) Passageiro(a)'
EMBARKED_METADATA = metadata = {
    'example': 'Cherbourg'}
EMBARKED_DESCRIPTION = 'Porto de embarque do(a) Passageiro(a)'
SURVIVED_METADATA = metadata = {
    'example': True}
SURVIVED_DESCRIPTION = 'Sobrevivência do Passageiro(a)'


class PassengerSchema(Schema):
    """
    Schema for validating and serializing passenger input data.

    Attributes:
        name (str): The name of the passenger (min 3, max 100 characters).
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

    name = fields.Str(required=True, metadata=NAME_METADATA,
                      description=NAME_DESCRIPTION, validate=validate.Length(min=3, max=100))
    ticket_class = fields.Integer(required=True, metadata=TICKET_CLASS_METADATA,
                                  description=TICKET_CLASS_DESCRIPTION, validate=validate.OneOf(
                                      [1, 2, 3],
                                      error="Ticket class must be 1 (First), 2 (Second), or 3 (Third)")
                                  )
    sex = fields.Str(required=True, metadata=SEX_METADATA,
                     description=SEX_DESCRIPTION, validate=validate.OneOf(
                         ['male', 'female'],
                         error="Sex must be either male or female.")
                     )
    age = fields.Float(required=False, allow_none=True, metadata=AGE_METADATA,
                       description=AGE_DESCRIPTION, validate=validate.Range(
                           min=0, max=100),
                       error="Age must be between 0 and 100 years.")
    number_siblings_spouses = fields.Integer(required=True,
                                             metadata=NUMBER_SIBLINGS_SPOUSES_METADATA,
                                             description=NUMBER_SIBLINGS_SPOUSES_DESCRIPTION,
                                             validate=validate.Range(min=0),
                                             error="The number of siblings and/or spouses related to the passenger "
                                             "aboard of the Titanic must be equal to or larger than 0.")
    number_parents_children = fields.Integer(required=True,
                                             metadata=NUMBER_PARENTS_CHILDREN_METADATA,
                                             description=NUMBER_PARENTS_CHILDREN_DESCRIPTION,
                                             validate=validate.Range(min=0),
                                             error="The number of parents and/or children related to the passenger "
                                             "aboard of the Titanic must be equal to or larger than 0.")
    ticket = fields.Str(
        required=True, metadata=TICKET_METADATA, description=TICKET_DESCRIPTION)
    fare = fields.Float(
        required=False, allow_none=True, metadata=FARE_METADATA, description=FARE_DESCRIPTION,
        validate=validate.Range(min=0),
        error="The fare value must be at least 0.")
    cabin = fields.Str(
        required=False, allow_none=True, metadata=CABIN_METADATA, description=CABIN_DESCRIPTION,
        validate=validate.Regexp(r"^[A-Z][\w\s]*$",
                                 error="Cabin format is invalid.")
    )
    embarked = fields.Str(
        required=False, allow_none=True, metadata=EMBARKED_METADATA,
        description=EMBARKED_DESCRIPTION,
        validate=validate.OneOf(['Cherbourg', 'Queenstown', 'Southampton']))


class PassengerViewSchema(Schema):
    """
    Schema for serializing passenger data for output.

    Attributes:
        id (int): The unique identifier of the passenger.
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
        survived (bool): The fate of the passenger after the collision.
    """

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, metadata=NAME_METADATA,
                      description=NAME_DESCRIPTION)
    ticket_class = fields.Integer(required=True, metadata=TICKET_CLASS_METADATA,
                                  description=TICKET_CLASS_DESCRIPTION
                                  )
    sex = fields.Str(required=True, metadata=SEX_METADATA,
                     description=SEX_DESCRIPTION)
    age = fields.Float(required=True, metadata=AGE_METADATA,
                       description=AGE_DESCRIPTION)
    number_siblings_spouses = fields.Integer(required=True,
                                             metadata=NUMBER_SIBLINGS_SPOUSES_METADATA,
                                             description=NUMBER_SIBLINGS_SPOUSES_DESCRIPTION)
    number_parents_children = fields.Integer(required=True,
                                             metadata=NUMBER_PARENTS_CHILDREN_METADATA,
                                             description=NUMBER_PARENTS_CHILDREN_DESCRIPTION)
    ticket = fields.Str(
        required=True, metadata=TICKET_METADATA, description=TICKET_DESCRIPTION)
    fare = fields.Float(
        required=True, metadata=FARE_METADATA, description=FARE_DESCRIPTION)
    cabin = fields.Str(
        required=True, metadata=CABIN_METADATA, description=CABIN_DESCRIPTION)
    embarked = fields.Str(
        required=True, metadata=EMBARKED_METADATA, description=EMBARKED_DESCRIPTION)
    survived = fields.Bool(
        required=True, metadata=SURVIVED_METADATA, description=SURVIVED_DESCRIPTION)
