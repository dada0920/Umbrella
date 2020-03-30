import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

url = "http://ncov.mohw.go.kr/"

res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parser")

h = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.num ").text
k = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.before").string
j = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.num").text
i = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text
a = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.num").text
l = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.before").text
t = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.num").text
o = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text
print("확진환자 : ",h,k)
print("완치자 : ",j,i)
print("치료중 : ",a,l)
print("사망자 : ",t,o)
