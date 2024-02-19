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

emoji = user.Emojii()


def a():
    return emoji["ping"]()


def b():
    return emoji["pong"]()


def c():
    return emoji["proses"]()


def d():
    return emoji["sukses"]()


def e():
    return emoji["gagal"]()


def f():
    return emoji["profil"]()


def g():
    return emoji["alive"]()


def h():
    return emoji["warn"]()


def i():
    return emoji["block"]()


ping = a()
pong = b()
proses = c()
sukses = d()
gagal = e()
profil = f()
alive = g()
warn = h()
block = i()
