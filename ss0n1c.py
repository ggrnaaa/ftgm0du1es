from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw 
import re
import io
from textwrap import wrap
#обосри себя сам, пока тебя не обосрал кто-то другой
def register(cb):
	cb(SsMod())
	
class SsMod(loader.Module):
	"""ssonic"""
	strings = {
		'name':'ssonic'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def ssovcmd(self, message):
		""".ssov реплай или свой текст"""
		
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
		await message.edit("<b>...</b>")
		pic = requests.get("https://raw.githubusercontent.com/ggrnaaa/ftgm0du1es/master/sonic/IMG_20201009_215534_245.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		text = "\n".join(wrap(txt, 40))
		t = text + "\n"
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 55, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+70, h+70), (0,0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((35, 35),t,(225,225,225),font=font, align='left')
		imtext.thumbnail((750, 570))
		w, h = 750, 570
		img.paste(imtext, (5,140), imtext)
		out = io.BytesIO()
		out.name = "out.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()


	async def ssavcmd(self, message):

		""".ssav реплай или свой текст"""

		
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
		await message.edit("<b>...</b>")
		pic = requests.get("https://raw.githubusercontent.com/ggrnaaa/ftgm0du1es/master/sonic/IMG_20201010_215005_786.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		text = "\n".join(wrap(txt, 40))
		t = text + "\n"
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 55, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+70, h+70), (0,0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((35, 35),t,(225,225,225),font=font, align='left')
		imtext.thumbnail((750, 570))
		w, h = 750, 570
		img.paste(imtext, (5,140), imtext)
		out = io.BytesIO()
		out.name = "out.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()
		

	async def ssaycmd(self, message):

		""".ssay реплай или свой текст"""
		
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
		await message.edit("<b>...</b>")
		pic = requests.get("https://raw.githubusercontent.com/ggrnaaa/ftgm0du1es/master/sonic/IMG_20201009_215530_082.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		text = "\n".join(wrap(txt, 40))
		t = text + "\n"
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 55, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+70, h+70), (0,0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((35, 35),t,(225,225,225),font=font, align='left')
		imtext.thumbnail((750, 540))
		w, h = 750, 540
		img.paste(imtext, (460,130), imtext)
		out = io.BytesIO()
		out.name = "out.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()
