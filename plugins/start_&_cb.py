from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from helper.database import db
from config import Config, Txt
import humanize
from time import sleep


@Client.on_message(filters.private & filters.command("surprise"))
async def start(client, message):

    if message.from_user.id in Config.BANNED_USERS:
        await message.reply_text("Sorry, You are banned.")
        return

    user = message.from_user
    await db.add_user(client, message)
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton('🔒 ꜱᴜʀᴘʀɪꜱᴇ', callback_data='start'),
    ],[    
        InlineKeyboardButton('💰 ᴅᴏɴᴀᴛᴇ', callback_data='haridonate'),
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)

    if not Config.STRING_SESSION:
        if file.file_size > 2000 * 1024 * 1024:
            return await message.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ")

    try:
        text = f"""**__ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ.?__**\n\n**ғɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n\n**ғɪʟᴇ sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 sᴛᴀʀᴛ ʀᴇɴᴀᴍᴇ", callback_data="rename")],
                   [InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 sᴛᴀʀᴛ ʀᴇɴᴀᴍᴇ", callback_data="rename")],
                   [InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "surprise":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('🔒 ꜱᴜʀᴘʀɪꜱᴇ', callback_data='start'),
            ]])
        )
    elif data == "start":
        await query.message.edit_text(
            text=Txt.SURPRISE_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('👀 ꜱᴇᴇ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ', callback_data='channel'),
            ], [
                InlineKeyboardButton('❄️ ᴀʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('❗ ʜᴇʟᴘ', callback_data='help')
            ]])
        )  
        
    elif data == "haridonate":
        await query.message.edit_text(
            text=Txt.DONATE_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('👨‍💻 ᴏᴡɴᴇʀ', url='https://t.me/+nDTaoJGRKJcxYmZl'),
            ]])
        )   
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✘ ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton("⟪ ʙᴀᴄᴋ", callback_data="start")
            ]])
        )
    elif data == "channel":
        await query.message.edit_text(
            text=Txt.CHANNEL_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ɢʀᴏᴜᴘ 𝟷 🔎',  url='https://t.me/+nDTaoJGRKJcxYmZl'),
            ],[
                InlineKeyboardButton('ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ɢʀᴏᴜᴘ 𝟸 🔎',  url='https://t.me/+_Ss2e1bjdn5lZGRl'),
            ],[
                InlineKeyboardButton('ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ɢʀᴏᴜᴘ 𝟹 🔎',  url='https://t.me/HK_Movies_Request'),
            ],[ 
                InlineKeyboardButton('ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ 📥',  url='https://t.me/+Il2xwa1M-g82Zjhl'),
                InlineKeyboardButton('ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 🪄',  url='https://t.me/TG_BOTS_UPDATE'),
            ],[
                InlineKeyboardButton('ʙᴀᴄᴋᴜᴘ ᴄʜᴀɴɴᴇʟ 🔥',  url='https://t.me/+0e9UjA2Thn83MGQ1'),
                InlineKeyboardButton('ʙᴀᴄᴋᴜᴘ ɢʀᴏᴜᴘ 🪡',  url='https://t.me/Kr_Movie2'),
            ],[
                InlineKeyboardButton("« ʙᴀᴄᴋ »", callback_data="start")
            ]])
        )
    
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✘ ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton("⟪ ʙᴀᴄᴋ", callback_data="start")
            ]])
        )

    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
