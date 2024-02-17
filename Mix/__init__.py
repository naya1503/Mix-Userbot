import asyncio


from Mix.core import *
from team.nandev.class_ubot import Userbot, Bot
from config import *


user = Userbot(
    name="user",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session,
    in_memory=True,
)


#bot = Bot()

class Bot2(Client):
    def __init__(self, **kwargs):
        super().__init__(name="bot", **kwargs)
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token or udB.get_token(owner_id)
        self.in_memory = False

    def on_message(self, filters=None, group=99):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def on_callback_query(self, filters=None, group=99):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()

bot = Bot2()

from team import *