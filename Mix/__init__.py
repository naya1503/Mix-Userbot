import asyncio

from team.nandev import Userbot, Bot

from config import *

user = Userbot(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
    in_memory=True,
)


bot = Bot()

from team import *