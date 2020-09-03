from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw 
import re
import io
from textwrap import wrap
#пельмень - это мучная раковина, таящая мясную жемчужину.
def register(cb):
	cb(ZagMod())
	
class ZagMod(loader.Module):
	"""Riddle"""
	strings = {
		'name': 'Riddle'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def jzagcmd(self, message):
		""".jzag <реплай или свой текст>, загадка от жака"""
		
		ufr = requests.get("http://allfont.de/cache/fonts/open-sans_5f14bd2f3cd41e7b13ff8bc4177c9d06.ttf")
		f = ufr.content
		
		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		if not args:
			if not reply:
				await utils.answer(message, self.strings('usage', message))
				return
			else:
				txt = reply.raw_text
		else:
			txt = utils.get_args_raw(message)
		await message.edit("<b>Думаю...</b>")
		pic = requests.get("https://raw.githubusercontent.com/ggrnaaa/ftgm0du1es/master/SAVE_20200903_191442_1599149787811.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		text = "\n".join(wrap(txt, 20))
		t = text + "\n"
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 25, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+50, h+50), (0,0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((35, 35),t,(225,225,225),font=font, align='left')
		imtext.thumbnail((450, 320))
		w, h = 450, 320
		img.paste(imtext, (2,140), imtext)
		out = io.BytesIO()
		out.name = "out.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()


	async def szagcmd(self, message):
		""".szag <реплай или свой текст>, загадка от джобса"""
		
		ufr = requests.get("http://allfont.de/cache/fonts/open-sans_5f14bd2f3cd41e7b13ff8bc4177c9d06.ttf")
		f = ufr.content
		
		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		if not args:
			if not reply:
				await utils.answer(message, self.strings('usage', message))
				return
			else:
				txt = reply.raw_text
		else:
			txt = utils.get_args_raw(message)
		await message.edit("<b>Думаю...</b>")
		pic = requests.get("https://raw.githubusercontent.com/ggrnaaa/ftgm0du1es/master/SAVE_20200903_191448_1599160234310.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")

		W, H = img.size
		text = "\n".join(wrap(txt, 20))
		t = text + "\n"
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 25, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+50, h+50), (255,255,255,255))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((50, 50),t,(0,0,0),font=font, align='left')
		imtext.thumbnail((650, 280))
		w, h = 650, 280
		img.paste(imtext, (2,60), imtext)
		out = io.BytesIO()
		out.name = "out.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()
