# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os
import datetime
from dbHelper import DBHelper
from time import time, sleep
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, username = "User"):
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_web = QtWidgets.QLabel(self.centralwidget)
        self.lbl_web.setGeometry(QtCore.QRect(70, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_web.setFont(font)
        self.lbl_web.setObjectName("lbl_web")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 100, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_crawl = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crawl.setGeometry(QtCore.QRect(190, 100, 86, 30))
        self.btn_crawl.setObjectName("btn_crawl")
        self.lbl_fliter = QtWidgets.QLabel(self.centralwidget)
        self.lbl_fliter.setGeometry(QtCore.QRect(430, 70, 41, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_fliter.setFont(font)
        self.lbl_fliter.setObjectName("lbl_fliter")
        self.conditionEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.conditionEdit.setGeometry(QtCore.QRect(310, 100, 291, 30))
        self.conditionEdit.setObjectName("conditionEdit")
        self.btn_query = QtWidgets.QPushButton(self.centralwidget)
        self.btn_query.setGeometry(QtCore.QRect(620, 100, 86, 30))
        self.btn_query.setAccessibleName("")
        self.btn_query.setObjectName("btn_query")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(710, 100, 86, 30))
        self.btn_delete.setObjectName("btn_delete")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(29, 179, 741, 361))
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 726, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(-5, -9, 751, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_crawl.clicked.connect(lambda: self.btn_crawl_clicked(MainWindow))
        self.btn_query.clicked.connect(self.btn_query_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # MainWindow.setStatusTip(_translate("MainWindow", "User , Welcome :  )"))
        self.default_statusbar_style(MainWindow)
        self.lbl_web.setText(_translate("MainWindow", "网站选择"))
        self.comboBox.setItemText(0, _translate("MainWindow", "豆瓣"))
        self.comboBox.setItemText(1, _translate("MainWindow", "安居客"))
        self.btn_crawl.setStatusTip(_translate("MainWindow", "Crawl the website"))
        self.btn_crawl.setText(_translate("MainWindow", "爬取"))
        self.lbl_fliter.setText(_translate("MainWindow", "fliter"))
        self.btn_query.setStatusTip(_translate("MainWindow", "Query by your statment"))
        self.btn_query.setText(_translate("MainWindow", "查询"))
        self.btn_delete.setStatusTip(_translate("MainWindow", "Delete data by your statment"))
        self.btn_delete.setText(_translate("MainWindow", "删除"))

    def default_statusbar_style(self, MainWindow):
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        statment = '[ ' + str(nowTime) + '] ' + self.username + ', Welcome :  )'
        MainWindow.setStatusTip(statment)

    def btn_crawl_clicked(self, MainWindow):
        os.chdir("/home/guixuan/Documents/py/Python-spyder/doubanbook/doubanbook")
        print("Running at --->:  "+os.getcwd())

        t1 = time()
        if self.comboBox.currentText() == "豆瓣":
            MainWindow.setStatusTip("Crawling the douban website")
            r = os.system("scrapy crawl dbbook")              
        else:
            MainWindow.setStatusTip("Crawling the anjuke website")
            r = os.system("scrapy crawl fangtianxia")

        t2 = time()

        print("Spider exit with code: " + str(r))
        s = "Finish crawling, Used time: " + str(int(t2 - t1)) + " s"
        MainWindow.setStatusTip(s) 
        

    def btn_query_clicked(self):
        condition = self.conditionEdit.text()
        dbname = "dbbook" if self.comboBox.currentText() == "豆瓣" else "Fang"
        db = DBHelper()

        rows = db.Query_by_condition(dbname, condition)

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(4 if dbname == 'dbbook' else 6)

        if dbname == 'dbbook':
            self.tableWidget.setHorizontalHeaderLabels(['num','title','author','rate'])

            for row, i in zip(rows, range(self.tableWidget.rowCount())):
                for column, j in zip(row, range(self.tableWidget.columnCount())):
                    newItem = QtWidgets.QTableWidgetItem(str(column))
                    self.tableWidget.setItem(i,j,newItem)

        else:
            self.tableWidget.setHorizontalHeaderLabels(['num', 'describtion', 'structure', 
                                                        'areasize', 'selling_price', 'address'])

            for row, i in zip(rows, range(self.tableWidget.rowCount())):
                for column, j in zip(row, range(self.tableWidget.columnCount())):
                    newItem = QtWidgets.QTableWidgetItem(str(column))
                    self.tableWidget.setItem(i, j, newItem)


    def btn_delete_clicked(self):
        condition = self.conditionEdit.text()
        dbname = "dbbook" if self.comboBox.currentText() == "豆瓣" else "Fang"

        db = DBHelper()
        result = db.Delete_by_condition(dbname, condition)

        if not result:
            QtWidgets.QMessageBox.warning(self.btn_delete, "提示", '删除失败或未输入条件')
        else:
            QtWidgets.QMessageBox.information(self.btn_delete, "提示", '删除成功')