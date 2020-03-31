import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
import re
import datetime
# from ui.main_ui import Ui_MainWindow
from ui.main_ui5 import Ui_MainWindow
import pytube
from threading import Thread
from PyQt5.QtCore import *
import subprocess
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import json
import os
import requests
import marker3
from PyQt5.QtPositioning import *

class TestForm(QMainWindow, Ui_MainWindow) :
    #생성자
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  # 초기화
        self.url = QUrl("http://localhost:8080/umbrella")
        self.webEngineView.load(QUrl(self.url))
        self.page = QWebEnginePage()
        self.page.setUrl(self.url)
        self.page.setView(self.webEngineView)
        self.pushButton_3.clicked.connect(self.translate_ui)



    def translate_ui(self) :

        print('aaaaaaaa')
        self.stackedWidget.setCurrentIndex(1)








if __name__ == "__main__" :
        app = QApplication(sys.argv)
        window = TestForm()
        window.show()
        app.exec_()
        window.browser.close()
        window.browser.quit()
