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

    def new_group(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = NewGroupWindow()
    main_app.show()
    sys.exit(app.exec_())