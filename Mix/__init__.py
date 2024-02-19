import asyncio

from team.nandev.class_ubot import Bot, Userbot

from config import *
from Mix.core import *

user = Userbot(
    name="user",
    api=api,
    api_hash=api_hash,
    session_string=session,
)

git()
heroku()
bot = Bot()


from team import *


#def fexid():
    #emo = Emojii()
   # emo.initialize()
 #   return emo


#fex = fexid()

ping = "<emoji id=5269563867305879894>🏓</emoji>"
pong = "<emoji id=6183961455436498818>🥵</emoji>"
proses = "<emoji id=6113844439292054570>🔄</emoji>"
gagal = "<emoji id=6113872536968104754>❌</emoji>"
sukses = "<emoji id=6113647841459047673>✅</emoji>"
profil = "<emoji id=5373012449597335010>👤</emoji>"
alive = "<emoji id=6127272826341690178>⭐</emoji>"
warn = "<emoji id=6172475875368373616>❗️</emoji>"
block = "<emoji id=5240241223632954241>🚫</emoji>"
