import mysql.connector


db_cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="active_recall",
)

cursor = db_cnx.cursor()

# Retrieve category id
category = "Data Fundamentals"
cursor.execute("SELECT cat_id FROM categories WHERE cat_name = %s", (category, ))
cat_id = cursor.fetchall()[0][0]
print(cat_id)


question = "What are datasets?"
answer = "Datasets are logical groupings of data that are closely related or share the same data structure (MNIST)."

newq_values = (question, answer, int(cat_id))
newq_sql = "INSERT INTO questions (question, answer, cat_id) VALUES (%s, %s, %s)"

cursor.execute(newq_sql, newq_values)

db_cnx.commit()