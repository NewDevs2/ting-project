from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

import urllib.parse as par
import urllib.request as req

# 데이터명:	한국부동산원_공동주택 실거래가격지수 통계 조회 서비스

#serviceKey = "본인의 서비스 키"
serviceKey = "ji1kgS0kZ0B%2B5svnXJTua9Td3Q8yMihu8bADZdXeLKkpPsKfCk6OeQzun%2FDPw1Cu3S9YEGgqO2UwMqSqceiR%2Fg%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

returnType = "json"  # "xml"
# numOfRows="100"
# pageNo="1"
region_cd = "A1000"
region_nm = "서울"
ver = "1.0"
apt_type = '0'  # 공동주택
size_gbn = "0"  # 전체
contract_type = "0"  # 매매
research_date = "(GTE) 202201"
detail_svc = "getAptRealTradingPriceIndex"

def AptPrice():
    url = "https://api.odcloud.kr/api/RealTradingPriceIndexSvc?ServiceKey=" + serviceKey
    # " / v1 / 상세서비스명?page = 1 & perPage = 10 & serviceKey = 서비스키
    #params = {                  # 우리 데이터에 맞게 변경
    #        'LAWD_CD': area,
    #        'DEAL_YMD': year + month
    #        }
    params = {
        "page": 1,
        "perPage": 10,
        #"totalCount": 100,
        #"currentCount": 50,
        #"matchCount": 10,
        "data": [
            {
                "REGION_CD":region_cd,
                #"REGION_NM": region_nm,   #"string",
                "APT_TYPE": apt_type,   #"string",
                "CONTRACT_TYPE": "0",  #"string",
                "RESEARCH_DATE": research_date, # "string",
                "INDICES": 0,
                "LEVEL_NO": "0"
            }
        ]
    }

    param = par.urlencode(params)
    #print(param)
    url = url + param

    #임의로 URL 생성
    url ="https://api.odcloud.kr/api/RealTradingPriceIndexSvc/v1/getAptRealTradingPriceIndex?page=1&perPage=10&cond%5BREGION_CD%3A%3AEQ%5D=11000&cond%5BAPT_TYPE%3A%3AEQ%5D=0&cond%5BSIZE_GBN%3A%3AEQ%5D=0&cond%5BCONTRACT_TYPE%3A%3AEQ%5D=0&cond%5BRESEARCH_DATE%3A%3ALTE%5D=202202&cond%5BRESEARCH_DATE%3A%3AGTE%5D=202201&serviceKey=" + serviceKey
    print(url)
    data = req.urlopen(url).read()
    print(data)

AptPrice()

