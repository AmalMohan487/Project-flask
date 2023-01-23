import mysql.connector

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database ="netf"
)
CR=DB.cursor(dictionary=True)