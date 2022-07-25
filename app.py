from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time
from selenium import webdriver
from linebot.models import *
from config import *
import time
import string
from selenium.webdriver.common.by import By

import time
# 自動推播
import re
# 必須放上自己的Channel Access Token
#line_bot_api = LineBotApi('npHX/BAgLnGzrMDuTXPdwYZOmMc6S7zZzh1FOaxjgrKuloHrShOzRNV3A8ImRST1SVoCSCbHjwjEYF5zKpnL4M25wJE4paVUu3vWdXIsVDcXHvRwbz3xh6s/SdQeacX0lTsyLFVzsmiezV7MdjhPigdB04t89/1O/w1cDnyilFU=')
href_list = []
header_list = []
save_message = []
new_header = []
new_href = []

def run():
    global dr
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    dr = webdriver.Chrome(chrome_options=chrome_options)
    dr.maximize_window()
    dr.get('http://www.facebook.com')
    dr.find_element(By.NAME,"email").send_keys("joe901007@yahoo.com.tw")
    time.sleep(3)
    dr.find_element(By.ID,"pass").send_keys("82585336")
    dr.find_element(By.NAME,"login").click()
    time.sleep(3)
    dr.get("https://www.facebook.com/groups/248305265374276")
    time.sleep(2)

    for i in range(5): 	# 讓頁面滾動x次
    #article = []
        dr.execute_script("window.scrollTo(0,document.body.scrollHeight);")# document.body.scrollHeight
        time.sleep(2)	 # 等待2秒鐘讓頁面讀取
        soup = BeautifulSoup(dr.page_source, "html.parser")
        frames = soup.find_all(role="article")#很多包涵內文跟文章
        attr1 = {'data-ad-preview':"message"} #找文章
        more = 0 #看查看更多點及次數
        for article in frames:
            t_content = article.find(attrs = attr1) #內文 有很多行
            #for line in t_content:
            if t_content != None: 
                if '抽' in t_content.text or '問卷' in t_content.text: #抽獎
                        time.sleep(1)
                        tag = article.find('a',{'class':"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"})
                        href_list.append(tag['href'])
                        try:
                        
                            header_list.append(t_content.text[:30])  #跑出前三十個字
                        except:
                            header_list.append('xxx')
                    
                        time.sleep(2)
    #print(len(header_list),len(href_list),sep=',')          
    dr.close()
    for i in range(len(href_list)): #有許多連結是重複的 用for迴圈把重複的刪除 並把需要的印出來 先印前三十個字 再印連結
        if header_list.count(header_list[i]) > 1:
            header_list[i] = 0
            href_list[i] = 0
        elif header_list[i] != 0:
            new_header.append(header_list[i])
            new_href.append(href_list[i])
            
        else:
            new_header.append(header_list[i])
            new_href.append(href_list[i])

    astring = ""    
    for i in range(len(new_header)):
            astring += new_header[i]
            astring += "\n"
            astring += new_href[i]
            astring += "\n"
    astring = str(astring)
    return astring
if __name__ == '__main__':
    from linebot import LineBotApi, WebhookHandler
    from linebot.exceptions import InvalidSignatureError
    from linebot.models import *
    from linebot.models import TextSendMessage
    message = str(run())
    print(message)
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    line_bot_api.push_message(USERID,TextSendMessage(text='你可以開始了'))
    line_bot_api.push_message(USERID,TextSendMessage(text=message))
