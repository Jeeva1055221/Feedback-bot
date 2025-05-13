import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 22977776))

    API_HASH = str(os.environ.get("API_HASH", "2ac7223d720bdeec757cbc88ced57224"))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", "7869073583:AAFFNhECe4jwa_OZTPVTm5TgDuhTwEMArM0"))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 7544529898))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7544529898").split())

    START = str(os.environ.get("START_TEXT", "<b> Dᴇᴀʀ Usᴇʀs 🍁 I am CloudXBotz ADMIN Support📢\n\n✪ How can I Help You? Need Help /help </b> "))

    HELP = str(os.environ.get("HELP_TEXT", "<b>Hᴇʟʟᴏ 🙋‍♂️ Tʜɪs  Is Oғғɪᴄɪᴀʟ Bᴏᴛ Fᴏʀ Rᴇǫᴜᴇsᴛɪɴɢ Sᴛᴀғғ Fʀᴏᴍ Tʜᴇ Aᴅᴍɪɴ💫 Oғ @Thirai_HDQ & @CloudxAdmin_Bot\n\n【 𝐌𝐨𝐯𝐢𝐞 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐅𝐨𝐫𝐦𝐚𝐭 👇 】\n ➤ Uncharted\n ➤ Uncharted 2022 ✔️\n\n【 𝐖𝐞𝐛 𝐒𝐞𝐫𝐢𝐞𝐬 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐅𝐨𝐫𝐦𝐚𝐭 👇 】\n ➤ Loki S01\n ➤ Loki S01E04\n\nGroup Link 🔎:https://t.me/+U2mWbtvr_PU4OTI9\n\n\n📌Rᴇǫᴜᴇsᴛᴇᴅ Mᴏᴠɪᴇ Wɪʟʟ Bᴇ Uᴘᴅᴀᴛᴇᴅ ᴡWɪᴛʜ Iɴ 𝟷ʜʀ Iғ Aᴠᴀɪʟᴀʙʟᴇ📌.\n\n🎁 <u>Pʀᴇᴍɪᴜᴍ Fᴇᴀᴛᴜʀᴇs</u> :\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n\nIғ Yᴏᴜ Aɴʏ Dᴏᴜʙᴛ Tᴇxᴛ Iɴ Bᴇʟᴏᴡ✍\n\n\nThank You,\nRegards\n@Thirai_HDQ & @CloudXbotz \nThank You,</b>"))

    DONATE = str(os.environ.get("DONATE_TEXT", "Dᴇᴀʀ Usᴇʀs 🍁"))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", "https://telegra.ph/file/8a6d4ed449d76c394d8be.jpg"))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/CloudXbotz"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/+Bs3lkePlgs44NjI1"))

    DB_URL = str(os.environ.get("DB_URL", "mongodb+srv://jeevanantham8157:1055221@heartai.9wl5t.mongodb.net/?retryWrites=true&w=majority&appName=HeartAI"))
    
    DB_NAME = str(os.environ.get("DB_NAME", "feedbackbot"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002691480602"))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))

