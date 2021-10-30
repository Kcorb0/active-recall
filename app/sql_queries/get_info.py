from .connection import cursor, db_cnx

def get_questions(category):

    cursor.execute("SELECT cat_id FROM categories WHERE cat_name = %s", (category, ))
    cat_id = cursor.fetchall()[0][0]

    cursor.execute("SELECT que_id, question, answer FROM questions WHERE cat_id = %s", (int(cat_id), ))
    question_set = cursor.fetchall()

    return question_set

def get_categories():
    cursor.execute("SELECT cat_name FROM categories")
    list_cats = [name[0] for name in cursor.fetchall()]

    return list_cats