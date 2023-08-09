import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = os.environ.get('DB_USER'),
    password = os.environ.get('DB_PASSWORD')
)

cursorObject = dataBase.cursor()

db_name = os.environ.get('DB_NAME')
cursorObject.execute(f"CREATE DATABASE {db_name}")

print("All Done!")