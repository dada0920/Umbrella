from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class Runner :

    def __init__(self, parent) :
        self.main = parent
        # chrome_option = Options()
        # chrome_option.add_argument("--headless")
        # chrome_option.add_argument("--mute-audio")
        # self.browser = webdriver.Chrome(chrome_options=chrome_option, executable_path="webdriver/Chrome/chromedriver.exe")
        # self.browser.get(url)


    def info_open(self, code) :
        script = """

        infowindow"""+str(code)+""".open(map, marker"""+str(code)+""");
        """
        self.main.page.runJavaScript(script)


    def search(self, search_text) :
        # search_text = self.lineEdit.text().strip()

        if True :
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
        # else:
        #     script = """
        #     removeMarkers();
        #     // 주소-좌표 변환 객체를 생성합니다
        #     var geocoder = new kakao.maps.services.Geocoder();
        #
        #     // 주소로 좌표를 검색합니다
        #     geocoder.addressSearch('"""+search_text+"""', function(result, status) {
        #
        #         // 정상적으로 검색이 완료됐으면
        #          if (status === kakao.maps.services.Status.OK) {
        #
        #             var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
        #
        #             // 결과값으로 받은 위치를 마커로 표시합니다
        #             /*var marker = new kakao.maps.Marker({
        #                 map: map,
        #                 position: coords
        #             });
        #             //*** 마커 담기
        #             markerList.push(marker)*/
        #
        #
        #             // 인포윈도우로 장소에 대한 설명을 표시합니다
        #
        #             infowindow.open(map, marker);
        #
        #             // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
        #             map.setCenter(coords);
        #         }
        #     });    """

        self.run(script)



    #거리 계산하는 메소드
    # center에는 기준좌표 [lat, lng]
    # pointList에는 측정할 좌표 리스트 [ [lat,lng]  ,  [lat,lng] .......  ]
    #리턴값은 측정한 거리(int값) list  ex) [ [0], [218667], [691542] ]
    #단위는 m
    def getDistance(self, center, pointList) :

        # center가 None일 경우
        # 기본값으로 '내위치'의 좌표
        center = center or [self.main.my_location_lat, self.main.my_location_lng]

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
            //tmp_div.append("result0 -"+result[0].address.address_name);
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




    #spring 컨트롤러 설정 필요
    def map_getCenter(self) :
        result = ""
        # print("map_getcenter call")
        script ="""
        $.ajax({
            type : 'POST',
            url : '/umbrella/save_center',
            data :{'center_lat' : map.getCenter().getLat(),'center_lng' : map.getCenter().getLng(), 'user_uuid' : '"""+str(self.main.user_uuid)+"""'}
        });
        """
        # print("mpct run1")
        self.main.page.runJavaScript(script)

        script2="""
        go_py_result2 = '';


        $.ajax({
            type : 'POST',
            url : '/umbrella/get_center',
            data : {'user_uuid' : '"""+str(self.main.user_uuid)+"""'},
            success : function(data_center){
                go_py_result2 = data_center;
            }


        });
        """
        # print("mpct run2")
        self.main.browser.execute_script(script2)
        for i in range(500) :
        # while True :
            result = self.main.browser.execute_script("return go_py_result2")
            # print("getcenter.....result : ",result)
            print("getcen,,,,,",result)
            if result != "" :
                return result.split()[0], result.split()[1]
                print("getcenter.....return : ",result.split()[0], result.split()[1])
                break
        print("getcen,,,,,",result)



    #지도 확대 레벨 확인
    def map_getLevel(self) :
        script = """

        $.ajax({
            type : 'POST',
            url : '/umbrella/save_level',
            data :{'level' : map.getLevel(),'user_uuid' : '"""+str(self.main.user_uuid)+"""'}
        });
        """
        self.main.page.runJavaScript(script)
        script2="""
        $.ajax({
            type : 'POST',
            url : '/umbrella/get_level',
            data : {'user_uuid' : '"""+str(self.main.user_uuid)+"""'},
            success : function(data_level){
                go_py_result = data_level;
            }
        });
        """
        self.main.browser.execute_script(script2)
        script3 = """
        return go_py_result
        """
        for i in range(500) :
            result = self.main.browser.execute_script(script3)
            if result != '' :
                print(f"지도레벨 반환 :[{result}] ")
                return result
        # print("지도레벨 반환 : ",result)
        return result

    #지도 레벨 설정
    def map_setLevel(self, level) :
        script = """
        map.setLevel("""+str(level)+""")
        """
        level = self.run(script)
        print(level)
        return level

    #마커 다 지우는 메소드
    def map_removeMarkers(self) :
        print("mk remove")
        script = """
        removeMarkers();
        removeInfowindows();
        """
        self.run(script)


    #맵 이동
    def setMap(self,lat, lng) :
        self.map_setLevel(3)
        script = """
        var umbrella_location = new kakao.maps.LatLng("""+str(lat)+""", """+str(lng)+""");
        map.setCenter(umbrella_location);
        """
        self.run(script)
        # self.d1 = self.main.dc.get_data_by_latlng(self.main.my_location_lat,self.main.my_location_lng,1000)
        # self.marking(self.d1)

        self.map_getCenter()
        self.map_getLevel()

    #스크립트 실행
    def run(self, script) :
        print("run runJavaScript")
        self.main.page.runJavaScript(script)
        print("run execute_Script")
        result = self.main.browser.execute_script(script)
        return result





    def marking(self, data) :
        self.map_removeMarkers()
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
            # print(f"addr = {addr}\ncode = {code}\ncreated_at = {created_at}\nlat = {lat}\nlng = {lng}\nname = {name}\nremain_stat = {remain_stat}\nstock_at = {stock_at}\ntype = {type}")

            script = """
            var markerPosition  = new kakao.maps.LatLng("""+str(lat)+""", """+str(lng)+""");

            var marker"""+str(code)+""" = new kakao.maps.Marker({
                position: markerPosition
            });

            markerList.push(marker"""+str(code)+""");

            marker"""+str(code)+""".setMap(map);

            var iwContent = '<div style="padding:5px;">"""+f"{name}   ({remain_stat})"+""" <br><a href="https://map.kakao.com/link/map/Hello World!,"""+str(lat)+""","""+str(lng)+"""" style="color:blue" target="_self">큰지도보기</a> <a href="https://map.kakao.com/link/to/"""+f'{name},{lat},{lng}'+"""" style="color:blue" target="_self">길찾기</a></div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
                    iwPosition = new kakao.maps.LatLng("""+str(lat)+""", """+str(lng)+"""); //인포윈도우 표시 위치입니다


            var infowindow"""+str(code)+""" = new kakao.maps.InfoWindow({
                position : iwPosition,
                removable : iwRemoveable,
                content : iwContent
            });
            infowindowList.push(infowindow"""+str(code)+""");
            //infowindow"""+str(code)+""".open(map, marker);

            kakao.maps.event.addListener(marker"""+str(code)+""", 'click', function() {
                  // 마커 위에 인포윈도우를 표시합니다
                  infowindow"""+str(code)+""".open(map, marker"""+str(code)+""");
            });



            """
            self.run(script)


# if __name__ == "__main__" :
    # page = QWebEnginePage()
    # url = "http://localhost:8080/umbrella"
    # runner = Runner(page, url)
