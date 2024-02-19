import asyncio

from team.nandev.class_ubot import Bot, Userbot

from config import *
from Mix.core import *

user = Userbot(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
)

git()
heroku()
bot = Bot()


from team import *


def fexid():
    emo = Emojii()
    emo.initialize()


fex = fexid()

ping = fex.ping
pong = fex.pong
proses = fex.proses
alive = fex.alive
gagal = fex.gagal
sukses = fex.sukses
profil = fex.profil
warn = fex.warn
block = fex.block
