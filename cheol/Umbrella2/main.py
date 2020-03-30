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
from urllib.parse import urljoin

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

# #요청
# url="https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json"
# savename = "D:umbrella/Mask.xml"
# if not os.path.exists(savename):
#     request.urlretrieve(url,savename)
#
# #숲처리
# xml=open(savename,'r',encoding='utf-8').read()
# soup=BeautifulSoup(xml, "html.parser")
#
# print(soup.prettify())

# 서치기능
# - 약국 별
# (약국 이름을 검색하면 해당 약국의 정보 (마스크잔량, 오픈시간, 위치 등) 을 보여준다)
def SearchPharmacy(addr):
    # 약국 검색 url
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json"
    addr = "?lat=37.6803112&lng=127.0549036&m=500"
    # address = urllib.parse.quote(addr)
    url_address = urljoin(url,addr)

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
def searchYG(data, yg) :
    for i in range(len(data)) :

        if data[i].get("name") == yg :

            return data[i]
    return "약국 못찾음"

#프로그램 진입점
def main():
    #검색 질의 요청
    res = SearchPharmacy("")
    if(res == None):
        print("검색 실패!!!")
        exit()
    #검색 결과를 json개체로 로딩
    jres = json.loads(res)
    if(jres == None):
        print("json.loads 실패!!!")
        exit()

    yg_info = searchYG(jres["stores"], "역삼오늘약국")

    print("약국 이름 : ",yg_info.get('name'))
    print("주소 : ",yg_info.get('addr'))
    if yg_info.get('created_at')=='empty' :
        print("정보 갱신 미상")
    elif yg_info.get('created_at') :
        print("정보 갱신 시각 : ",yg_info.get('created_at'))
    if yg_info.get('remain_stat')==None or yg_info.get('remain_stat')=='break' or yg_info.get('remain_stat')=='empty':
        print("마스크 재고 : 없음")
    elif yg_info.get('remain_stat')=='some' or yg_info.get('remain_stat')=='few':
        print("마스크 재고 : 부족")
    elif yg_info.get('remain_stat')=='plenty':
        print("마스크 재고: 충분")

# - 마스크 잔량 별
#     ( 마스크 잔량 기준을 선택하면 해당 약국만 보여준다)

# 마스크 잔량 기준약국검색 메소드  data : jres["remain_stat"], mk : 마스크 잔량
def searchMK(data, mk) :
    list = []
    for i in range(len(data)) :
        if data[i].get("remain_stat") == mk :
            list.append(data[i])
    return list

#프로그램 진입점
def main2():
    #검색 질의 요청
    res = SearchPharmacy("")
    if(res == None):
        print("검색 실패!!!")
        exit()
    #검색 결과를 json개체로 로딩
    jres = json.loads(res)
    if(jres == None):
        print("json.loads 실패!!!")
        exit()

    mask_info = searchMK(jres["stores"], 'empty')

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


# - 위치 기반 별
#     ( 지정한 위치 기준 반경 500m 이내의 판매 약국을 보여준다)

#  신뢰도 표시 == ??? 재고 입고 시간, 데이터의 정확성 (empty or null), 갱신시각

if __name__ == "__main__" :
    main2()
