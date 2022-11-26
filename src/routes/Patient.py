from flask import Blueprint, request, jsonify

#Entity
from models.entinty.Patient import Patient

#Models
from models.PatientModel import PatientModel

#Blueprint
patient_bp = Blueprint('patient_bp', __name__)


@patient_bp.route('/', methods=['GET'])
def get_all():
    try:
        patients = PatientModel.get_all()
        return jsonify(patients), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@patient_bp.route('/<id>', methods=['GET'])
def get_by_id(id):
    try:
        patient = PatientModel.get_by_id(id)
        if patient != None:
            return jsonify(patient), 200
        else:
            return jsonify({"message": "Patient not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@patient_bp.route('/add', methods=['POST'])
def add_patient():
    try:
        full_name = request.json['nombre']
        id = request.json['id']
        type_id = request.json['tipo_documento']
        age = request.json['edad']
        gender = request.json['genero']
        corporal_temp = request.json['temperatura_corporal']
        discomfort = request.json['malestar']
        date = request.json['fecha_ingreso']
        eps = request.json['eps']

        patient = Patient(full_name, id, age, gender, corporal_temp, discomfort, date, eps, type_id)
        affected_rows = PatientModel.add_patient(patient)

        if affected_rows == 1:
            return jsonify({"message": "Patient added"}), 201
        else:
            return jsonify({"message": "Patient not added"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@patient_bp.route('/update/<id>', methods=['PUT'])
def update_patient(id):
    try:
        full_name = request.json['nombre']
        age = request.json['edad']
        gender = request.json['genero']
        corporal_temp = request.json['temperatura_corporal']
        discomfort = request.json['malestar']
        date = request.json['fecha_ingreso']
        eps = request.json['eps']

        patient = Patient(full_name, id, age, gender, corporal_temp, discomfort, date, eps)
        affected_rows = PatientModel.update_patient(patient)

        if affected_rows == 1:
            return jsonify({"message": "Patient updated"}), 200
        else:
            return jsonify({"message": "Patient not updated"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

@patient_bp.route('/delete/<id>', methods=['DELETE'])
def delete_patient(id):
    try:
        affected_rows = PatientModel.delete_patient(id)

        if affected_rows == 1:
            return jsonify({"message": "Patient deleted"}), 200
        else:
            return jsonify({"message": "Patient not deleted"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500
