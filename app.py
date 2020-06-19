from flask import Flask, request, abort

import logging
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('XV1X7KidmK44Bs1oKK8JCshs028vWypnmKpcKV0Xv/GGUplLnrccpEBF3YWHqXGXjiqYb+rCIQU3CoZCEKonzERWWuSx3z+/nnx6dRGMUA1LsXe+7CHxqOGHpM8PbPRKt8Ubn68+5WhjhTpPQjwPSQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0d8a150467c7c3629bd50fe6e49a8605')

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

help_dict = {


}


def filter_message(message):
    if message == 'TextSendMessage':
#         pass
        return 'TextSendMessage function'
    elif message == 'ImageSendMessage':
#         pass
        return 'ImageSendMessage function'
    elif message == 'VideoSendMessage':
#         pass
        return 'VideoSendMessage function'
    elif message == 'AudioSendMessage':
#         pass
        return 'AudioSendMessage function '
    elif message == 'LocationSendMessage':
#         pass
        return 'LocationSendMessage function'
    elif message == 'StickerSendMessage':
#         pass
        return 'StickerSendMessage function'
    elif message == 'ImagemapSendMessage':
#         pass
        return 'ImagemapSendMessage function'
    elif message == 'ButtonsTemplate':
#         pass
        return 'ButtonsTemplate function '
    elif message == 'ConfirmTemplate':
#         pass
        return 'ConfirmTemplate function'
    elif message == 'CarouselTemplate':
#         pass
        return 'CarouselTemplate function'
    elif message == 'ImageCarouselTemplate':
#         pass
        return 'ImageCarouselTemplate function'
    elif message == 'help':
        return '''You can test following cmd in this bot:
                'TextSendMessage'
                'ImageSendMessage'
                'VideoSendMessage'
                'AudioSendMessage'
                'LocationSendMessage'
                'StickerSendMessage'
                'ImagemapSendMessage'
                'ButtonsTemplate'
                'ConfirmTemplate'
                'CarouselTemplate'
                'ImageCarouselTemplate'
        '''
    else:
        return message


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#     message = TextSendMessage(text=event.message.text)
#     logging.info(message)
    message = filter_message(message=event.message.text)
#     t = ', '.join(os.listdir('./'))
    message = TextSendMessage(text=message)
#     message = os.listdir('./')
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
