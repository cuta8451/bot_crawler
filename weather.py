import requests
import time,random
from bs4 import BeautifulSoup
from urllib import request

def getData(data):
    string=""
    time,temp,pict,condi,confort,rain,msg=[],[],[],[],[],[],[]
    for data_ in data:#取得時間、溫度、天氣狀況、舒適度、降雨機率等資料
        time.append(data_.find('th',{'scope':'row'}).text)
        temp.append(data_.find_all('td')[0].text)
        condi.append(data_.find('img')['title'])
        confort.append(data_.find_all('td')[2].text)
        rain.append(data_.find_all('td')[3].text)
        if "雨" in str(condi[0]): msg.append("記得帶雨傘唷!!")
        elif "晴" in str(condi[0]):msg.append("要記得塗防曬喔~~~~")
        elif "多雲" in str(condi[0]):msg.append("今天是個適合運動的日子")
        else :msg.append("每一天都是新的一天!")
        break
    #for i in range(len(time)):
    string+="時間：%s \n溫度：%s (℃) \n天氣狀況：%s \n舒適度：%s \n降雨機率：%s \n我想對你說：%s"%(time[0],temp[0],condi[0],confort[0],rain[0],msg[0])
    return string

def Country(text):
    dic={"Taipei_City.htm":["台北市","臺北市","台北","臺北"],"New_Taipei_City.htm":["新北市","新北"],"Taoyuan_City.htm":["桃園市","桃園"],\
    "Taichung_City.htm":["臺中市","台中市","台中","臺中"],"Tainan_City.htm":["臺南市","台南市","台南","臺南"],"Kaohsiung_City.htm":["高雄市","高雄"],\
    "Keelung_City.htm":["基隆市","基隆"],"Hsinchu_City.htm":["新竹市"],"Hsinchu_County.htm":["新竹縣"],"Miaoli_County.htm":["苗栗縣","苗栗"],\
    "Changhua_County.htm":["彰化縣","彰化"],"Nantou_County.htm":["南投縣","南投"],"Yunlin_County.htm":["雲林縣","雲林"],\
    "Chiayi_City.htm":["嘉義市"],"Chiayi_County.htm":["嘉義縣"],"Pingtung_County.htm":["屏東縣","屏東"],"Yilan_County.htm":["宜蘭縣","宜蘭"],\
    "Hualien_County.htm":["花蓮縣","花蓮"],"Taitung_County.htm":["臺東縣","台東縣","台東","臺東"],"Penghu_County.htm":["澎湖縣","澎湖"],\
    "Kinmen_County.htm":["金門縣","金門"],"Lienchiang_County.htm":["連江縣","連江"]}
    for k,v in dic.items(): #連進縣市天氣資訊頁面
        if text in v :
            url ="https://www.cwb.gov.tw/V7/forecast/taiwan/"+k
            break
    response=requests.get(url)
    html=response.content
    html_doc=str(html,'utf-8')
    soup = BeautifulSoup(html_doc,"html.parser")
    data=soup.find('div',{'class':'BoxContent clearfix'}).find('table',{'class':'FcstBoxTable01'}).find('tbody').find_all('tr')#取得標籤資料
    return getData(data)
    
def dataurl():
    url="https://www.cwb.gov.tw/V7/forecast/UVI/UVI.htm"
    http="https://www.cwb.gov.tw"
    response=requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    data=soup.find('div',{'class':'UVITWmap'})["style"].split("url(")[1][:-1]
    return request.urlopen(http+data)

def main():
    Country('台北市')

    return

if __name__ == '__main__':
    main()