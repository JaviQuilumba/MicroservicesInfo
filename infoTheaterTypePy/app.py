from flask import Flask, jsonify
from routes.theater_routes import theater_bp
from swagger_config import swagger_ui_blueprint, SWAGGER_URL
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(theater_bp, url_prefix='/api')

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "ok", "message": "Microservice List Theater Running"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3017, debug=True)
