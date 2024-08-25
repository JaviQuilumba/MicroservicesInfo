from flask import jsonify
from models.theater_model import Theater

def list_theater():
    try:
        theaters = Theater.find_all()
        return jsonify(theaters), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
