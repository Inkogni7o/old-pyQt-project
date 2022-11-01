# -*- coding: UTF-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from forms.add_groupUI import Ui_Form


class NewGroupWindow(QWidget, Ui_Form):
    def __init__(self):
        super(NewGroupWindow, self).__init__()
        self.setupUi(self)
        self.buttonBox.rejected.connect(lambda: self.close())
        self.buttonBox.accepted.connect(self.new_group)

        lst = [self.monday, self.tuesday, self.wendsday, self.thursday, self.friday, self.saturday, self.sunday]
        for word in lst:
            word.clicked.connect(self.open_time)

        self.main_dict = {
            'Понедельник': (self.time_edit_1, self.end_edit_1),
            'Вторник': (self.time_edit_2, self.end_edit_2),
            'Среда': (self.time_edit_3, self.end_edit_3),
            'Четверг': (self.time_edit_4, self.end_edit_4),
            'Пятница': (self.time_edit_5, self.end_edit_5),
            'Суббота': (self.time_edit_6, self.end_edit_6),
            'Воскресенье': (self.time_edit_7, self.end_edit_7)
        }

    def open_time(self):
        if self.main_dict[self.sender().text()][0].isEnabled() == 0:
            self.main_dict[self.sender().text()][0].setEnabled(True)
            self.main_dict[self.sender().text()][1].setEnabled(True)
        else:
            self.main_dict[self.sender().text()][0].setEnabled(False)
            self.main_dict[self.sender().text()][1].setEnabled(False)

    def new_group(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = NewGroupWindow()
    main_app.show()
    sys.exit(app.exec_())