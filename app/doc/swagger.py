from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint

SWAGGER_URL = '/api/docs'  
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL,
    config={  
        'app_name': "API DataTarget"
    }
)

swagger_blueprint = Blueprint('swagger', __name__)
swagger_blueprint.register_blueprint(swaggerui_blueprint)