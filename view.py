import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.sp_edit = None
        self.flo_edit = None
        self.poa_edit = None

        self.subscribers = set(sp_edit, flo_edit, poa_edit)

        self.setLayout(self._init_layout())

    def _init_layout(self):
        self.flo_edit = QLineEdit("Florianópolis")
        self.poa_edit = QLineEdit("Porto Alegre")
        self.sp_edit = QLineEdit("São Paulo")
        layout = QVBoxLayout()
        layout.addWidget(self.flo_edit)
        layout.addWidget(self.poa_edit)
        layout.addWidget(self.sp_edit)

        