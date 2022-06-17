# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021
@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第一章 Line Bot申請與串接
Line Bot機器人串接與測試
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('kmRJwK0lUv3/NOQT3QwqO+tLV0c77quOM+QgO+ZoAaQLAp/Rar8nW9Yyd5biy/ygZEacENGElsGTuO8c2+I+jHolY0JN5/hVlfWfJIJwrwot1bPoGdXQif95x7PiDMqlxOQqXymEs56EXhMeLpbJswdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('8ac3e99312066d35645803542a4bd28a')

line_bot_api.push_message('U5b8aedc528e5ea2663cbc03fb4b89042', TextSendMessage(text='你可以開始了'))


import datetime
date = datetime.date.today()

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

href_list = []
header_list = []
new_header = []
new_href = []
ua = UserAgent()
user_agent = ua.random
headers = {'user-agent': user_agent}

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
dr.find_element(By.NAME,"email").send_keys("joe901007@yahoo.com.tw")  # 帳號
time.sleep(3)
dr.find_element_by_id("pass").send_keys("82585336")  # 密碼
dr.find_element_by_name("login").click()
time.sleep(3)
dr.get("https://www.facebook.com/groups/248305265374276")
length = 0
time.sleep(2)
        
        

for i in range(5): 	# 讓頁面滾動5次
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
    else:
        new_header.append(header_list[i])
        new_href.append(href_list[i])
string = ""
for i in range(len(new_header)):
    string += new_header[i]
    string += "\n"
    string += new_href[i]
    string += "\n"
        


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

 
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=string)
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message)
        )
       

        



#        else:
#         message = TextSendMessage(text=event.message.text)
#     if event.message.text == '本周新片':
#         r = requests.get('http://www.atmovies.com.tw/movie/new/')
#         r.encoding = 'utf-8'

#         soup = BeautifulSoup(r.text, 'lxml')
#         content = []
#         for i, data in enumerate(soup.select('div.filmTitle a')):
#             if i > 20:
#                 break
#             content.append(data.text + '\n' + 'http://www.atmovies.com.tw' + data['href'])

#         

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
