from msilib.schema import DrLocator
import os
from selenium import webdriver
#20220618版本 上網查如何heroku爬蟲
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
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
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
import re
new_header = []
new_href = []
href_list = []
header_list = []
# -*- coding: utf-8 -*-
app = Flask(__name__)
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('hasav1yTh4IWtiMEsnArqYIP2yvLc7fciTgFDo84I090TLH3kjZwJ0f+V8oPT6c8WDg+ISp/lUw6ewAvQJFStEabiEG0V4zhD0jv+vWr3DcWCgm90vbcNBX4PazqOf5QmxmegujhUm5PlafJ3Z5QtwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('9c9bf00c6a2bbb8cef9ef817d43aead1')
line_bot_api.push_message('U8e9ac6911787e11c263670660337a474', TextSendMessage(text='你可以開始了'))
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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):   
    def get_chrome():
        global dr
        
        op= webdriver.ChromeOptions()
        
        op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        op.add_argument("--headless")
        op.add_argument("--disable-dev-shm-usage")
        op.add_argument("--no-sandbox")
        dr = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)
        dr.maximize_window()
        dr.get('http://www.facebook.com')
        '''
        # avoid detection 好孩子先不要 ^.<
        op.add_argument('--disable-infobars')
        op.add_experimental_option('useAutomationExtension', False)
        op.add_experimental_option("excludeSwitches", ["enable-automation"])
        '''
    if __name__ == '__main__' and event.message.text == '抽獎':
        get_chrome()
    dr.find_element(By.NAME,"email").send_keys("joe901007@yahoo.com.tw")  # 帳號
    time.sleep(3)
    dr.find_element_by_id("pass").send_keys("82585336")  # 密碼
    dr.find_element_by_name("login").click()
    time.sleep(3)
    dr.get("https://www.facebook.com/groups/248305265374276")
    time.sleep(2)
    for i in range(5): 	# 讓頁面滾動5次
            #article = []
            dr.execute_script("window.scrollTo(0,document.body.scrollHeight);")# document.body.scrollHeight
            time.sleep(6)	 # 等待2秒鐘讓頁面讀取
            soup = BeautifulSoup(dr.page_source, "html.parser")

            frames = soup.find_all(role="article")#很多包涵內文跟文章
                
            
            attr1 = {'data-ad-preview':"message"} #找文章
            for article in frames:
                
                    t_content = article.find(attrs = attr1) #內文 有很多行
                    
                    
                    #for line in t_content:
                    if t_content != None: 
                        
                        if '抽' in t_content.text or '問卷' in t_content.text: #抽獎
                                    time.sleep(5)
                                    tag = article.find('a',{'class':"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"})
                                    href_list.append(tag['href'])
                                    try:
                                    
                                        header_list.append(t_content.text[:30])  #跑出前三十個字
                                    except:
                                        header_list.append('xxx')
                                    
                                    time.sleep(2)
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
            message = TextSendMessage(text=string)
            line_bot_api.reply_message(event.reply_token, message)
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
