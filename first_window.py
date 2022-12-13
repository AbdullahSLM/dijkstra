from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore

from ui_first_window import Ui_Form


class FirstWindow(QWidget, Ui_Form):

    done = QtCore.pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.node_n_le.textChanged.connect(self._node_in_changed)
        self.next_btn.clicked.connect(self._next_btn_clicked)


    def _next_btn_clicked(self):
        n = int(self.node_n_le.text())
        self.done.emit(n)
    

    def _node_in_changed(self, txt):
        self.next_btn.setEnabled(txt.isdigit())