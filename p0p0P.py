from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
#как же хочется тяяяночку худенькую бледную не очень высооокую

def register(cb):
    cb(PoopMod())


class PoopMod(loader.Module):
    """хахахаха я назвала eго какашки вот это прикол"""

    strings = {'name': 'pipa'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def plcmd(self, message):
        """.pl реплай на фотокарточку."""
        
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("на фотокарточку реплай блин")
            return
        try:
            photo = reply.media.photo
        except:
            await message.edit("на фотокарточку!!!")
        
        args = utils.get_args_raw(message)
                
                
        chat = '@PoolsEverywhereBot'
        await message.edit('<code>...</code>')
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=719058307))
                await message.client.send_file(chat, photo, caption=args)
                response = await response
            except YouBlockedUserError:
                await message.reply('<code>разблокируй</code>@PoolsEverywhereBot')
                return

            await message.delete()
            await message.client.send_file(message.to_id, response.media)
            
    async def switchcmd(self, message):
        """.switch — все режимы бота."""
        
        args = utils.get_args_raw(message)
        if args:
          chat = '@PoolsEverywhereBot'
          async with message.client.conversation(chat) as conv:
              try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=719058307))
                await message.client.send_message(chat,str(args))
                response = await response
                if response.text=="что-то пошло не так, попробуйте еще раз чуть позднее":
                  return await message.edit("такого режима не существует дебил напиши .switch")
              except YouBlockedUserError:
                  await message.reply('<code>разблокируй</code>@PoolsEverywhereBot')
                  return

              await message.edit(f"<b>{response.text}</b>")
        else:
          await message.edit('<b>Что бы сменить передний план, пиши:</b>\n<code>.switch</code> <режим>\n\n<b>Режимы:</b>\n1. <code>Десант</code>\n2. <code>Бассейны 🏊‍♂</code>\n3. <code>Китайская стена</code>\n4. <code>JoJo</code>\n5. <code>Evangelion</code>\n6. <code>YOU DIED</code>\n7. <code>Дед с батей...</code>\n8. <code>Топ кросоверов</code>\n9. <code>Капустин</code> (фото с лицом)')