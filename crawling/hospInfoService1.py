import requests, xmltodict , json

key = "0gq8vc7H2YBXHYB0ZEGn%2FH1mK0ohv1NBOrs39BL5hjZjHWrSOHJBnJhgWJctf78sBkdd0VTMXCNQjqOi8CXeOQ%3D%3D"
url = "http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1?sidoCd=110000&sgguCd=110019&zipCd=2010&clCd=11&xPos=127.09854004628151&yPos=37.6132113197367&radius=3000&ServiceKey={}".format(key)
url2 = "http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1?zipCd=2040&clCd=28&ServiceKey={}".format(key)
content = requests.get(url2).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['response']['body']['items']['item']['addr'],ensure_ascii=False)
print(jsonString)
#jsonObj = json.loads(jsonString)


#for item in jsonObj['items']['item']:
#    print(item['addr'])