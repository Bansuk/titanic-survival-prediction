"""
This module contains standard descriptions and responses for the Passenger API.
"""

from schemas.error_schema import ErrorSchema

GET_PASSENGER_SUMMARY = 'Retorna a lista de todos os passageiros(as).'
GET_PASSENGER_DESCRIPTION = 'Este endpoint retorna uma coleção de registros de passageiros(as) ' \
    'no formato JSON.'
POST_PASSENGER_SUMMARY = 'Lida com a criação de um novo passageiro(a).'
POST_PASSENGER_DESCRIPTION = 'Este endpoint processa o envio de um formulário (JSON) ' \
    'para criar um novo registro de passageiro(a).'

passenger_responses = {
    400: {
        'description': 'Bad Request: O formato do corpo JSON é inválido.',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 400,
                    'errors': {
                        'json': [
                            'Invalid JSON body.'
                        ]
                    },
                    'status': 'Bad Request'
                }
            }
        }
    },
    422: {
        'description':
        'Validation Error: A requisição contém campos ausentes ou inválidos.\n\n'
        '**Motivos Possíveis:**\n'
        '- `name` é obrigatório, mas não foi fornecido.\n'
        '- `name` o número de caracteres deve estar enre 3 e 100.\n'
        '- `ticket_class` é obrigatório, mas não foi fornecido.\n'
        '- `ticket_class` valor deve ser 1, 2 ou 3.\n'
        '- `sex` é obrigatório, mas não foi fornecido.\n'
        '- `sex` valor deve ser `male` ou `female`.\n'
        '- `age` valor deve estar entre 0 e 120.\n'
        '- `number_siblings_spouses` é obrigatório, mas não foi fornecido.\n'
        '- `number_siblings_spouses` o valor deve ser maior ou igual a 0.\n'
        '- `number_parents_children` é obrigatório, mas não foi fornecido.\n'
        '- `number_parents_children` o valor deve ser maior ou igual a 0.\n'
        '- `ticket` é obrigatório, mas não foi fornecido.\n'
        '- `fare` é obrigatório, mas não foi fornecido.\n'
        '- `fare` o valor deve ser maior ou igual a 0.\n'
        '- `cabin` formato inválido.\n'
        '- `embarked` valor deve ser Cherbourg, Queenstown ou Southampton.\n\n',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 422,
                    'errors': {
                        'json': {
                            'name': ['Missing data for required field.',
                                     'Name length must be between 3 and 100 characters.'],
                            'ticket_class': ['Missing data for required field.',
                                             'Ticket class must be 1 (First), 2 (Second), or 3 (Third).'],
                            'sex': ['Missing data for required field.',
                                    'Sex must be either male or female.'],
                            'age': ['Age must be between 0 and 120 years.'],
                            'number_siblings_spouses': ['Missing data for required field.',
                                                        'The number of siblings and / or spouses related to the passenger '
                                                        'aboard of the Titanic must be equal to or larger than 0.'],
                            'number_parents_children': ['Missing data for required field.',
                                                        '"The number of parents and/or children related to the passenger '
                                                        'aboard of the Titanic must be equal to or larger than 0.'],
                            'ticket': ['Missing data for required field.'],
                            'fare': ['Missing data for required field.', 'The fare value must be at least 0.'],
                            'cabin': ['Cabin format is invalid.'],
                            'embarked': ['Embkarked value must be one either Cherbourg, Queenstown or Southampton.'],
                        }
                    },
                    'status': 'Unprocessable Entity'
                }
            }
        }
    }
}
