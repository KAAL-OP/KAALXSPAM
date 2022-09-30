from pyrogram import filters 
from pyrogram import Client as app
from pyrogram.types import Message
from Spam import SUDO_USERS, HNDLR, DEVS
import asyncio

@app.on_message(filters.user(DEVS) & filters.command(["inviteall"], prefixes=HNDLR))
@app.on_message(filters.user(SUDO_USERS) & filters.command(["inviteall"], prefixes=HNDLR))
@app.on_message(filters.me & filters.command(["inviteall"], prefixes=HNDLR))
async def copy_members(client, message):
# by : @ZDDDU 
      chat_id = message.text.split(None, 2)[1]
      # by : @ZDDDU 
      m = await message.reply("~ Processing...")
      # by : @ZDDDU 
      c = 0
      # by : @ZDDDU 
      async for member in app.get_chat_members(chat_id):
      # by : @ZDDDU 
            try:
            # by : @ZDDDU 
              await app.add_chat_members(message.chat.id, member.user.id)
              # by : @ZDDDU 
              c += 1
              # by : @ZDDDU 
            except Exception:
            # by : @ZDDDU 
              pass
      try:
      # by : @ZDDDU 
        await m.delete()
        # by : @ZDDDU 
        await message.delete()
        # by : @ZDDDU 
        await message.reply(f" Done {c}")
        # by : @ZDDDU 
      except:
      # by : @ZDDDU 
        pass
# by : @ZDDDU 
print("🟢")
# by : @ZDDDU 
# by : @ZDDDU 
# by : @ZDDDU 
