# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 601, 551))
        self.groupBox.setObjectName("groupBox")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBox)
        self.webEngineView.setGeometry(QtCore.QRect(10, 20, 581, 521))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 0, 351, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(290, 20, 51, 31))
        self.pushButton.setObjectName("pushButton")
        # self.listView = QtWidgets.QListView(self.groupBox_2)
        # self.listView.setGeometry(QtCore.QRect(10, 60, 331, 192))
        # self.listView.setObjectName("listView")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 331, 192))
        self.listWidget.setDragEnabled(True)
        self.listWidget.setObjectName("listWidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(610, 270, 351, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
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
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
