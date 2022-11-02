# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import QMainWindow
from forms.today_formUI import Ui_MainWindow
from new_group import NewGroupWindow


class TodayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, login):
        self.login = login
        super(TodayWindow, self).__init__()
        self.setupUi(self)
        self.add_group.triggered.connect(self.add_new_group)

    def add_new_group(self):
        wndw = NewGroupWindow(self.login)
        wndw.show()

