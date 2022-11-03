# -*- coding: UTF-8 -*-
import datetime as dt
import sqlite3
import sys

from PyQt5.QtCore import QDate

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView
from forms.today_formUI import Ui_MainWindow
from new_group import NewGroupWindow
from consts import DECODE_DAYS
from edit_group import EditGroupWindow


class TodayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, login: str):
        self.login, self.today = login, (dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day)
        super(TodayWindow, self).__init__()
        self.setupUi(self)
        self.add_group.triggered.connect(self.add_new_group)
        self.calendar.setSelectedDate(QDate(*self.today))
        self.display_groups()
        self.calendar.clicked.connect(self.display_groups)

    def display_groups(self):
        with sqlite3.connect('main_db.db') as con:
            day_of_the_week = DECODE_DAYS[self.calendar.selectedDate().dayOfWeek()]
            cur = con.cursor()
            self.result = cur.execute("""SELECT title, days_of_the_week, starts, ends, id FROM groups
             WHERE days_of_the_week LIKE ?""", ('%' + day_of_the_week + '%',)).fetchall()
        for group in self.result:
            self.today_groups.setRowCount(len(self.result))
            self.today_groups.setItem(self.result.index(group), 0, QTableWidgetItem(group[0]))
            time = QTableWidgetItem(group[2].split()[group[1].split().index(day_of_the_week)] + ' - '
                                    + group[3].split()[group[1].split().index(day_of_the_week)])
            self.today_groups.setItem(self.result.index(group), 1, time)
            self.today_groups.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.today_groups.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.today_groups.scrollToItem(time)
        self.today_groups.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                event.buttons() == QtCore.Qt.LeftButton and
                source is self.today_groups.viewport()):
            item = self.today_groups.itemAt(event.pos())
            self.edit_group = EditGroupWindow(self.result[-1])
            self.close()
            self.edit_group.show()
        return super(TodayWindow, self).eventFilter(source, event)

    def add_new_group(self):
        wndw = NewGroupWindow(self.login)
        wndw.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = TodayWindow('Логин')
    main_app.show()
    sys.exit(app.exec_())
