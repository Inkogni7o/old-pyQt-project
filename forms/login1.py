# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_wndw(object):
    def setupUi(self, login_wndw):
        login_wndw.setObjectName("login_wndw")
        login_wndw.resize(432, 241)

        self.welcome = QtWidgets.QLabel(login_wndw)
        self.welcome.setGeometry(QtCore.QRect(140, 10, 181, 21))
        self.welcome.setObjectName("welcome")

        self.login_label = QtWidgets.QLabel(login_wndw)
        self.login_label.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.login_label.setObjectName("login_label")

        self.password_label = QtWidgets.QLabel(login_wndw)
        self.password_label.setGeometry(QtCore.QRect(20, 100, 55, 16))
        self.password_label.setObjectName("password_label")

        self.login_input = QtWidgets.QLineEdit(login_wndw)
        self.login_input.setGeometry(QtCore.QRect(90, 60, 241, 22))
        self.login_input.setObjectName("login_input")

        self.password_input = QtWidgets.QLineEdit(login_wndw)
        self.password_input.setGeometry(QtCore.QRect(90, 100, 241, 22))
        self.password_input.setObjectName("password_input")

        self.label = QtWidgets.QLabel(login_wndw)
        self.label.setGeometry(QtCore.QRect(20, 190, 151, 21))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(login_wndw)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 151, 28))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(login_wndw)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(login_wndw)
        QtCore.QMetaObject.connectSlotsByName(login_wndw)

    def retranslateUi(self, login_wndw):
        _translate = QtCore.QCoreApplication.translate
        login_wndw.setWindowTitle(_translate("login_wndw", "Form"))
        self.welcome.setText(_translate("login_wndw", "Добро пожаловать!"))
        self.login_label.setText(_translate("login_wndw", "Логин:"))
        self.password_label.setText(_translate("login_wndw", "Пароль:"))
        self.label.setText(_translate("login_wndw", "Впервые с нами?"))
        self.pushButton.setText(_translate("login_wndw", "Зарегестрироваться!"))
        self.pushButton_2.setText(_translate("login_wndw", "Войти"))
