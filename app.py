from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi("r1/7Xd4STB+4iTmui6ylkQhAI5/5J6tfHjGzbid5l1g/chxk6Aqw8mrEmrn7/4ZuKQlli5cwQREXrRr8Eq20MPB4ChUNI7Q8ARrLx7tf+w6GgNhZLzWsHzGTJXMp7RoFcI+zBgdB8cTgshaBh/HccgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler('9e32837ba7d824102992394dfeffda37')


@app.route("/")
def home():
    return 'home OK'

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='今天台北下著雨！'))


if __name__ == "__main__":
    app.run()
    