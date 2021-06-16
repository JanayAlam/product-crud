import os

import mysql.connector
from dotenv import load_dotenv

# loading the dot env file
load_dotenv()

mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME"),
    auth_plugin="mysql_native_password"
)

cursor = mydb.cursor()
