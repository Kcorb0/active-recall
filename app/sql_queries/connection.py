import mysql.connector

db_cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="active_recall",
)

cursor = db_cnx.cursor()