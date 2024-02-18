import asyncio
from Mix.core import *
from team.nandev.class_ubot import Userbot, Bot
from config import *



user = Userbot(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
)

git()
heroku()
bot = Bot()

loop = asyncio.get_event_loop_policy()
event_loop = loop.get_event_loop()
asyncio.set_event_loop(event_loop)

from team import *