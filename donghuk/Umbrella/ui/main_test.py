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
        MainWindow.resize(1080, 854)
        MainWindow.setMinimumSize(QSize(920, 820))
        MainWindow.setMaximumSize(QSize(920, 820))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 921, 630))
        self.frame.setStyleSheet("background-color : #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame)
        self.webEngineView.setGeometry(QtCore.QRect(-1, 0, 921, 601))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
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
        self.radio1 = QtWidgets.QRadioButton(self.frame)
        self.radio1.setGeometry(QtCore.QRect(600, 600, 71, 31))
        self.radio1.setObjectName("radio2")
        self.radio2 = QtWidgets.QRadioButton(self.frame)
        self.radio2.setGeometry(QtCore.QRect(670, 600, 71, 31))
        self.radio2.setObjectName("radio2")
        self.radio3 = QtWidgets.QRadioButton(self.frame)
        self.radio3.setGeometry(QtCore.QRect(750, 600, 71, 31))
        self.radio3.setObjectName("radio3")
        self.radio4 = QtWidgets.QRadioButton(self.frame)
        self.radio4.setGeometry(QtCore.QRect(830, 600, 81, 31))
        self.radio4.setObjectName("radio4")
        self.listWidget = QtWidgets.QListWidget(MainWindow)
        self.listWidget.setGeometry(QtCore.QRect(0, 630, 921, 171))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.pushButton2.setText(_translate("MainWindow", "판매처 탐색"))
        self.pushButton3.setText(_translate("MainWindow", "내 위치"))
        self.radio1.setText(_translate("MainWindow", "전체"))
        self.radio2.setText(_translate("MainWindow", "1개 ↑"))
        self.radio3.setText(_translate("MainWindow", "30개 ↑"))
        self.radio4.setText(_translate("MainWindow", "100개 ↑"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
