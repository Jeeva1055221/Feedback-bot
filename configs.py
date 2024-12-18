import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 16023154))

    API_HASH = str(os.environ.get("API_HASH", "c216393ab439dd055858680916a3444b"))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", "8084082805:AAEVFYl9JFVYgHRWRE04USrjnR3AKoh8sb8"))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1397269319))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1397269319").split())

    START = str(os.environ.get("START_TEXT", "Hi"))

    HELP = str(os.environ.get("HELP_TEXT", "welcome my bot"))

    DONATE = str(os.environ.get("DONATE_TEXT", "please donate @pkremo"))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", "please donate2 @pkremo"))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/cloudbotz"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/+Bs3lkePlgs44NjI1"))

    DB_URL = str(os.environ.get("DB_URL", "mongodb+srv://techbots203:jXjEjUeBZnQJu6zU@feedbackbot.plubg.mongodb.net/?retryWrites=true&w=majority&appName=feedbackbot"))
    
    DB_NAME = str(os.environ.get("DB_NAME", "feedbackbot"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001740524004"))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))

