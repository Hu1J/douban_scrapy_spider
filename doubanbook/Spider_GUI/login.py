# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from MainWin import Ui_MainWindow
from dbHelper import DBHelper
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(529, 391)
        self.center(Login)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.lbl_username = QtWidgets.QLabel(Login)
        self.lbl_username.setGeometry(QtCore.QRect(130, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.lbl_password = QtWidgets.QLabel(Login)
        self.lbl_password.setGeometry(QtCore.QRect(130, 250, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.passEdit = QtWidgets.QLineEdit(Login)
        self.passEdit.setGeometry(QtCore.QRect(190, 250, 191, 30))
        self.passEdit.setObjectName("passEdit")
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lbl_pic = QtWidgets.QLabel(Login)
        self.lbl_pic.setGeometry(QtCore.QRect(-10, 0, 551, 181))
        self.lbl_pic.setText("")
        self.lbl_pic.setPixmap(QtGui.QPixmap("imgs/login_pic.png"))
        self.lbl_pic.setScaledContents(True)
        self.lbl_pic.setObjectName("lbl_pic")
        self.btn_login = QtWidgets.QPushButton(Login)
        self.btn_login.setGeometry(QtCore.QRect(125, 320, 101, 41))
        self.btn_login.setObjectName("btn_login")
        self.btn_login.setShortcut("Return")
        self.btn_register = QtWidgets.QPushButton(Login)
        self.btn_register.setGeometry(QtCore.QRect(295, 320, 101, 41))
        self.btn_register.setObjectName("btn_register")
        self.username_Edit = QtWidgets.QLineEdit(Login)
        self.username_Edit.setGeometry(QtCore.QRect(190, 200, 191, 30))
        self.username_Edit.setText("")
        self.username_Edit.setObjectName("username_Edit")
        self.lbl_username.raise_()
        self.lbl_password.raise_()
        self.passEdit.raise_()
        self.btn_login.raise_()
        self.btn_register.raise_()
        self.username_Edit.raise_()
        self.lbl_pic.raise_()

        self.retranslateUi(Login)
        self.btn_login.clicked.connect(lambda: self.btn_login_click(Login)) # 处理切换窗口的关键
        self.btn_register.clicked.connect(self.btn_register_click)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.username_Edit, self.passEdit)
        Login.setTabOrder(self.passEdit, self.btn_login)
        Login.setTabOrder(self.btn_login, self.btn_register)

        self.MWindow = QtWidgets.QMainWindow()
        self.MWinow_UI = Ui_MainWindow()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.lbl_username.setText(_translate("Login", "账号"))
        self.lbl_password.setText(_translate("Login", "密码"))
        self.btn_login.setText(_translate("Login", "登录"))
        self.btn_register.setText(_translate("Login", "注册"))

    def center(self, Form):
        qr = Form.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        Form.move(qr.topLeft())

    def btn_login_click(self, Login):
        user_info = {
            'username': self.username_Edit.text(),
            'password': self.passEdit.text()
        }
        db = DBHelper()
        result = db.Confirm_user(user_info)

        if result:
            QtWidgets.QMessageBox.information(self.btn_login, "提示", '登录成功')
            self.MWinow_UI.setupUi(self.MWindow, user_info['username'])
            self.center(self.MWindow)
            Login.close()
            self.MWindow.show()
        else:
            QtWidgets.QMessageBox.warning(self.btn_login, "提示", '登录失败')


    def btn_register_click(self):
        user_info = {
            'username': self.username_Edit.text(),
            'password': self.passEdit.text()
        }
        db = DBHelper()
        result = db.Regist_user(user_info)

        QtWidgets.QMessageBox.information(self.btn_login, "提示", result)
