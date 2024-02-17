import asyncio

from aiohttp import ClientSession

from team.nandev.class_ubot import Userbot, Bot
from config import *

aiohttpsession = ClientSession()


user = Userbot(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
    in_memory=True,
)


bot = Bot()

from team import *