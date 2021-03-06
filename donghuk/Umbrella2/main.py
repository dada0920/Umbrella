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



import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



import random



from ScriptRunner import Runner
#python -m http.server

#웹 엔진에서 파이썬으로 신호주기
#https://doc.qt.io/qtforpython/PySide2/QtWebEngineWidgets/QWebEnginePage.html#PySide2.QtWebEngineWidgets.PySide2.QtWebEngineWidgets.QWebEnginePage.runJavaScript
#https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwebenginewidgets/qwebenginepage.html#Feature

class TestForm(QMainWindow, Ui_MainWindow) :
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
        #headless 모드
        chrome_option.add_argument("--headless")
        #사운드 뮤트
        chrome_option.add_argument("--mute-audio")

        # webdriver 설정(chrome) --headless
        self.browser = webdriver.Chrome(chrome_options=chrome_option, executable_path="webdriver/Chrome/chromedriver.exe")

        self.browser.get(self.url)

        self.runner = Runner(self.page, self.browser)
        self.comboBox.addItem("키워드")
        self.comboBox.addItem("주소")

        # self.page.featurePermissionRequested.connect(self.setPagePermission)


        # self.pushButton.clicked.connect(self.map_removeMarkers)

        # self.pushButton.clicked.connect(lambda: self.map_setLevel(random.randrange(7)))

        #현재위치
        #self.pushButton.clicked.connect(lambda: self.coord_to_address(37.62244036,127.072065, 0))
        #거리
        self.pushButton.clicked.connect(lambda: self.getDistance([33.450500,126.569968],[[33.450500,126.569968],[35.404195,126.886323],[39.668777,126.065913]]))

        self.pushButton.clicked.connect(lambda: self.runner.coord_to_address(self.my_location_lat,self.my_location_lng, random.randrange(0,5)))
        # self.pushButton.clicked.connect(lambda: self.getDistance([33.450500,126.569968],[[33.450500,126.569968],[35.404195,126.886323],[39.668777,126.065913]]))

        # self.pushButton.clicked.connect(self.test_a)
        # self.pushButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(self.search)
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


    def test_a(self) :
        script ="""
        return centerX.val()
        """
        centerX = self.run(script)
        print(centerX)



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





    #거리 계산하는 메소드
    # center에는 기준좌표 [lat, lng]
    # pointList에는 측정할 좌표 리스트 [ [lat,lng]  ,  [lat,lng] .......  ]
    #리턴값은 측정한 거리(int값) list  ex) [ [0], [218667], [691542] ]
    #단위는 m
    def getDistance(self, center, pointList) :

        # center가 None일 경우
        # 기본값으로 '내위치'의 좌표
        center = center or [self.my_location_lat, self.my_location_lng]

        script = """
        var tmp_point_arr = """+str(pointList)+"""
        var tmp_center = """+str(center)+"""
        var tmp_div = $('#tmp_div');
        var result_arr = new Array();
        for(var i=0; i < tmp_point_arr.length; i++){
            const polyline = new window.daum.maps.Polyline({
                map : map,
                path : [
                    new window.daum.maps.LatLng(tmp_center[0], tmp_center[1]),
                    new window.daum.maps.LatLng(tmp_point_arr[i][0], tmp_point_arr[i][1])
                ],
                strokeWeight : 0
            });
            result_arr.push(polyline.getLength());
        }
        return '['+result_arr.toString()+']';
        """
        result = list(map(int, eval(self.run(script))))
        print(result)
        for i in result :
            print(f"거리 : {i}m, type : {type(i)}")

        return result







    #좌표로 주소 얻기 idx
    #0 : 지번주소
    #1 : 지번주소 - 시도단위
    #2 : 지번주소 - 구 단위
    #3 : 지번주소 - 동 단위
    #4 : 지번주소 - 우편번호(6자리)
    #없을경우 ""
    def coord_to_address(self, lat, lng, idx) :
        if not idx in (0,1,2,3,4) :
            idx = 0
        result = ""
        print(lat)
        print(lng)
        script = """
        go_py_result = '대기중'
        var coord = new kakao.maps.LatLng("""+str(lat)+""", """+str(lng)+""");
        var c2a = function(result, status) {
            tmp_div.append("result0 -"+result[0].address.address_name);
            //go_py_result = result[0].address.address_name;
            var idx = """+str(idx)+"""


            if(idx === 0){
                go_py_result = result[0].address.address_name;
            }else if(idx === 1){
                go_py_result = result[0].address.region_1depth_name;
            }else if(idx === 2){
                go_py_result = result[0].address.region_2depth_name;
            }else if(idx === 3){
                go_py_result = result[0].address.region_3depth_name;
            }else if(idx === 4){
                go_py_result = result[0].address.zip_code;
            }else{
                go_py_result = result[0].address.address_name;
            }

        };
        geocoder.coord2Address(coord.getLng(), coord.getLat(), c2a);
        """
        script2 = "return go_py_result;"
        self.run(script)
        for i in range(50) :
            result = self.run(script2)
            if result != "대기중" :
                print("idx : ",idx,"c 2 a : ",result)
                return result
                break
        print("idx : ",idx,"c 2 a : ",result)
        return ""



    #지도 확대 레벨 설정
    def map_setLevel(self, level) :
        script = """
        map.setLevel("""+str(level)+""")
        """
        self.run(script)


    #마커 다 지우는 메소드
    def map_removeMarkers(self) :
        script = """
        removeMarkers();
        """
        self.run(script)


    #맵 이동
    def setMap(self,lat, lng) :
        script = """
        var umbrella_location = new kakao.maps.LatLng("""+str(lat)+""", """+str(lng)+""");
        map.setCenter(umbrella_location);
        """
        self.run(script)



    #스크립트 실행
    def run(self, script) :
        # print("run runJavaScript")
        self.page.runJavaScript(script)
        # print("run execute_Script")
        result = self.browser.execute_script(script)
        return result





    def marking(self, data) :
        typeP = ["","약국","우체국","농협"]
        for item in data :
            addr = item.get('addr')
            code = item.get('code')
            created_at = item.get('created_at')
            lat = item.get('lat')
            lng = item.get('lng')
            name = item.get('name')
            remain_stat = item.get('remain_stat')
            stock_at = item.get('stock_at')
            type = typeP[int(item.get('type'))]
            print(f"addr = {addr}\ncode = {code}\ncreated_at = {created_at}\nlat = {lat}\nlng = {lng}\nname = {name}\nremain_stat = {remain_stat}\nstock_at = {stock_at}\ntype = {type}")

            script = """










            """
            self.run(script)













if __name__ == "__main__" :
    # command = "python -m http.server"
    # subprocess.Popen("e:", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # subprocess.Popen("cd umbrella/donghuk/umbrella2", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # (stdoutdata, stderrdata) = popen.communicate()
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
    window.browser.close()
    window.browser.quit()
