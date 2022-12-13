import sys

from main_window import MainWindow
from PyQt6.QtWidgets import QApplication


app = QApplication(sys.argv)

win = MainWindow()

win.show()

app.exec()
