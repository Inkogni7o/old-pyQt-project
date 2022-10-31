from PyQt5.QtWidgets import QWidget
from forms.login1 import Ui_login_wndw
from registration import RegWindow


class LogWindow(QWidget, Ui_login_wndw):
    def __init__(self):
        super(LogWindow, self).__init__()
        self.setupUi(self)

        self.initUI()

    def initUI(self):
        self.setFixedSize(430, 240)
        self.pushButton.clicked.connect(self.registration)

    def registration(self):
        self.close()
        self.reg = RegWindow()
        self.reg.show()



