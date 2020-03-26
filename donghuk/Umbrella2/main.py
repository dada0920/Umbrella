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
import json
import os
import requests

from PyQt5.QtPositioning import *


#웹 엔진에서 파이썬으로 신호주기
#https://doc.qt.io/qtforpython/PySide2/QtWebEngineWidgets/QWebEnginePage.html#PySide2.QtWebEngineWidgets.PySide2.QtWebEngineWidgets.QWebEnginePage.runJavaScript
#https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwebenginewidgets/qwebenginepage.html#Feature

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



        self.comboBox.addItem("키워드")
        self.comboBox.addItem("주소")

        # self.page.featurePermissionRequested.connect(self.setPagePermission)


        # self.pushButton.clicked.connect(self.search)

        self.pushButton.clicked.connect(self.returnP)
        self.lineEdit.returnPressed.connect(self.search)
        self.init_my_location()
        self.page.loadFinished.connect(lambda: self.setMap(self.my_location_lat, self.my_location_lng))
        # self.setMap(self.my_location_lat, self.my_location_lng)


    #아이피로 현재 위치 받아오기(google api 사용)
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
        self.my_location_lat = my_location.get('location').get('lat')
        self.my_location_lng = my_location.get('location').get('lng')


    def setMap(self,lat, lng) :
        script = """
        var umbrella_location = new kakao.maps.LatLng("""+str(lat)+""", """+str(lng)+""");
        map.setCenter(umbrella_location);
        """
        self.run(script)

    #위치권한 요청이 왔을때 허용해줌
    def setPagePermission(self, url, feature) :
        self.page.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)


    def search(self) :


        search_text = self.lineEdit.text().strip()

        if self.comboBox.currentIndex() == 0 :
            script = """
            removeMarkers();
            // 주소-좌표 변환 객체를 생성합니다
            var geocoder = new kakao.maps.services.Geocoder();

            // 장소 검색 객체를 생성합니다
            var ps = new kakao.maps.services.Places();

            // 키워드로 장소를 검색합니다
            ps.keywordSearch('"""+search_text+"""', placesSearchCB);

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


            """
        elif self.comboBox.currentIndex():
            script = """
            removeMarkers();
            // 주소-좌표 변환 객체를 생성합니다
            var geocoder = new kakao.maps.services.Geocoder();

            // 주소로 좌표를 검색합니다
            geocoder.addressSearch('"""+search_text+"""', function(result, status) {

                // 정상적으로 검색이 완료됐으면
                 if (status === kakao.maps.services.Status.OK) {

                    var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

                    // 결과값으로 받은 위치를 마커로 표시합니다
                    var marker = new kakao.maps.Marker({
                        map: map,
                        position: coords
                    });



                    //*** 마커 담기
                    markerList.push(marker)


                    // 인포윈도우로 장소에 대한 설명을 표시합니다

                    infowindow.open(map, marker);

                    // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                    map.setCenter(coords);
                }
            });    """

        else :





            return


        self.run(script)

    def returnP(self) :
        script = """
        $(function(){
            var x = document.getElementById('centerY').value;
            return x
        })
        """
        # result = self.run(script)
        # print(result)
        print(str(self.page.scripts()))

    def run(self, script) :
        result = self.page.runJavaScript(script)
        return result
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
