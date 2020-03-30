import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
# from ui.main_ui import Ui_MainWindow
from ui.main_test import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from lib.ScriptRunner import Runner
from lib.DataCollector import DataCollector
from lib.item import Item
import requests
import json
class Umbrella(QMainWindow, Ui_MainWindow) :
    #생성자
    def __init__(self) :
        super().__init__()
        self.init_my_location()
        self.setupUi(self)  # 초기화
        self.url = "http://localhost:8080/umbrella"
        # self.url = "http://localhost:8000/umbrella2.html"
        self.webEngineView.load(QUrl(self.url))
        self.page = QWebEnginePage()
        self.page.setUrl(QUrl(self.url))
        self.page.setView(self.webEngineView)
        self.appLoaded = False
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--mute-audio")
        self.browser = webdriver.Chrome(chrome_options=chrome_option, executable_path="resources/chromedriver.exe")
        self.browser.get(self.url)

        self.runner = Runner(self)
        self.dc = DataCollector()
        # self.comboBox.addItem("키워드")
        # self.comboBox.addItem("주소")
        self.itemList = []
        self.rowList = []
        # self.page.featurePermissionRequested.connect(self.setPagePermission)

        self.pushButton.clicked.connect(self.runner.map_removeMarkers)
        # self.pushButton.clicked.connect(self.map_removeMarkers)
        # self.pushButton.clicked.connect(self.runner.map_getLevel)
        # self.pushButton.clicked.connect(lambda: self.runner.map_setLevel(random.randrange(7)))
        # self.pushButton.clicked.connect(lambda: self.runner.coord_to_address(self.my_location_lat,self.my_location_lng, random.randrange(0,5)))
        # self.pushButton.clicked.connect(lambda: self.getDistance([33.450500,126.569968],[[33.450500,126.569968],[35.404195,126.886323],[39.668777,126.065913]]))
        # self.pushButton.clicked.connect(self.test_a)
        # self.pushButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(lambda: self.runner.search(self.lineEdit.text().strip()))
        self.pushButton.clicked.connect(lambda: self.runner.search(self.lineEdit.text().strip()))
        self.page.loadFinished.connect(lambda: self.runner.setMap(self.my_location_lat, self.my_location_lng))
        # self.setMap(self.my_location_lat, self.my_location_lng)

        self.pushButton2.clicked.connect(self.mark_around)
        self.pushButton3.clicked.connect(lambda: self.runner.setMap(self.my_location_lat,self.my_location_lng))
        self.page.urlChanged.connect(self.setButton)


        self.listWidget.itemActivated.connect(self.activateRow)
        # self.lineEdit.setText(self.runner.coord_to_address(self.my_location_lat,self.my_location_lng, 0))
        self.lineEdit.setText(self.runner.coord_to_address(self.my_location_lat,self.my_location_lng, 0))


    def mark_around(self) :
        self.remove_list()
        if not self.page.url().toString().strip().startswith("http://localhost:8080/umbrella") :
            self.page.load(QUrl(self.url))
            return
        self.runner.map_removeMarkers()
        lat, lng = self.runner.map_getCenter()
        data = self.dc.get_data_by_latlng(lat, lng, 1000)
        self.runner.marking(data)
        self.show_list(data)

        lat, lng = self.runner.map_getCenter()
        self.lineEdit.setText(self.runner.coord_to_address(lat, lng, 0))


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


    def setButton(self) :
        if self.page.url().toString().strip().startswith("http://localhost:8080/umbrella") :
            self.pushButton2.setText("판매처 탐색")
        else :
            self.pushButton2.setText("지도 새로고침")

    def show_list(self, data) :
        for i in range(len(data)) :
            item = QListWidgetItem(self.listWidget)
            row = Item(data[i])
            item.setWhatsThis(str(i))
            item.setSizeHint(row.sizeHint())
            self.listWidget.setItemWidget(item, row)
            self.listWidget.addItem(item)
            self.itemList.append(item)
            self.rowList.append(row)
    def remove_list(self) :
        for i in range(len(self.itemList)) :
            self.itemList[i].setHidden(True)
        self.itemList = []
        self.rowList = []

    def activateRow(self, row) :
        self.runner.setMap(self.rowList[int(row.whatsThis())].lat,self.rowList[int(row.whatsThis())].lng)
        self.runner.info_open(self.rowList[int(row.whatsThis())].code)
        # self.runner.map_setLevel(2)
        pass
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Umbrella()
    window.show()
    app.exec_()
    window.browser.close()
    window.browser.quit()

    # print(f'{lat}\n{lng}')
    pass
