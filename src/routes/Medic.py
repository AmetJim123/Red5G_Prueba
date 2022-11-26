from flask import Blueprint, jsonify, request

#Entities
from models.entinty.Medic import Medic, LoginConfirm

#Models
from models.MedicModel import MedicModel

medic_bp = Blueprint('medic_bp', __name__)

@medic_bp.route('/add', methods=['POST'])
def add_medic():
    try:
        first_name = request.json['nombre']
        last_name = request.json['apellido']
        email = request.json['email']
        password = request.json['password']
        medic = Medic(first_name, last_name, email, password)
        affected_rows = MedicModel.add_medic(medic)

        if affected_rows == 1:
            return jsonify({"message": "Medic added"}), 200
        else:
            return jsonify({"message": "Error creating Medic"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@medic_bp.route('/login', methods=['POST'])
def login_medic():
    try:
        email = request.json['email']
        password = request.json['password']
        medic = LoginConfirm(email, password)
        affected_rows = MedicModel.login_medic(medic)
        if affected_rows:
            return jsonify({"message": "Welcome, {}".format(affected_rows['email'])}), 200
        else:
            return jsonify({"message": "User or password are incorrect"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500