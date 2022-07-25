from config import *
from web_crawler import *
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, abort, render_template
from selenium.webdriver.common.by import By
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from liffpy import LineFrontendFramework as LIFF, ErrorResponse
from linebot.models import *
from linebot import LineBotApi
from linebot.models import TextSendMessage
# 必須放上自己的Channel Access Token
liff_api = LIFF(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
#add_liff = liff_api.add(view_type="compact",view_url="https://pypi.org/project/liffpy/")
app = Flask(__name__,template_folder='templates')
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
yourID = USERID
line_bot_api.push_message(yourID, TextSendMessage(text='你可以開始了，只要打"抽獎"，就幫您找出台大交流版抽獎貼文連結'))

#line_bot_api = LineBotApi('npHX/BAgLnGzrMDuTXPdwYZOmMc6S7zZzh1FOaxjgrKuloHrShOzRNV3A8ImRST1SVoCSCbHjwjEYF5zKpnL4M25wJE4paVUu3vWdXIsVDcXHvRwbz3xh6s/SdQeacX0lTsyLFVzsmiezV7MdjhPigdB04t89/1O/w1cDnyilFU=')
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  msg =event.message.text
  if '抽獎' in msg :
    message = run()
    message = str(message)
    line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
