import requests
import time
from bs4 import BeautifulSoup

dic={"總榜":["","01"],"商業理財":["02","03"],"藝術設計":["03","04"],"自然科普":["06","07"],"心理勵志":["07","08"],"旅遊":["11","12"],"語言學習":["17","18"]}
def printTop5(name,link):
    #印出答案
    string=""
    for i in range(len(name)):
        string+="TOP%s：%s\n連結：%s\n=======================\n"%(str(i+1),name[i],link[i])
    return string
def top5(data):
    link,name=[],[]
    #因為只抓前5名，所以用count計次數，跑到第5次，就跳出
    #link是存連結，name是存名字，兩個的類型都是list
    count=0
    for i in data:
        count+=1
        info=i.find("a")
        link.append(info["href"])
        name.append(i.text.split("：")[0])
        if count==5:break
    return printTop5(name,link)
    #return link,name
def novel(text):
    #找你要分類的網址(我是找博客來總榜的月暢銷排行榜)
    url ="https://www.books.com.tw/web/sys_bkmtop/books/"+dic[text][0]+"/?loc=P_002_0"+dic[text][1]
    #請求抓取該網址的內容
    response=requests.get(url)
    #有時候抓下來的內容會有亂碼，所以我們要解碼成看得懂的中文
    html=response.content
    html_doc=str(html,'utf-8')
    #利用BeautifulSoup這個函式去做後續find的動作
    soup = BeautifulSoup(html_doc,"html.parser")
    #利用find去抓網頁的tag標籤(網頁按f12可以看網頁程式碼)
    data=soup.find("div",{"class","mod_a clearfix"}).find("ul",{"class","clearfix"}).find_all("h4")
    return top5(data)
