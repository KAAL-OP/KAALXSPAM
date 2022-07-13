

from Spam import (DEVS, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(DEVS) & filters.command(["join"], prefixes=HNDLR))
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["join"], prefixes=HNDLR))
async def join(xspam: Client, e: Message):
    chat = e.text[6:]
    if chat.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
      await xspam.join_chat(chat)
      await e.reply_text("**Join Successfully ✅ **")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    if LOGS_CHANNEL:
         try:
             await xspam.send_message(LOGS_CHANNEL, f"Joined New Chat \n\n Chat: {chat} \n Cmd By User: {e.from_user.id}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.user(DEVS) & filters.command(["leave"], prefixes=HNDLR))
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["leave"], prefixes=HNDLR))
async def leave(xspam: Client, e: Message):
    Kaal = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        chat = Kaal[0]
        try:
           await xspam.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    else:
        chat = e.chat.id
        ok = e.from_user.id
        if int(chat) == int(ok):
            return await e.reply_text(f"Usage: {HNDLR}leave <chat username or id> or {HNDLR}leave (type in Group for Direct leave)")
        if int(chat) == -1001359155814:
              return e.reply_text("**Error**")
        try:
           await xspam.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
        if LOGS_CHANNEL:
           try:
                await xspam.send_message(LOGS_CHANNEL, f"Leaved Chat \n\n Chat: {chat} \n Cmd By User: {e.from_user.id}")
           except Exception as a:
             print(a)
             pass
