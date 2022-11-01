# -*- coding: UTF-8 -*-
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from login import LogWindow
from registration import RegWindow


class MainFrom(QWidget):
    def __init__(self):
        super(MainFrom, self).__init__()
        self.login = LogWindow()
        self.login.show()
        self.login.register_btn.clicked.connect(self.to_registration)
        self.login.login_btn.clicked.connect(self.login_user)

    def to_registration(self):
        self.reg = RegWindow()
        self.reg.lets_begin_btn.clicked.connect(self.to_login)
        self.reg.show()
        self.login.close()

    def to_login(self):
        self.reg.close()
        self.login = LogWindow()
        self.login.show()

    def login_user(self):
        with sqlite3.connect('db/main_db.db') as con:
            cur = con.cursor()
            result = cur.execute("""SELECT password FROM users WHERE login=?""", self.login.login_input.text())
            if self.login.password_input.text() in result:
                self.user = self.login.login_input.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainFrom()
    sys.exit(app.exec_())
