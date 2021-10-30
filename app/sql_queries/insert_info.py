from .connection import cursor, db_cnx

def insert_categories(category):
    values = (category, )
    sql = "INSERT INTO categories (cat_name) VALUES (%s)"
    cursor.execute(sql, values)
    db_cnx.commit()


def insert_question(question, answer, category):

    cursor.execute("SELECT cat_id FROM categories WHERE cat_name = %s", (category, ))
    cat_id = cursor.fetchall()[0][0]

    values = (question, answer, int(cat_id))
    sql = "INSERT INTO questions (question, answer, cat_id) VALUES (%s, %s, %s)"

    cursor.execute(sql, values)
    db_cnx.commit()
