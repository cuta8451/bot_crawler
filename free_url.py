from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json

def content_url(photo_u,list_u,data):
    for j in photo_u:
        data.append(j["href"])
    for i in list_u:
        data.append(i["href"])
    return data

def crawl():
    data=[]
    url="http://ec.ltn.com.tw/list/international/"
    for i in range(1,40):
        res=requests.get(url+str(i))
        soup=BeautifulSoup(res.text,"html.parser")
        photo_url=soup.find('div',{'class':'listphoto'}).find_all('a')
        list_url=soup.find('div',{'class':'whitecon boxTitle'}).find('ul','list').find_all('a')
        content_url(photo_url,list_url,data)
    return data

data= crawl()

with open('../python/crawler/free_url.json','w') as f :
    json.dump(data,f)
    print("加载入文件完成...")
