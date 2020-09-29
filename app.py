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

line_bot_api = LineBotApi("cQblRI5ktnRr5bHZuooaxrlWj50dgRWtO8TK1oPt0sjhskiSq9s27MyEDDhJZT5xKQlli5cwQREXrRr8Eq20MPB4ChUNI7Q8ARrLx7tf+w5o9OYcBPfI+TQYeyW5i1qauDDol2/j4IF6qbC+is50/wdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("85b99a197013166b3d0f12d24f0bba24")


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
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text)
    # )
    # TextSendMessage(text=event.message.text))
    text = event.message.text
    print(text)
    if text == 'Hi' or text == 'hi':
        reply_text = "嗨！今天過的好嗎？"
    elif text == '你好' or text == '妳好':
        reply_text = '逆豪，汪汪！'
    elif text == "我愛你" or text == "I love you.":
        reply_text = "真的嗎？我也超級超級喜歡你/妳！"
    else:
        reply_text = '嗨嗨～離放假只剩一哩路！'
    
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
    