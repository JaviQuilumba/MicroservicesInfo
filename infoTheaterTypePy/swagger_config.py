import json
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api-docs'  
API_URL = '/static/swagger.json' 

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Theater Listing Service"
    }
)


swagger_data = {
    "swagger": "2.0",
    "info": {
        "title": "Theater Listing Service",
        "description": "API para listar tipos de salas de teatro",
        "version": "1.0.0"
    },
    "host": "localhost:3017",
    "basePath": "/api",
    "schemes": ["http"],
    "paths": {
        "/rooms": {
            "get": {
                "summary": "Devuelve una lista de salas de teatro",
                "responses": {
                    "200": {
                        "description": "Lista de salas de teatro",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "integer"},
                                    "name": {"type": "string"},
                                    "description": {"type": "string"}
                                }
                            }
                        }
                    },
                    "500": {
                        "description": "Error al leer los datos de las salas de teatro"
                    }
                }
            }
        }
    }
}

with open('static/swagger.json', 'w') as swagger_file:
    json.dump(swagger_data, swagger_file)
