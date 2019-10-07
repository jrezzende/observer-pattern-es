import sys
import random

from threading import Timer
from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import (
    QLineEdit, QApplication, QVBoxLayout, QDialog, QWidget, QLabel)

from data import dataset

class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.flo_label = QLabel("Florianópolis")
        self.poa_label = QLabel("Porto Alegre")
        self.sp_label = QLabel("São Paulo")

        self.flo_label.setAlignment(Qt.AlignCenter)
        self.poa_label.setAlignment(Qt.AlignCenter)
        self.sp_label.setAlignment(Qt.AlignCenter)

        self.edits = self._register_edits()
        self.setLayout(self._init_layout())
        

    def _register_edits(self):
        edits = {
            'Florianópolis': self.flo_label,
            'Porto Alegre': self.poa_label,
            'São Paulo': self.sp_label
        }
        return edits

    def _init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.flo_label)
        layout.addWidget(self.poa_label)
        layout.addWidget(self.sp_label)
        return layout

    def randomize_weather(self):
        opts = ['Florianópolis', 'Porto Alegre', 'São Paulo']
        random_loc = random.choice(opts)
        edit = self.edits.get(random_loc)
        random_weather = random.choice(dataset.get(random_loc))
        edit.setText(
            f'{random_loc}, Temperatura: {random_weather[0]}, Precipitação: {random_weather[1]}, Umidade: {random_weather[2]}, Vento: {random_weather[3]}')


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False