import sys
import io
import urllib.request as req
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

url = "http://ncov.mohw.go.kr/"

res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parser")

# 숫자만 가져오는것
def numI(text) :
    textL=list(text)
    result = ''
    for i in range(len(textL)):
         if textL[i].isnumeric() :
             result += textL[i]
    return int(result)

a = numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.num ").text)
b = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.before").text
c = numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.num").text)
d = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text
e = numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.num").text)
f = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.before").text
g = numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.num").text)
h = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text
print("확진환자 : ",a,b)
print("완치자 : ",c,d)
print("치료중 : ",e,f)
print("사망자 : ",g,h)

# matplotlib 한글 폰트 설정
font_name = font_manager.FontProperties(fname="c:/Windows/fonts/YTTE08.TTF").get_name()
rc('font', family=font_name)

labels = ('확진환자', '완치자', '치료중', '사망자') ## 라벨

xs = [a,c,e,g] ## 값들, pie 차트에서 알아서 100% 기준으로 변경해서 정리해줌

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
