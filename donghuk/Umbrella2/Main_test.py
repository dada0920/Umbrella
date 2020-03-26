import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from ui.main_ui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from ScriptRunner import Runner
import requests
import json
class Umbrella(QMainWindow, Ui_MainWindow) :
    #생성자
    def __init__(self) :
        super().__init__()
        self.init_my_location()
        self.setupUi(self)  # 초기화
        # self.url = "http://localhost:8080/umbrella"
        self.url = "http://localhost:8000/umbrella2.html"
        self.webEngineView.load(QUrl(self.url))
        self.page = QWebEnginePage()
        self.page.setUrl(QUrl(self.url))
        self.page.setView(self.webEngineView)

        chrome_option = Options()
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--mute-audio")
        self.browser = webdriver.Chrome(chrome_options=chrome_option, executable_path="webdriver/Chrome/chromedriver.exe")
        self.browser.get(self.url)

        self.runner = Runner(self.page, self.browser)
        self.comboBox.addItem("키워드")
        self.comboBox.addItem("주소")

        # self.page.featurePermissionRequested.connect(self.setPagePermission)


        # self.pushButton.clicked.connect(self.map_removeMarkers)

        # self.pushButton.clicked.connect(lambda: self.map_setLevel(random.randrange(7)))
        self.pushButton.clicked.connect(lambda: self.runner.coord_to_address(self.my_location_lat,self.my_location_lng, random.randrange(0,5)))
        # self.pushButton.clicked.connect(lambda: self.getDistance([33.450500,126.569968],[[33.450500,126.569968],[35.404195,126.886323],[39.668777,126.065913]]))
        # self.pushButton.clicked.connect(self.test_a)
        # self.pushButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(self.runner.search)
        self.page.loadFinished.connect(lambda: self.runner.setMap(self.my_location_lat, self.my_location_lng))
        # self.setMap(self.my_location_lat, self.my_location_lng)










    def init_my_location(self) :
        url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDQKxbTt0MrFNH85kTJXzickMD5s88UVaI'
        data = {
            'considerIp': True,
        }

        result = requests.post(url, data)

        my_location = json.loads(result.text)
        # print(my_location)
        # print("lat : ",my_location.get('location').get('lat'))
        # print("lon : ",my_location.get('location').get('lng'))
        self.my_location_lat = str(my_location.get('location').get('lat'))
        self.my_location_lng = str(my_location.get('location').get('lng'))




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Umbrella()
    window.show()
    app.exec_()
    window.browser.close()
    window.browser.quit()

    # print(f'{lat}\n{lng}')
    pass
