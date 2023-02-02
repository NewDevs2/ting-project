import urllib
import xml

from django.shortcuts import render
from rest_framework.views import APIView
from opendata.models import AptData

# Create your views here.
class Main(APIView):        #config/url에서 사용
    def get(self, request):
        apt_list = AptData.objects.all().order_by('-id')
        return render(request, 'opendata/main.html', context=dict(apt_list=apt_list))

def index(request):
    data = AptPrice()
    apt_list = AptData.objects.order_by('-month') #Choices are: city, id, month, price_apt, year
    return render(request, 'opendata/main.html', apt_list)


def AptPrice():     #아래 코드는 변경 필요
    encodingKey = "ji1kgS0kZ0B%2B5svnXJTua9Td3Q8yMihu8bADZdXeLKkpPsKfCk6OeQzun%2FDPw1Cu3S9YEGgqO2UwMqSqceiR%2Fg%3D%3D"
    decodingKey = "ji1kgS0kZ0B+5svnXJTua9Td3Q8yMihu8bADZdXeLKkpPsKfCk6OeQzun/DPw1Cu3S9YEGgqO2UwMqSqceiR/g=="

    # request url 정의
    url = "http://apis.data.go.kr/1611000/nsdi/IndvdHousingPriceService/attr/getIndvdHousingPriceAttr"
    request = urllib.request.Request(url)

    # request 요청
    response = urllib.request.urlopen(request)

    # response 결과
    rescode = response.getcode()

    if (rescode == 200): # 요청 결과 성공시에만
        response_body = response.read()
        res = xml.dom.minidom.parseString(response_body.decode('utf-8'))
        pretty_res = res.toprettyxml()
        print(pretty_res)
    else: # 실패시 -> 에러코드 출력
        print("Error Code:" + rescode)



def StockIndex():           #아래 코드는 갱신 필요
    encodingKey = "ji1kgS0kZ0B%2B5svnXJTua9Td3Q8yMihu8bADZdXeLKkpPsKfCk6OeQzun%2FDPw1Cu3S9YEGgqO2UwMqSqceiR%2Fg%3D%3D"
    decodingKey = "ji1kgS0kZ0B+5svnXJTua9Td3Q8yMihu8bADZdXeLKkpPsKfCk6OeQzun/DPw1Cu3S9YEGgqO2UwMqSqceiR/g=="
    # request url 정의
    url="https://apis.data.go.kr/1160100/service/GetMarketIndexInfoService/getStockMarketIndex?serviceKey=ji1kgS0kZ0B%2B5svnXJTua9Td3Q8yMihu8bADZdXeLKkpPsKfCk6OeQzun%2FDPw1Cu3S9YEGgqO2UwMqSqceiR%2Fg%3D%3D&"

    request = urllib.request.Request(url)

    # request 요청
    response = urllib.request.urlopen(request)

    # response 결과
    rescode = response.getcode()

    if (rescode == 200): # 요청 결과 성공시에만
        response_body = response.read()
        res = xml.dom.minidom.parseString(response_body.decode('utf-8'))
        pretty_res = res.toprettyxml()
        print(pretty_res)
    else: # 실패시 -> 에러코드 출력
        print("Error Code:" + rescode)



# 다른 예 urllib parse 사용
""" urllib 패키지의 parse 모듈은 url에 파라미터를 입력할 때 사용,
     param 에는 "LAWD_CD=area&DEAL_YMD=year+month" 문자열이 입력된다.
      이것을 사용하여 area, year, month 값을 바꿔가면서 아파트 실거래 데이터를 받을 수 있다. 
      그리고 data에는 해당 url을 통해 받은 아파트 실거래 데이터가 xml 형식으로 입력된다.
      [출처] https://blog.naver.com/PostView.nhn?blogId=swengdaddy&logNo=221463439968
"""
import urllib.parse as par
import urllib.request as req

def AptPrice1():
    url = "http://openapi..."
    params = {                  # 우리 데이터에 맞게 변경
            'LAWD_CD': area,
            'DEAL_YMD': year + month
            }
    param = par.urlencode(params)
    url = url + param
    data = req.urlopen(url).read()
