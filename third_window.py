from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QDialog, QDialogButtonBox
from PyQt6.QtGui import QDoubleValidator
from pyqtgraph import VerticalLabel
from dijkstra_algorithm import dijsktra
from ui_third_window import Ui_Form
import sys


class ThirdWindow(QWidget, Ui_Form):
    def __init__(self, names, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.names = names
        n = len(names)

        self.calc_btn.clicked.connect(self.calculate)
        
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().hide()

        lable = VerticalLabel('Source')
        self.src_widget.layout().addWidget(lable)

        self.table.setRowCount(n +1)
        self.table.setColumnCount(n +1)

        v_group_box = QGroupBox()
        h_group_box = QGroupBox()

        v_group_box.setLayout(QVBoxLayout())
        h_group_box.setLayout(QHBoxLayout())

        self.table.setCellWidget(1, 0, v_group_box)
        self.table.setCellWidget(0, 1, h_group_box)

        self.table.setSpan(1, 0, n, 1)
        self.table.setSpan(0, 1, 1, n)

        for i in range(n +1):
            for j in range(n +1):
                widget = None
                if i == 0 and j == 0:
                    continue
                elif i == 0 or j == 0:
                    name = names[j-1 if i == 0 else i-1]
                    widget = QRadioButton(name)
                    if i == 0:
                        v_group_box.layout().addWidget(widget)
                    else:
                        h_group_box.layout().addWidget(widget)
                else:
                    widget = QLineEdit()
                    widget.setPlaceholderText('∞')
                    validator = QDoubleValidator()
                    validator.setRange(0, sys.float_info.max)
                    widget.setValidator(validator)
                    if i == j:
                        widget.setPlaceholderText('0')
                        widget.setEnabled(False)

                    self.table.setCellWidget(i, j, widget)

        for i in range(1, n+1):
            for j in range(1, n+1):
                le1 : QLineEdit = self.table.cellWidget(i, j)
                le2 : QLineEdit = self.table.cellWidget(j, i)

                le1.textChanged.connect(le2.setText)
                le2.textChanged.connect(le1.setText)


    def calculate(self):
        n = len(self.names)

        src = None
        dest = None

        layout = self.table.cellWidget(1, 0).layout()
        for i in range(layout.count()):
            rb: QRadioButton = layout.itemAt(i).widget()
            if rb.isChecked(): src = rb.text()

        layout = self.table.cellWidget(0, 1).layout()
        for i in range(layout.count()):
            rb: QRadioButton = layout.itemAt(i).widget()
            if rb.isChecked(): dest = rb.text()
        
        if src is None or dest is None:
            self.warning_dialog('Please select Source and Destination first')
            return

        graph = {}
        for i in range(1, n+1):
            temp = {}
            for j in range(1, n+1):
                if i == j:
                    continue
                else:
                    le: QLineEdit = self.table.cellWidget(i, j)
                    txt = le.text()
                    val = sys.maxsize if len(txt) == 0 else int(txt)
                    temp[self.names[j - 1]] = val
            
            graph[self.names[i - 1]] = temp

        path, cost = dijsktra(graph, src, dest)

        self.path.setText(str(path))
        self.cost.setText(str(cost))
        

    def warning_dialog(self, text):
        dialog = QDialog()
        dialog.setWindowTitle("Warinign!!!")

        btn = QDialogButtonBox.StandardButton.Ok

        buttonBox = QDialogButtonBox(btn)
        buttonBox.accepted.connect(dialog.accept)

        layout = QVBoxLayout()
        message = QLabel(text)
        layout.addWidget(message)
        layout.addWidget(buttonBox)
        dialog.setLayout(layout)

        dialog.exec()