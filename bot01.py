import telepot,time
from datetime import datetime
from pprint import pprint
from telepot.loop import MessageLoop
from weather import (Country,dataurl)
from novel import novel
from telepot.delegate import per_chat_id
#bot 
bot = telepot.Bot(token="663093043:AAGh67h0uSdO0-my4E7qTQIXPBaas1kUEF4")

country=["台北市","臺北市","台北","臺北","新北市","新北","桃園市","桃園",\
"臺中市","台中市","台中","臺中","臺南市","台南市","台南","臺南",\
"高雄市","高雄","基隆市","基隆","新竹市","新竹縣","苗栗縣","苗栗",\
"彰化縣","彰化","南投縣","南投","雲林縣","雲林","嘉義市","嘉義縣",\
"屏東縣","屏東","宜蘭縣","宜蘭","花蓮縣","花蓮","臺東縣","台東縣","台東","臺東",\
"澎湖縣","澎湖","金門縣","金門","連江縣","連江"]
menu=[["音樂"], ["天氣"], ["新聞"], ["小說"], ["電影"],["書籍"]]
novellist=["總榜","商業理財","藝術設計","自然科普","心理勵志","旅遊","語言學習"]

botcon=["早安阿!!不要賴床囉~~再賴下去，我也想跟你一起睡惹......","中午了!!不要再工作了!!看你這麼累，我會心疼der~~","加油加油!!就快下班囉!!","已經下課了喔!!別再打程式了，去走走吧!!"]

msgid=[]
def botsays(msgid,botcon,way):#傳送訊息給user
    for i in range(len(msgid)):
        bot.sendMessage(msgid[i],botcon)
        on_chat({'text':way,"chat":{"id":msgid[i]}})
def on_chat(message):
    pprint(message)
    if message['text'] == "天氣":
        bot.sendMessage(message['chat']['id'], '請選擇你要查詢的項目', reply_markup = {"keyboard":[["縣市"], ["紫外線"]]})
    elif message['text'] == "紫外線":
        bot.sendPhoto(message['chat']['id'],("light.png",dataurl()),reply_markup = {"keyboard":menu})
    elif message['text'] == "縣市":
        bot.sendMessage(message['chat']['id'],'你住在哪個縣市啊?')
    elif message['text'] in country:
        bot.sendMessage(message['chat']['id'],Country(message['text']),reply_markup = {"keyboard":menu})
    elif message["text"]=="/start":
        bot.sendMessage(message['chat']['id'],"歡迎你，你可以利用選單選擇你有興趣的主題",reply_markup = {"keyboard":menu})
        if message['chat']['id'] not in msgid:
            msgid.append(message['chat']['id'])
    elif message['text'] == "書籍":
        bot.sendMessage(message['chat']['id'], '請選擇你要查詢的項目', reply_markup = {"keyboard":[["總榜"], ["商業理財"],["藝術設計"],["自然科普"],["心理勵志"],["旅遊"],["語言學習"]]})
    elif message["text"] in novellist:
        bot.sendMessage(message['chat']['id'],novel(message['text']),reply_markup = {"keyboard":menu})
    else:
        pass


MessageLoop (bot,on_chat).run_as_thread ()

while True:
    if datetime.now().hour==8 and datetime.now().minute==30:botsays(msgid,botcon[0],"紫外線")
    elif datetime.now().hour==12 and datetime.now().minute==5:botsays(msgid,botcon[1],"")
    elif datetime.now().hour==15 and datetime.now().minute==30:botsays(msgid,botcon[2],"")
    elif datetime.now().hour==24 and datetime.now().minute==3:botsays(msgid,botcon[3],"")
    time.sleep(60)