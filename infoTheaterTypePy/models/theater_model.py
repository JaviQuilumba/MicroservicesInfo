import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

class Theater:
    @staticmethod
    def find_all():
        try:
            connection = psycopg2.connect(
                user=Config.DB_USER,
                host=Config.DB_HOST,
                database=Config.DB_NAME,
                password=Config.DB_PASSWORD,
                port=Config.DB_PORT
            )
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute('SELECT * FROM rooms')
            theaters = cursor.fetchall()
            cursor.close()
            connection.close()
            return theaters
        except Exception as e:
            raise Exception(f"Error connecting to the database: {str(e)}")
