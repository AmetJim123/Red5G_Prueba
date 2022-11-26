from .entinty.Patient import Patient
from database.db import get_connection

class PatientModel():

    @classmethod
    def get_all(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM pacientes")
                
                result_set = cursor.fetchall()
                patients = []

                for row in result_set:
                    patient = Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    patients.append(patient.to_json())
                
            connection.close()
            return patients
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_by_id(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM pacientes WHERE "id" = %s""", (id,))
                
                row = cursor.fetchone()
                patient = None
                if row != None:
                    patient = Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    patient = patient.to_json()
            
            connection.close()
            return patient
        except Exception as e:
            raise Exception(e)

    @classmethod
    def add_patient(self, patient):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(""" INSERT INTO pacientes (nombre, id, edad, genero, temperatura_corporal, malestar, fecha_ingreso, eps, tipo_documento) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                                    (patient.full_name, patient.id, patient.age, patient.gender, patient.corporal_temp, patient.discomfort, patient.date, patient.eps, patient.type_id)) 

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def update_patient(self, patient):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(""" UPDATE pacientes SET nombre = %s, edad = %s, genero = %s, temperatura_corporal = %s, malestar = %s, fecha_ingreso = %s, eps = %s 
                                    WHERE id = %s""", 
                                    (patient.full_name, patient.age, patient.gender, patient.corporal_temp, patient.discomfort, patient.date, patient.eps, patient.id))
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)

    @classmethod
    def delete_patient(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)
