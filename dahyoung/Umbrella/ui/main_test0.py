# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 820)
        MainWindow.setMinimumSize(QSize(920, 820))
        MainWindow.setMaximumSize(QSize(920, 820))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 920, 820))
        self.stackedWidget.setObjectName("stackedWidget")

        #page1
        #Intro_frame
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.intro_frame = QtWidgets.QFrame(self.page)
        self.intro_frame.setGeometry(QtCore.QRect(0, 0, 920, 820))
        self.intro_frame.setStyleSheet("background-color : #000000")
        self.intro_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.intro_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.intro_frame.setObjectName("intro_frame")

        self.widget_main = QtWidgets.QWidget(self.intro_frame)
        self.widget_main.setGeometry(QtCore.QRect(20, 480, 420, 250))
        self.widget_main.setObjectName("widget_main")
        self.widget_1 = QtWidgets.QWidget(self.widget_main)
        self.widget_1.setGeometry(QtCore.QRect(0, 0, 210, 125))
        self.widget_1.setStyleSheet("background-color : #ff0000")
        self.widget_1.setObjectName("widget_1")
        self.widget_2 = QtWidgets.QWidget(self.widget_main)
        self.widget_2.setGeometry(QtCore.QRect(210, 0, 210, 125))
        self.widget_2.setStyleSheet("background-color : #0000ff")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_main)
        self.widget_3.setGeometry(QtCore.QRect(0, 125, 210, 125))
        self.widget_3.setStyleSheet("background-color : #ff8c00")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_main)
        self.widget_4.setGeometry(QtCore.QRect(210, 125, 210, 125))
        self.widget_4.setStyleSheet("background-color : #808080")
        self.widget_4.setObjectName("widget_4")


        # self.listView_3 = QtWidgets.QListView(self.intro_frame)
        # self.listView_3.setGeometry(QtCore.QRect(20, 480, 420, 251))
        # self.listView_3.setStyleSheet("background-color : #ffffff")
        # self.listView_3.setObjectName("listView_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.intro_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 0, 601, 431))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Umbrella/dahyoung/umbrella2/log/umbrella5.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(600, 600))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_graph = QtWidgets.QWidget(self.intro_frame)
        self.widget_graph.setGeometry(QtCore.QRect(460, 480, 420, 251))
        self.widget_graph.setStyleSheet("background-color : #ffffff")
        self.widget_graph.setObjectName("listView_5")
        self.stackedWidget.addWidget(self.intro_frame)
        #page2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 921, 630))
        self.frame.setStyleSheet("background-color : #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame)
        self.webEngineView.setGeometry(QtCore.QRect(-1, 0, 921, 601))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")

        #stack1로 돌아가는 버튼
        self.pushButton__image = QtWidgets.QPushButton(self.frame)
        self.pushButton__image.setGeometry(QtCore.QRect(30, 30, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Umbrella/dahyoung/umbrella2/log/umbrella5.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton__image.setIcon(icon)
        self.pushButton__image.setIconSize(QtCore.QSize(30, 30))
        self.pushButton__image.setObjectName("pushButton__image")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 600, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(281, 601, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.frame)
        self.pushButton2.setGeometry(QtCore.QRect(381, 601, 101, 31))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.frame)
        self.pushButton3.setGeometry(QtCore.QRect(481, 601, 101, 31))
        self.pushButton3.setObjectName("pushButton3")
        #1개 미만
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(590, 600, 101, 31))
        self.radioButton.setObjectName("radioButton")
        #30개 미만
        self.radioButton2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton2.setGeometry(QtCore.QRect(700, 600, 111, 31))
        self.radioButton2.setObjectName("radioButton2")
        #100개 미만
        self.radioButton3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton3.setGeometry(QtCore.QRect(810, 600, 111, 31))
        self.radioButton3.setObjectName("radioButton3")
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 630, 921, 171))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.stackedWidget.addWidget(self.page_2)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.pushButton2.setText(_translate("MainWindow", "판매처 탐색"))
        self.pushButton3.setText(_translate("MainWindow", "내 위치"))
        self.radioButton.setText(_translate("MainWindow", "CheckBox"))
        self.radioButton2.setText(_translate("MainWindow", "CheckBox"))
        self.radioButton3.setText(_translate("MainWindow", "CheckBox"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
