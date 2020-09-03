from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def register(cb):
	cb(RandomPhrMod())


class RandomPhrMod(loader.Module):
	"""Random phrases with @vsratoslavbot"""

	strings = {'name': 'RandomPhrases'}

	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()

	async def phrcmd(self, message):
		""".phr <reply to photo>"""
		
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("Reply to photo, bro")
			return
		try:
			photo = reply.media.photo
		except:
			await message.edit("Only photo please")
		
		args = utils.get_args_raw(message)
				
				
		chat = '@vsratoslavbot'
		await message.edit('@vsratoslavbot <code>thinks...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=1066090937))
				blank = conv.wait_event(events.NewMessage(incoming=True, from_users=1066090937))
				await message.client.send_file(chat, photo, caption=args)
				blank = await blank
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Unblock</code>@vsratoslavbot')
				return

			await message.delete()
			await message.client.send_file(message.to_id, response.media)
			