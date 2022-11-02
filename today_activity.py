# -*- coding: UTF-8 -*-
import datetime as dt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow
from forms.today_formUI import Ui_MainWindow
from new_group import NewGroupWindow


class TodayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, login):
        self.decode_days = {
            1: 'Понедельник', 2: 'Вторник',
            3: 'Среда', 4: 'Четверг',
            5: 'Пятница', 6: 'Суббота',
            7: 'Воскресенье'
        }
        self.login, self.today = login, (dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day)
        super(TodayWindow, self).__init__()
        self.setupUi(self)
        self.add_group.triggered.connect(self.add_new_group)
        self.calendar.setSelectedDate(QDate(*self.today))

    def add_new_group(self):
        wndw = NewGroupWindow(self.login)
        wndw.show()

