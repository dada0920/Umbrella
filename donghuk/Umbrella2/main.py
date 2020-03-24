import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
import re
import datetime
from ui.main_ui import Ui_MainWindow
import pytube
from threading import Thread
from PyQt5.QtCore import *
import subprocess
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class TestForm(QMainWindow, Ui_MainWindow) :
    #생성자
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  # 초기화
        self.url = "http://localhost:8080/umbrella"
        self.webEngineView.load(QUrl(self.url))
        self.page = QWebEnginePage()
        self.page.setUrl(QUrl(self.url))
        self.page.setView(self.webEngineView)
        self.pushButton.clicked.connect(self.search)

    def search(self) :
        keyword = self.lineEdit.text().strip()

        script_tmp_1 = """


// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();

// 장소 검색 객체를 생성합니다
var ps = new kakao.maps.services.Places();

// 키워드로 장소를 검색합니다
ps.keywordSearch('"""+self.lineEdit.text().strip()+"""', placesSearchCB);

function placesSearchCB (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();

        for (var i=0; i<data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        }

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);
    }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {

    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x)
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(map, marker);
    });
}




        """

        self.run(script_tmp_1)
    def run(self, script) :     
        self.page.runJavaScript(script)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
