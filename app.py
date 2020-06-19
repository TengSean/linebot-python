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
#         return 'TextSendMessage function'
        return TextSendMessage(text='TextSendMessage function')
    elif message == 'ImageSendMessage':
#         pass
#         return 'ImageSendMessage function'
        return ImageSendMessage(
                    original_content_url='https://i.imgur.com/Uschheg.jpg',
                    preview_image_url='https://i.imgur.com/Uschheg.jpg'
                )
    elif message == 'VideoSendMessage':
#         pass
#         return 'VideoSendMessage function'
        return VideoSendMessage(
                    original_content_url='https://im.ezgif.com/tmp/ezgif-1-2a754b6badc2.mp4',
                    preview_image_url='https://i.imgur.com/cUkNhls.png'
                )
    elif message == 'AudioSendMessage':
#         pass 
#         return 'AudioSendMessage function '
        return AudioSendMessage(
                    original_content_url='https://www.myinstants.com/media/sounds/ringtone_20.mp3',
                    duration=3000
                )
    elif message == 'LocationSendMessage':
#         pass 
#         return 'LocationSendMessage function'
        return LocationSendMessage(
                    title='Demo Location',
                    address='清大',
                    latitude=24.796297,
                    longitude=120.996638
                )
    elif message == 'StickerSendMessage':
#         reference pdf: https://developers.line.biz/media/messaging-api/messages/sticker_list.pdf
#         pass
#         return 'StickerSendMessage function'
        return  StickerSendMessage(
                    package_id='1',
                    sticker_id='1'
                )
    elif message == 'ImagemapSendMessage':
#         pass https://i.imgur.com/4NYu7s2.png
#         return 'ImagemapSendMessage function'
        return ImagemapSendMessage(
                    base_url='https://i.imgur.com/4NYu7s2.png',
                    alt_text='this is an imagemap',
                    base_size=BaseSize(height=1040, width=1040),
                    actions=[
                        URIImagemapAction(
                            link_uri='https://i.imgur.com/4NYu7s2.png',
                            area=ImagemapArea(
                                x=0, y=0, width=520, height=1040
                            )
                        ),
                        MessageImagemapAction(
                            text='hello',
                            area=ImagemapArea(
                                x=520, y=0, width=520, height=1040
                            )
                        )
                    ]
                )
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
        return TextSendMessage(text='''You can test following cmd in this bot:
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
        ''')
    else:
        return TextSendMessage(text=message)


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#     message = TextSendMessage(text=event.message.text)
#     logging.info(message)
    message = filter_message(message=event.message.text)
#     t = ', '.join(os.listdir('./'))
#     message = TextSendMessage(text=message)
#     message = os.listdir('./')
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
