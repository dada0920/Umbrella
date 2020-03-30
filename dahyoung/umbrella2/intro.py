import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
import re
import datetime
from UI.main_ui2 import Ui_MainWindow
import pytube
from threading import Thread
from PyQt5.QtCore import *
import subprocess


class TestForm(QMainWindow, Ui_MainWindow) :
    #생성자
    def __init__(self) :
        super().__init__() #부모의 생성자 함수 호출
        self.url= "http://localhost:8080/umbrella"
        self.setupUi(self)  # 초기화
        self.webEngineView.load(QUrl(self.url))
        self.pushButton.clicked.connect(self.aaa)
        self.load.clicked.connect(self.daum_load)
    def aaa(self) :
        url = self.lineEdit.text().strip()
        print('aaaaaaaa')
        self.webEngineView.load(QUrl(url))
    def daum_load(self) :
        url="https://map.kakao.com/?eX=523953&eY=1084098&eName=%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8C%90%EA%B5%90%EC%98%A4%ED%94%BC%EC%8A%A4"
        print('load')
        self.webEngineView.load(QUrl(url))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
