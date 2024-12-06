import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    DB_URL = os.environ.get("DB_URL", "")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration

    START_TXT = """<b>ʜɪɪ {} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. 
    
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ 👇 ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ꜱᴇᴇ ᴍᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅꜱ 😁</b>"""
    
    SURPRISE_TXT = """<b>
ʜᴇʟʟᴏ ᴅᴇᴀʀ 👋 

ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ 😊. 
ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏғ ʏᴏᴜʀ ғɪʟᴇ. 
ᴀʟꜱᴏ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏꜱ ᴛᴏ ᴅᴏᴄᴜᴍᴇɴᴛꜱ ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛꜱ ᴛᴏ ᴠɪᴅᴇᴏꜱ 
ᴀʟꜱᴏ ᴛʜɪꜱ ʙᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴꜱ.
"""

    ABOUT_TXT = """<b>╭───────────⍟
🙍‍♂️ ᴍy ɴᴀᴍᴇ : {}
⚙️ ᴄʜɪʟʟɪɴɢ ᴏɴ : <a href="https://www.heroku.com/">ʜᴇʀᴏᴋᴜ</a>
🍿 ʙʀᴀɪɴ ғᴜᴇʟᴇᴅ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
🐍 ᴄᴏᴅɪɴɢ ᴍᴜsᴄʟᴇs : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ 3</a>
🙏🏻 ᴍʏ ᴄʀᴇᴀᴛᴏʀ : ʜᴀʀᴀ ʜᴀʀᴀ ᴍᴀʜᴀᴅᴇᴠ
🤡 ᴍʏ ᴍᴀɴᴀɢᴇʀ : <a href="https://telegram.me/harikushal">ᴄʀᴇᴀᴛᴏʀ</a>
╰───────────────⍟ """
    
    CHANNEL_TXT = """
ʜᴇʟʟᴏ ᴀʟʟ ʟᴏᴏᴋ ʙᴇʟᴏᴡ 👇 ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ꜱᴇᴇ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ. 

<b>ᴀʟꜱᴏ ɪᴏɪɴ ᴛʜᴇʀᴇ ☺️ ᴀɴᴅ ꜱᴜᴘᴘᴏʀᴛ ᴜꜱ 🎊</b>"""

    HELP_TXT = """
<u>🌌 <b>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b></u>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


<u>📑 <b>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ:- <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

<b>➜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <a href=https://t.me/TG_UPDATES1>old main channel</a>
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Kr_Movie2" -metadata author="@TG_UPDATES1" -metadata:s:s title="Subtitled By :- @Kr_Movie2" -metadata:s:a title="By :- @TG_UPDATES1" -metadata:s:v title="By:- @Kr_Movie2" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Kr_Movie2
"""
    
    METADATA_TXT = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>
For Example :-
<code>By @Kr_Movie2</code>
💬 For Any Help Contact @Harikushal"""
    
    PROGRESS_BAR = """<b>\n
ᴘʀᴏɢʀᴇss ʙᴀʀ 
🗃️ sɪᴢᴇ: {1} | {2}
⏳️ ᴅᴏɴᴇ : {0}%
🚀 sᴘᴇᴇᴅ: {3}/s
⏰️ ᴇᴛᴀ: {4}

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Hari_Search
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
</b>"""
