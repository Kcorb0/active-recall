import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
# from app_gui import Ui_MainWindow



class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/ar_gui.ui', self)
        self.setWindowTitle("Active Recall")
        self.content_widget.setCurrentIndex(0)

        self.start_btn.clicked.connect(self.game_pg)
        self.begin_btn.clicked.connect(self.play_pg)
        self.add_btn.clicked.connect(self.create_pg)
        self.view_questions_btn.clicked.connect(self.see_questions_pg)
        self.analytics_btn.clicked.connect(self.view_graph_pg)

    
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
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = AppWindow()
    myApp.show()
    sys.exit(app.exec())