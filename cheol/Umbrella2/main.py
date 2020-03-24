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

#요청
url="https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json"
savename = "D:umbrella/Mask.xml"
if not os.path.exists(savename):
    req.urlretrieve(url,savename)

#숲처리
xml=open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml, "html.parser")

print(soup.prettify())

# 서치기능
# - 약국 별
# (약국 이름을 검색하면 해당 약국의 정보 (마스크잔량, 오픈시간, 위치 등) 을 보여준다)
def SearchPharmacy(addr):

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

#검색 결과 항목 정보 출력하기
def showPharmacy(Pharmacy):
    print("주소 : " +Pharmacy['addr'])
    print("약국이름 : " +Pharmacy['name'])
    print("위도 : ",Pharmacy['lat'])
    print("경도 : ",Pharmacy['lng'])
    if Pharmacy['created_at']==None :
        print("정보 갱신 미상")
    elif Pharmacy['created_at'] :
        print("정보 갱신 시각 : "+Pharmacy['created_at'])
    if Pharmacy['remain_stat']==None or Pharmacy['remain_stat']== 'break' or Pharmacy['remain_stat']=='empty':
        print("마스크 재고 : 없음")
    elif Pharmacy['remain_stat']=='some' or Pharmacy['remain_stat']=='few':
        print("마스크 재고 : 부족")
    elif Pharmacy['remain_stat']=='plenty':
        print("마스크 재고: 충분")
    print("================")

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

    #검색 결과의 name 목록의 각 항목(post)을 출력
    for post in jres['stores']:
        showPharmacy(post)

# - 마스크 잔량 별
#     ( 마스크 잔량 기준을 선택하면 해당 약국만 보여준다)
#
# - 위치 기반 별
#     ( 지정한 위치 기준 반경 500m 이내의 판매 약국을 보여준다)

if __name__ == "__main__" :
    main()
