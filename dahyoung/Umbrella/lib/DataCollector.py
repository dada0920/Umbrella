import urllib.request
import json


#마커 찍으면서, 약국이름, 주소, 갱신시간, 입고시간, remain_stat
#type 1 : 약국, 2 : 우체국, 3 : 농협


#공릉역 :37.625782432083724,127.07302589022808

#위, 경도 기준
#https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat=34&lng=125&m=5000
class DataCollector :


    def get_data_by_latlng(self, lat, lng, ds) :
        remainP = {'plenty' : '100개 이상', 'some' : '30개 이상 100개 미만', 'few' : '2개 이상 30개 미만', 'empty' : '1개 이하', 'break' : '판매중지'}
        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat="+str(lat)+"&lng="+str(lng)+"&m="+str(ds)+""
        result = json.loads(urllib.request.urlopen(url).read()).get("stores")
        for i in result :
            if i.get('remain_stat') in remainP :
                i['remain_stat'] = remainP[i['remain_stat']]


        return result





if __name__ == "__main__" :
    # url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat=37.625782432083724&lng=127.07302589022808&m=500"
    # data1 = json.loads(urllib.request.urlopen(url).read()).get("stores")

    # print(data1)
    # print(f"\n\n\n\n {type(data1[0])}")
    dc = DataCollector()
    print(dc.get_data_by_latlng(37.6257824320837,127.07302589022,500))
