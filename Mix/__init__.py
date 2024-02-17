import asyncio


from Mix.core import *
from team.nandev.class_ubot import Userbot, Bot2
from config import *


user = Userbot(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
    in_memory=True,
)


bot = Bot2()

from team import *