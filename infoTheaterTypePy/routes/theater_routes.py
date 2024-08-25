from flask import Blueprint
from controllers.theater_controller import list_theater

theater_bp = Blueprint('theater_bp', __name__)

@theater_bp.route('/rooms', methods=['GET'])
def get_theaters():
    """
    Devuelve una lista de salas de teatro.
    ---
    responses:
      200:
        description: Lista de salas de teatro
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID de la sala de teatro
              name:
                type: string
                description: Tipo de la sala de teatro
              description:
                type: string
                description: Descripción de la sala de teatro
      500:
        description: Error al leer los datos de las salas de teatro
    """
    return list_theater()
