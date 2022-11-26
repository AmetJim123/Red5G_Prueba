import psycopg2
from psycopg2 import DatabaseError
from decouple import config
import traceback

def get_connection():
    try:
        connection = psycopg2.connect(
            user = config('USER'),
            password = config('PASSWORD'),
            host = config('HOST'),
            port = config('PORT'),
            database = config('DATABASE')
        )
        return connection
    except DatabaseError as e:
        print(traceback.format_exc())
        return e