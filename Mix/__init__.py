import asyncio

from pyrogram import Client

from config import *
from Mix.core import *
from Mix.mix_client import *

git()
heroku()
bot = Bot()
nlx = Userbot()
"""
nlx = Client(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
    device_model="Mix-Userbot",
    proxy=dict(scheme="socks5", hostname=proxy_host, port=22),
 )
 """


from team import *
from thegokil import DEVS, NO_GCAST

from langs import *
