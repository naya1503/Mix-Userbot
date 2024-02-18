import asyncio


from Mix.core import *
from team.nandev.class_ubot import Userbot, Bot
from config import *
from uvloop import install

user = Userbot(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
)

#git()
install()
heroku()
bot = Bot()

loop = asyncio.get_event_loop_policy()
loop2 = loop.get_event_loop()

from team import *