from connection import cursor, db_cnx

def clear_database():
    sql = """
        DROP DATABASE IF EXISTS active_recall;
        CREATE DATABASE active_recall;
        USE active_recall;

        CREATE TABLE categories (
            cat_id INT NOT NULL AUTO_INCREMENT,
            cat_name VARCHAR(50),
            PRIMARY KEY (cat_id)
        );

        ALTER TABLE categories AUTO_INCREMENT=1;

        CREATE TABLE questions (
            que_id int NOT NULL AUTO_INCREMENT,
            question varchar(250),
            answer varchar(250),
            cat_id int,
            PRIMARY KEY (que_id),
            FOREIGN KEY (cat_id) REFERENCES categories(cat_id)
        );

        ALTER TABLE questions AUTO_INCREMENT=1;
        """
    cursor.execute(sql)


clear_database()