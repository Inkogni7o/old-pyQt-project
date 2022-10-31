from PyQt5.QtWidgets import QWidget
from forms.reg import Ui_Form


class RegWindow(QWidget, Ui_Form):
    def __init__(self):
        super(RegWindow, self).__init__()
        self.setupUi(self)