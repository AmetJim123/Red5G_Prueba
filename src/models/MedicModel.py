from database.db import get_connection
from .entinty.Medic import Medic, LoginConfirm
from lib.authorizer import generate_token, decode_token

import traceback

class MedicModel():

    #Adding a Medic
    @classmethod
    def add_medic(self, medic):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO medico (nombre, apellido, email, password)
                                VALUES (%s, %s, %s, %s)""",
                                (medic.first_name, medic.last_name, medic.email, medic.password))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            print(traceback.format_exc())
            raise Exception(e)

    #Login a Medic
    @classmethod
    def login_medic(self, medic):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""SELECT "email", "password" FROM medico 
                                    WHERE "email" = %s AND "password" = %s """,
                                    (medic.email, medic.password))

                row = cursor.fetchone()
                medic = None

                if row != None:
                    email = row[0]
                    password = row[1]
                    password = decode_token(password, email)

                    medic = LoginConfirm(email, password)
                    token = generate_token(password, email)
                    medic.token = token
                    medic = medic.to_json()

            connection.close()
            if token:
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute(""" UPDATE medico SET "token" = %s WHERE "email" = %s """, (token, email))
                    connection.commit()
            else:
                return None
            return medic
        except Exception as e:
            print(traceback.format_exc())
            raise Exception(e)