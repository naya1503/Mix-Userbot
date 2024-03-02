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

loop = asyncio.get_event_loop_policy().get_event_loop()

from team import *

from langs import cgr
