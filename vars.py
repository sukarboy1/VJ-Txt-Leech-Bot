# Don't Remove Credit Tg - @SONICKUWALSSCBOT
# website For Amazing Bot https://sonickuwalssc.blogspot.com/
# Ask Doubt on telegram @SONICKUWALUPDATEKANHA

from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

try:
    ADMINS=[]
    #auth_users id - 1234736828 1375282662
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
