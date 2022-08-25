# @KEK_Projects

import bot
import pyromod.listen
from pyrogram import Client
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from func import subscribed, encode, decode, get_messages



app = Client(
    "bot",
    api_id=C.API_ID,
    api_hash=C.API_HASH,
    bot_token=C.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="database"),
)

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    text = "<b>Anda harus bergabung Channel/Group Untuk menggunakan saya\n\nSilahkan Klik Bergabung Dulu</b>"
    message_text = message.text
    try:
        command, argument = message_text.split()
        text = text + f" <b>dan <a href='https://t.me/{client.username}?start={argument}'>coba lagi</a></b>"
    except ValueError:
        pass
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Bergabunglah dengan Saluran", url = client.UPDATE_CHANNEL)]])
    await message.reply(
        text = text,
        reply_markup = reply_markup,
        quote = True,
        disable_web_page_preview = True
    )
