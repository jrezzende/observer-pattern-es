import sys

from twisted.internet import task, reactor
from PySide2.QtWidgets import QApplication

from view import Widget, RepeatedTimer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #cria interface
    window = Widget()
    window.resize(450, 200)
    window.show()
    #inicia o timer que executará a função de gerar clima aleatório de 3 em 3 segundos
    rt = RepeatedTimer(3, window.observer.randomize_weather)

    sys.exit(app.exec_())