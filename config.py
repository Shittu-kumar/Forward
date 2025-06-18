# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "20114039")
    API_HASH = environ.get("API_HASH", "87297b8f3cc8fc9bbce591ad30da5896")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7711849714:AAEcnio5LrvkwkxbGYo_53UnPIv25ENLWCE") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8172163893').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://ssmemes163:mwWPwSoo73h8XRoo@cluster0.uc5ph6w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002511678727'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002500606405") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
