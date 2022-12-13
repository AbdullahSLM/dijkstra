from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt
import typing

from first_window import FirstWindow
from second_window import SecondWindow
from third_window import ThirdWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dijkstra Algorithm')
        

        self.first_window = FirstWindow()
        # self.first_window = ThirdWindow(['A', 'B', 'C'])

        self.first_window.done.connect(self.to_second_window)

        self.setCentralWidget(self.first_window)


    def to_second_window(self, n):
        self.second_window = SecondWindow(n)
        self.second_window.done.connect(self.to_third_window)

        self.setCentralWidget(self.second_window) 

            
    def to_third_window(self, names):
        self.third_window = ThirdWindow(names)
        self.setCentralWidget(self.third_window) 