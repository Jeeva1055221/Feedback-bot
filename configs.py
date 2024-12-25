import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 16023154))

    API_HASH = str(os.environ.get("API_HASH", "c216393ab439dd055858680916a3444b"))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", "8084082805:AAEVFYl9JFVYgHRWRE04USrjnR3AKoh8sb8"))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1397269319))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1397269319").split())

    START = str(os.environ.get("START_TEXT", "Hi🙋‍♂️  <a href=https://t.me/{}>{}</a>\n\n Hello {first}\n\n I am CloudXBotz ADMIN Support📢\n\n✪ How can I Help You? Need Help /help "))

    HELP = str(os.environ.get("HELP_TEXT", "<b>Hᴇʟʟᴏ !{} Tʜɪs  Is Oғғɪᴄɪᴀʟ Bᴏᴛ Fᴏʀ Rᴇǫᴜᴇsᴛɪɴɢ [⚒️Staff⚒️] Fʀᴏᴍ Tʜᴇ ADMIN💫 😎 Oғ @Thirai_HDQ & @CloudxAdmin_Bot\n\n【 𝐌𝐨𝐯𝐢𝐞 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐅𝐨𝐫𝐦𝐚𝐭 👇 】\n ➤ Uncharted\n ➤ Uncharted 2022 ✔️\n\n【 𝐖𝐞𝐛 𝐒𝐞𝐫𝐢𝐞𝐬 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐅𝐨𝐫𝐦𝐚𝐭 👇 】\n ➤ Loki S01\n ➤ Loki S01E04\n\n<blockquote>Group Link 🔎:https://t.me/+U2mWbtvr_PU4OTI9</blockquote>\n\n\n📌Rᴇǫᴜᴇsᴛᴇᴅ Mᴏᴠɪᴇ Wɪʟʟ Bᴇ Uᴘᴅᴀᴛᴇᴅ ᴡWɪᴛʜ Iɴ 𝟷ʜʀ Iғ Aᴠᴀɪʟᴀʙʟᴇ📌.\n\n🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n\nIғ Yᴏᴜ Aɴʏ Dᴏᴜʙᴛ Tᴇxᴛ Iɴ Bᴇʟᴏᴡ✍\n\n\nThank You,\nRegards\n@Thirai_HDQ & @CloudxAdmin_Bot &☣️Mooderator☣️ 👇\nThank You,</b>"))

    DONATE = str(os.environ.get("DONATE_TEXT", "pklinkzzadmin@ybl"))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", "https://telegra.ph/file/8a6d4ed449d76c394d8be.jpg"))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/CloudXbotz"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/+Bs3lkePlgs44NjI1"))

    DB_URL = str(os.environ.get("DB_URL", "mongodb+srv://techbots203:jXjEjUeBZnQJu6zU@feedbackbot.plubg.mongodb.net/?retryWrites=true&w=majority&appName=feedbackbot"))
    
    DB_NAME = str(os.environ.get("DB_NAME", "feedbackbot"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001740524004"))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))

