import sys
import io
from bs4 import BeautifulSoup
import urllib.request
import os.path
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
import re
import datetime
import json
# from UI.main_ui import Ui_MainWindow
# import pytube
from threading import Thread
from PyQt5.QtCore import *
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

class Marker:
        def __init__(self):
            pass
        def SearchPharmacy(self,addr):

            # 약국 검색 url
            url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json"
            # option = "&display=3&sort=count"
            address = "?address="+urllib.parse.quote(addr)
            # url_address = url + address + option
            url_address = url + address

            #Open API 검색 요청 개체 설정
            request = urllib.request.Request(url_address)

            #검색 요청 및 처리
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode == 200):
                return response.read().decode('utf-8')
            else:
                return None


        #약국검색 메소드  data : jres["stores"], yg : 약국이름
        def searchYG(self,data, yg) :
            for i in range(len(data)) :

                if data[i].get("name") == yg :

                    return data[i]
            return "약국 못찾음"


        #약국검색 메소드  data : jres["stores"], latlng : 주소를 이용해 위경도 알아내기
        def searchaddr(self,data, addr) :
            for i in range(len(data)) :

                str=data[i].get("addr")

                if str.find(addr)!=-1:

                    return data[i].get("addr")
            return "약국 못찾음"

        def main2(self):
            #검색 질의 요청
            res = self.SearchPharmacy("")
            if(res == None):
                print("검색 실패!!!")
                exit()
            #검색 결과를 json개체로 로딩
            jres = json.loads(res)
            if(jres == None):
                print("json.loads 실패!!!")
                exit()

            mask_info = self.searchYG(jres["stores"], 'empty')

            for i in range(len(mask_info)):
                mask_info[i]
                print("약국 이름 : ",mask_info[i].get('name'))
                print("주소 : ",mask_info[i].get('addr'))
                print("dnl : ",mask_info[i].get('lat'))
                if mask_info[i].get('created_at')=='empty' :
                    print("정보 갱신 미상")
                elif mask_info[i].get('created_at') :
                    print("정보 갱신 시각 : ",mask_info[i].get('created_at'))
                if mask_info[i].get('remain_stat')==None or mask_info[i].get('remain_stat')=='break' or mask_info[i].get('remain_stat')=='empty':
                    print("마스크 재고 : 없음")
                elif mask_info[i].get('remain_stat')=='some' or mask_info[i].get('remain_stat')=='few':
                    print("마스크 재고 : 부족")
                elif mask_info[i].get('remain_stat')=='plenty':
                    print("마스크 재고: 충분")


if __name__ == "__main__" :
    marker=Marker()
    marker.main2()
