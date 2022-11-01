# -*- coding: UTF-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from login import LogWindow
from registration import RegWindow


class MainFrom(QWidget):
    def __init__(self):
        super(MainFrom, self).__init__()
        self.login = LogWindow()
        self.login.show()
        self.login.pushButton.clicked.connect(self.to_registration)

    def to_registration(self):
        self.reg = RegWindow()
        self.reg.lets_begin_btn.clicked.connect(self.to_login)
        self.reg.show()
        self.login.close()

    def to_login(self):
        self.reg.close()
        self.login = LogWindow()
        self.login.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainFrom()
    sys.exit(app.exec_())
