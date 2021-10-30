import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
import mysql.connector

db_cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="active_recall",
)

cursor = db_cnx.cursor()


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/ar_gui.ui', self)
        self.setWindowTitle("Active Recall")

        self.start_btn.clicked.connect(self.game_pg)
        self.begin_btn.clicked.connect(self.play_pg)
        self.add_btn.clicked.connect(self.create_pg)
        self.view_questions_btn.clicked.connect(self.see_questions_pg)
        self.analytics_btn.clicked.connect(self.view_graph_pg)

        # Creating new questions and categories
        self.add_cat_btn.clicked.connect(self.add_category)
        self.add_question_btn.clicked.connect(self.add_question)

    def game_pg(self):
        self.content_widget.setCurrentIndex(0)
    
    def play_pg(self):
        self.content_widget.setCurrentIndex(1)
    
    def create_pg(self):
        self.content_widget.setCurrentIndex(2)

    def see_questions_pg(self):
        self.content_widget.setCurrentIndex(3)

    def view_graph_pg(self):
        self.content_widget.setCurrentIndex(4)

    def add_category(self):
        item = self.add_cat_input.displayText()
        self.add_cat_input.setText("")
        self.select_cat_combo.addItem(item)

    def add_question(self):
        category = self.select_cat_combo.currentText()
        question = self.new_question_input.toPlainText()
        answer = self.new_answer_input.toPlainText()

        cursor.execute("SELECT cat_id FROM categories WHERE cat_name = %s", (category, ))
        cat_id = cursor.fetchall()[0][0]

        q_values = (question, answer, int(cat_id))
        q_sql = "INSERT INTO questions (question, answer, cat_id) VALUES (%s, %s, %s)"

        cursor.execute(q_sql, q_values)
        db_cnx.commit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = AppWindow()
    myApp.show()
    sys.exit(app.exec())