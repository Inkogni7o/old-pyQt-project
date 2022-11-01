# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import QMainWindow
from forms.today_form import Ui_MainWindow


class TodayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TodayWindow, self).__init__()
        self.setupUi(self)