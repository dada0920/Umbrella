
import json
import sys
import io
import urllib.request as req
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from bs4 import BeautifulSoup
#마커 찍으면서, 약국이름, 주소, 갱신시간, 입고시간, remain_stat
#type 1 : 약국, 2 : 우체국, 3 : 농협


#공릉역 :37.625782432083724,127.07302589022808

#위, 경도 기준
#https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat=34&lng=125&m=5000
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")
class DataCollector :
    def __init__(self):
            list_data=[]
            url = "http://ncov.mohw.go.kr/"

            res = req.urlopen(url).read()

            soup = BeautifulSoup(res, "html.parser")
            a = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.num ").text)
            b = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.before").text
            c = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.num").text)
            d = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text
            e = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.num").text)
            f = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.before").text
            g = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.num").text)
            h = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text



    def get_data_by_latlng(self, lat, lng, ds) :
        remainP = {'plenty' : '100개 이상', 'some' : '30개 이상 100개 미만', 'few' : '2개 이상 30개 미만', 'empty' : '1개 이하', 'break' : '판매중지'}
        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat="+str(lat)+"&lng="+str(lng)+"&m="+str(ds)+""
        result = json.loads(req.urlopen(url).read()).get("stores")
        for i in result :
            if i.get('remain_stat') in remainP :
                i['remain_stat'] = remainP[i['remain_stat']]


        return result






    # 숫자만 가져오는것
    def numI(self,text) :
        textL=list(text)
        result = ''
        for i in range(len(textL)):
             if textL[i].isnumeric() :
                 result += textL[i]
        return int(result)

    def A(self):
        list_data=[]
        url = "http://ncov.mohw.go.kr/"

        res = req.urlopen(url).read()

        soup = BeautifulSoup(res, "html.parser")
        a = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.num ").text)
        b = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.before").text
        c = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.num").text)
        d = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text
        e = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.num").text)
        f = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.before").text
        g = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.num").text)
        h = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text
        for i in (a,b,c,d,e,f,g,h):
            list_data.append(i)

        return list_data
        # print("완치자 : ",c,d)
        # print("치료중 : ",e,f)
        # print("사망자 : ",g,h)

    def intro_graph(self):
        # matplotlib 한글 폰트 설정
        font_name = font_manager.FontProperties(fname="c:/Windows/fonts/YTTE08.TTF").get_name()
        rc('font', family=font_name)

        labels = ('확진환자', '완치자', '치료중', '사망자') ## 라벨

        xs = [self.a,self.c,self.e,self.g] ## 값들, pie 차트에서 알아서 100% 기준으로 변경해서 정리해줌

        ## 그림
        plt.figure(figsize=(6, 6))
        ## plt.pie로 생기는 요소를 다음처럼 리턴하여 값을 저장
        patches, texts, autotexts = plt.pie(
            labels=labels, ## label
            x = xs, ## 값
            startangle=90,## 어디에서 시작할지, 정해줌
            shadow=False, ##그림자
            counterclock=False, ## 시계방향으로 가는지, 시계 반대 방향으로 가는지 정해줌
            autopct='%1.1f%%', ## pi 위에 표시될 글자 형태, 또한 알아서 %로 변환해서 알려줌
            pctdistance=0.7, ## pct가 radius 기준으로 어디쯤에 위치할지 정함
            colors=['red', 'blue', 'green','grey'],
        )
        ## add circle
        ## 도넛처럼 만들기 위해서 아래처럼
        centre_circle = plt.Circle((0,0),0.50,color='white')
        plt.gca().add_artist(centre_circle)
        #######
        ## label만 변경해주기
        for t in texts:
            t.set_color("black")
            t.set_fontsize(20)
        ## pie 위의 텍스트를 다른 색으로 변경해주기
        for t in autotexts:
            t.set_color("white")
            t.set_fontsize(20)
        plt.tight_layout()
        plt.savefig("D:/umbrella/200330_pie_chart.svg")
        plt.show()




if __name__ == "__main__" :
    # url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat=37.625782432083724&lng=127.07302589022808&m=500"
    # data1 = json.loads(urllib.request.urlopen(url).read()).get("stores")

    # print(data1)
    # print(f"\n\n\n\n {type(data1[0])}")
    dc = DataCollector()
    # # print(dc.get_data_by_latlng(37.6257824320837,127.07302589022,500))
    # print(dc.A())
    dc.intro_graph()
