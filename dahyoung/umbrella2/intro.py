import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
import re
import datetime
from ui.main_ui2 import Ui_MainWindow
import pytube
from threading import Thread
from PyQt5.QtCore import *
import subprocess


class TestForm(QMainWindow, Ui_MainWindow) :
    #생성자
    def __init__(self) :
        super().__init__() #부모의 생성자 함수 호출
        self.pushButton.clicked.connect(self.aaa)
        self.load.clicked.connect(self.daum_load)

    def aaa(self) :

        print('aaaaaaaa')
        self.webEngineView.load(QUrl(url))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
