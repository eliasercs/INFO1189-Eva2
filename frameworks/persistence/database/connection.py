import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def crear_conexion():
    """Crea y retorna la conexión a MySQL"""
    try:
        conexion = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 3306)),
            database=os.getenv('DB_NAME', 'botilleria_db'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
        )
        return conexion
    except Error as e:
        print(f"Error conectando a MySQL: {e}")
        return None