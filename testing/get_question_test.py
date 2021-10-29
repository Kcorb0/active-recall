import mysql.connector


db_cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bombtrack36!",
    database="active_recall",
)

cursor = db_cnx.cursor()

cursor.execute("SELECT * FROM questions")

query_result = cursor.fetchall()

for i in query_result:
    print(i)
    print(f"Question:   {i[1]}")
    print(f"Answer:     {i[2]}\n")