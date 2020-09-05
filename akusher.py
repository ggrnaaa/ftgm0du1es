#код спиздила с модуля который сколько раз я тебе повторял автор не ругайся пожалуйста ты крутой а я люблю вареники с творогом и вишней
import telethon
from .. import loader, utils
import os
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import re
import io
from io import BytesIO
from textwrap import wrap
import random

def register(cb):
    cb(AkshMod())

class AkshMod(loader.Module):
    """Акушер"""
    strings = {'name': 'Акушер'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def akcmd(self, message):
        """.ak и реплай на картинку"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = haha(pic)
            await message.client.send_file(message.to_id, what)

def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def haha(image):
    pics = requests.get("https://0x0.st/i6m3.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (1, 1), 410)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None



