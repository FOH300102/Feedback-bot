from configs import UPDATE_CHANNEL
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(UPDATE_CHANNEL, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + UPDATE_CHANNEL
            else:
                chat_info = await bot.get_chat(UPDATE_CHANNEL)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/654ddaf472f18b799600b.jpg", caption=f"» ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [ᴅᴇᴠɪʟs ʜᴇᴀᴠᴇɴ]({link}) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [ᴅᴇᴠɪʟs ʜᴇᴀᴠᴇɴ]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🥺 ᴅᴇᴠɪʟs ʜᴇᴀᴠᴇɴ 🥺", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the UPDATE_CHANNEL chat : {UPDATE_CHANNEL} !")
