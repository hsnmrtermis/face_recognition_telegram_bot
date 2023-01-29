import psycopg2
from psycopg2 import Error

class Database:
    database = "facedetection"
    username = "postgres"
    password = "123456"
    host = "localhost"
    port = "5432"
    connection = None
    cursor = None
    
    def __init__(self) -> None:
        pass
    
    def connect(self):
        self.connection = psycopg2.connect(
            user= self.username,
            password= self.password,
            host = self.host,
            port = self.port,
            database = self.database
        )
        self.cursor = self.connection.cursor()
        return self
        
    def close(self):
        self.cursor.close()
        self.connection.close()
        return self
    
    def get_users(self):
        self.cursor.execute('SELECT * FROM facedetection.public.people');
        return self.cursor.fetchall()
            