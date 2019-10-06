# import random

# from data import dataset

# def random_opt():
#     opt = ['Florianópolis', 'Porto Alegre', 'São Paulo']
#     random_opt = random.choice(opt)
#     print(random_opt)
#     print(random.choice(dataset.get(random_opt)))

# random_opt()
import sys
from view import Form
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())