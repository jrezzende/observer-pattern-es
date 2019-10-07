import sys

from twisted.internet import task, reactor
from PySide2.QtWidgets import QApplication

from view import Widget, RepeatedTimer

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Widget()
    window.resize(450, 200)
    window.show()

    rt = RepeatedTimer(3, window.randomize_weather)

    sys.exit(app.exec_())