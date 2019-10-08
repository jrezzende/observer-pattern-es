import sys
import random

from threading import Timer
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QFont
from PySide2.QtWidgets import (
    QLineEdit, QApplication, QVBoxLayout, QDialog, QWidget, QLabel)

from data import dataset

#classe que fornecerá uma interface para o programa, similar a um swing em java só que melhor        muito melhor
class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.subject = Subject()

        #cria observers
        self.flo_label = ObserverLabel("Florianópolis")
        self.poa_label = ObserverLabel("Porto Alegre")
        self.sp_label = ObserverLabel("São Paulo")

        #adiciona observers ao subject
        self.subject.register_observers(self.flo_label, self.poa_label, self.sp_label)

        self.flo_label.setAlignment(Qt.AlignCenter)
        self.poa_label.setAlignment(Qt.AlignCenter)
        self.sp_label.setAlignment(Qt.AlignCenter)

        self.setLayout(self._init_layout())

    def _init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.flo_label)
        layout.addWidget(self.poa_label)
        layout.addWidget(self.sp_label)
        return layout

#classe subject, contém um conjunto de observers
class Subject():
    def __init__(self):
        self.observers = set()

    def register_observers(self, *observers):
        if not observers:
            return
        #percorre uma lista de argumentos, onde adicionamos cada observers ao subject
        for obs in observers:
            self.observers.add(obs)
    
    def unregister_all(self):
        self.observers.clear()

    #dispara a mensagem a todos os observers (location é uma string, Florianópolis, Porto Alegre ou São Paulo, que decidirá qual label será alterada)
    def notify_observers(self, location, message):
        if not self.observers:
            return
        #para cara observer em observers, verificar se a localização (floripa, sp, poa) bate com o da mensagem enviada e enviar um update para o label observer
        for obs in self.observers:
            if location == obs.name:
                obs.update(message)

    #função para gerar estados de clima aleatórios
    def randomize_weather(self):
        #lista de possibilidades (labels) a serem alteradas
        opts = ['Florianópolis', 'Porto Alegre', 'São Paulo']
        #escolhe uma localização aleatória
        random_loc = random.choice(opts)
        #escolhe um clima aleatório baseado na localização acima
        random_weather = random.choice(dataset.get(random_loc))
        #envia mensagem contendo novo estado de clima aleatorio
        return self.notify_observers(random_loc, random_weather)

#observer é uma label, que ficará na interface gráfica mostrando estados de clima aleatório
class ObserverLabel(QLabel):
    def __init__(self, name, parent=None):
        super(ObserverLabel, self).__init__(parent)
        self.name = name
        self._apply_initial_status()
    
    def _apply_initial_status(self):
        font = QFont('Times', 24, QFont.Bold)
        self.setFont(font)

        random_weather = random.choice(dataset.get(self.name))
        self.setText(
            f'{self.name}, Temperatura: {random_weather[0]}, Precipitação: {random_weather[1]}, Umidade: {random_weather[2]}, Vento: {random_weather[3]}'
        )
    #caso receba uma mensagem, printa no cmd que recebeu uma atualização e atualiza seu texto na interface grafica
    def update(self, message):
        print(f'{self.name} got an update!')
        self.setText(
            f'{self.name}, Temperatura: {message[0]}, Precipitação: {message[1]}, Umidade: {message[2]}, Vento: {message[3]}'
        )

#timer para executar função que gera clima aleatório em intervalos de tempo
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
