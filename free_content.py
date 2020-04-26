from pprint import pprint
from bs4 import BeautifulSoup
import selenium
import requests
import json
import re

with open('../python/crawler/free_url.json', 'r') as f:
    urlList = json.load(f)

def crawl_content(url_):
    regex = re.compile(r'[\n\r\t]')
    data = {'title':'', 'time':'', 'content':'', 'resource':'', 'url':''}
    data['url']=url_
    res=requests.get(url_)
    soup=BeautifulSoup(res.text,'html.parser')
    contentbox=soup.find('div',{'class':'whitecon boxTitle'})
    data['title']=regex.sub(' ',contentbox.find('h1').text).strip()
    data['time']=contentbox.find('span',{'class','time'}).text
    data['resource']='自由時報電子報'
    temp=contentbox.find_all('p')
    content=''
    for i in temp[1::]:
        if i.text=='':pass
        else:
            content=content+i.text+'\n'
    data['content']=content
    return data

def crawl():
    data=[]
    for url_ in urlList:
        data.append(crawl_content(url_))
    return data
    
data=crawl()
with open('../python/crawler/free_news.json','w') as f :
    json.dump(data,f)
    print("加载入文件完成...")
    
