import mysql.connector


db_cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="active_recall",
)

cursor = db_cnx.cursor()

cursor.execute("SELECT cat_name FROM categories")

query_result = cursor.fetchall()

for i in query_result:
    print(i[0])