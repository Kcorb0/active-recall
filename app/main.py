import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

from sql_queries.insert_info import insert_categories, insert_question
from sql_queries.get_info import get_categories, get_questions


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/gui/ar_gui.ui', self)
        self.setWindowTitle("Active Recall")

        # Fill combo boxes
        self.fill_cat_combo(self.cat_combo)
        self.fill_cat_combo(self.select_cat_combo)
        self.fill_cat_combo(self.view_cat_combo)
        self.fill_cat_combo(self.analyze_cat_combo)

        # Navigation buttons
        self.start_btn.clicked.connect(self.game_pg)
        self.add_btn.clicked.connect(self.create_pg)
        self.view_questions_btn.clicked.connect(self.see_questions_pg)
        self.analytics_btn.clicked.connect(self.view_graph_pg)

        # Starting the game
        self.begin_btn.clicked.connect(self.start_game)

        # Creating new questions and categories
        self.add_cat_btn.clicked.connect(self.add_category)
        self.add_question_btn.clicked.connect(self.add_question)

    def game_pg(self):
        self.content_widget.setCurrentIndex(0)
    
    def create_pg(self):
        self.content_widget.setCurrentIndex(2)

    def see_questions_pg(self):
        self.content_widget.setCurrentIndex(3)

    def view_graph_pg(self):
        self.content_widget.setCurrentIndex(4)

    def fill_cat_combo(self, combobox):
        """Fills all category combo boxes throughout the app"""

        for cat_name in get_categories():
            combobox.addItem(cat_name)

    def add_category(self):
        """Create a new category that is added to the database"""

        category = self.add_cat_input.displayText()
        self.add_cat_input.setText("")
        self.select_cat_combo.addItem(category)
        insert_categories(category)

    def add_question(self):
        """Adds new question to the database"""

        category = self.select_cat_combo.currentText()
        question = self.new_question_input.toPlainText()
        answer = self.new_answer_input.toPlainText()

        self.new_question_input.setPlainText("")
        self.new_answer_input.setPlainText("")

        insert_question(question, answer, category)


    def start_game(self):

        self.content_widget.setCurrentIndex(1)
        
        category_title = self.cat_combo.currentText()

        # Generate Questions
        question_set = get_questions(category_title)

        # Setup first round
        round = 1
        max_round = 20
        question = question_set[round-1][1]
        answer = question_set[round-1][2]

        self.cat_title_lbl.setText(category_title)
        self.round_lbl.setText(f"{round} / {max_round}")
        self.question_lbl.setText(f"Question: {question}")
        self.answer_lbl.setText(answer)

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = AppWindow()
    myApp.show()
    sys.exit(app.exec())