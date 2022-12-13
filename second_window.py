from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6.QtCore import Qt, pyqtSignal

from ui_second_window import Ui_Form


class SecondWindow(QWidget, Ui_Form):
    
    done = pyqtSignal(list)


    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.scroll_layout = self.scrollAreaWidgetContents.layout()

        for i in range(n):
            le = QLineEdit()
            le.setPlaceholderText(f'Node Name ({i + 1})')
            le.textChanged.connect(self.activate_btn)
            self.scroll_layout.addWidget(le, 0, Qt.AlignmentFlag.AlignHCenter)
        
        self.next_btn.clicked.connect(self.next_btn_cliked)

    def activate_btn(self,_):
        enabled = True
        for i in range(self.scroll_layout.count()):
            le = self.scroll_layout.itemAt(i).widget()
            enabled &= len(le.text().strip()) != 0
        self.next_btn.setEnabled(enabled)


    def next_btn_cliked(self):
        node_names = []

        for i in range(self.scroll_layout.count()):
            le = self.scroll_layout.itemAt(i).widget()
            node_names.append(le.text().strip())

        self.done.emit(node_names)