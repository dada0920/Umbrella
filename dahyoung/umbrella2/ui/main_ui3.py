# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 20, 991, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(310, 30, 341, 221))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../resource/Umbrella.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.listView_3 = QtWidgets.QListView(self.page)
        self.listView_3.setGeometry(QtCore.QRect(330, 250, 311, 192))
        self.listView_3.setObjectName("listView_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 500, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 601, 551))
        self.groupBox.setObjectName("groupBox")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBox)
        self.webEngineView.setGeometry(QtCore.QRect(10, 20, 581, 521))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_2.setGeometry(QtCore.QRect(630, 20, 351, 551))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 40, 51, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView_2 = QtWidgets.QListView(self.groupBox_2)
        self.listView_2.setGeometry(QtCore.QRect(10, 150, 331, 381))
        self.listView_2.setObjectName("listView_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 56, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 56, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 56, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 100, 191, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.groupBox.setTitle(_translate("MainWindow", "지도"))
        self.groupBox_2.setTitle(_translate("MainWindow", "검색"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">반경</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">잔량</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">약국 이름</p></body></html>"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
