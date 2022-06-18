import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
date = datetime.date.today()
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import *
from linebot import LineBotApi
from linebot.models import TextSendMessage
import time
# 自動推播
import re
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('hasav1yTh4IWtiMEsnArqYIP2yvLc7fciTgFDo84I090TLH3kjZwJ0f+V8oPT6c8WDg+ISp/lUw6ewAvQJFStEabiEG0V4zhD0jv+vWr3DcWCgm90vbcNBX4PazqOf5QmxmegujhUm5PlafJ3Z5QtwdB04t89/1O/w1cDnyilFU=')
# 請填入您的ID
yourID = 'U8e9ac6911787e11c263670660337a474'
new_header = []
new_href = []
line_bot_api.push_message(yourID, TextSendMessage(text='你可以開始了'))
#line_bot_api = LineBotApi('npHX/BAgLnGzrMDuTXPdwYZOmMc6S7zZzh1FOaxjgrKuloHrShOzRNV3A8ImRST1SVoCSCbHjwjEYF5zKpnL4M25wJE4paVUu3vWdXIsVDcXHvRwbz3xh6s/SdQeacX0lTsyLFVzsmiezV7MdjhPigdB04t89/1O/w1cDnyilFU=')
'''@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text

    if re.match('抽獎',message):
      for i in len(new_href):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = new_header[i] + new_href[i]))'''
href_list = []
header_list = []
ua = UserAgent()
user_agent = ua.random
headers = {'user-agent': user_agent}

#class="bi6gxh9e"是貼文裡面文字
#class_="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"是貼文本身
#save_message = ''
"""
Line Bot聊天機器人
第三章 互動回傳功能
推播push_message與回覆reply_message
"""
# 必須放上自己的Channel Access Token
'''line_bot_api = LineBotApi('npHX/BAgLnGzrMDuTXPdwYZOmMc6S7zZzh1FOaxjgrKuloHrShOzRNV3A8ImRST1SVoCSCbHjwjEYF5zKpnL4M25wJE4paVUu3vWdXIsVDcXHvRwbz3xh6s/SdQeacX0lTsyLFVzsmiezV7MdjhPigdB04t89/1O/w1cDnyilFU=')
# 請填入您的ID
yourID = 'U8e9ac6911787e11c263670660337a474'
# 主動推播訊息
line_bot_api.push_message(yourID, 
                          TextSendMessage(text='安安您好！早餐吃了嗎？'))
# 用迴圈推播訊息
for i in [1,2,3,4,5]:
    line_bot_api.push_message(yourID, 
                              TextSendMessage(text='我們來倒數：'+str(i)))
    time.sleep(1)'''

save_message = []
def run():
  global dr
  chrome_options = webdriver.ChromeOptions()
  prefs = {"profile.default_content_setting_values.notifications" : 2}
  chrome_options.add_experimental_option("prefs",prefs)
  chrome_options.add_argument(("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
+"AppleWebKit/537.36 (KHTML, like Gecko)"
+"Chrome/87.0.4280.141 Safari/537.36"))
  dr = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
  
  dr.maximize_window()
  dr.get('http://www.facebook.com')

if __name__ == '__main__':
  run()
dr.find_element(By.NAME,"email").send_keys("joe901007@yahoo.com.tw")
time.sleep(3)
dr.find_element_by_id("pass").send_keys("82585336")
dr.find_element_by_name("login").click()
time.sleep(3)
dr.get("https://www.facebook.com/groups/248305265374276")
length = 0
time.sleep(2)

for i in range(5): 	# 讓頁面滾動x次
  #article = []
  dr.execute_script("window.scrollTo(0,document.body.scrollHeight);")# document.body.scrollHeight
  time.sleep(6)	 # 等待2秒鐘讓頁面讀取
  soup = BeautifulSoup(dr.page_source, "html.parser")

  frames = soup.find_all(role="article")#很多包涵內文跟文章
    
  
  attr1 = {'data-ad-preview':"message"} #找文章
  more = 0 #看查看更多點及次數
  for article in frames:
    
        t_content = article.find(attrs = attr1) #內文 有很多行
        
        
        #for line in t_content:
        if t_content != None: 
              
           if '抽' in t_content.text or '問卷' in t_content.text: #抽獎
                    time.sleep(5)
                    
                    tag = article.find('a',{'class':"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"})
                    href_list.append(tag['href'])
                    try:
                      
                      header_list.append(t_content.text[:30])  #跑出前三是個字
                    except:
                      header_list.append('xxx')
                   
                    time.sleep(2)
print(len(header_list),len(href_list),sep=',')          

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

string = ""
for i in range(len(new_header)):
  string += new_header[i]
  string += "\n"
  string += new_href[i]
  string += "\n"



# 主動推播訊息

  #print(i)
line_bot_api.push_message(yourID, 
                          TextSendMessage(text=string))
# 用迴圈推播訊息
