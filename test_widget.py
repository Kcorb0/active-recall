import sys
import random as rd
from PySide6 import QtCore, QtWidgets, QtGui

from get_questions import get_questions


class GameWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.questions = get_questions("Machine Learning")
        self.q_num = 0

        # Question and answers text
        self.question_lbl = QtWidgets.QLabel(self.questions[self.q_num][1], alignment=QtCore.Qt.AlignCenter)
        self.question_lbl.setWordWrap(True)
        self.answer_lbl = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)
        self.answer_lbl.setWordWrap(True)

        # Users answer
        self.answer_input = QtWidgets.QLineEdit()
        
        # Show answers and next question buttons
        self.show_btn = QtWidgets.QPushButton("Show Answers")
        self.show_btn.clicked.connect(self.show_ans)
        self.next_btn = QtWidgets.QPushButton("Next Question")
        self.next_btn.clicked.connect(self.nextq)

        # Draw widgets to layout widget
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.question_lbl)
        self.layout.addWidget(self.answer_lbl)
        self.layout.addWidget(self.answer_input)
        self.layout.addWidget(self.show_btn)
        self.layout.addWidget(self.next_btn)


    @QtCore.Slot()
    def nextq(self):

        if self.q_num < len(self.questions)-1:
            self.q_num += 1
        else:
            self.q_num = 0

        self.question_lbl.setText(self.questions[self.q_num][1])
        self.answer_lbl.setText("")
        self.answer_input .setText("")
    
    @QtCore.Slot()
    def show_ans(self):
        self.answer_lbl.setText(self.questions[self.q_num][2])

    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = GameWidget()
    widget.resize(900, 600)
    widget.show()

    sys.exit(app.exec())