import asyncio

import pytgcalls
from team.nandev.class_ubot import Bot, Userbot

from config import *
from Mix.core import *

# part of https://github.com/thehamkercat/Telegram_VC_Bot

CLIENT_TYPE = pytgcalls.GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
PLAYOUT_FILE = "input.raw"
PLAY_LOCK = asyncio.Lock()
OUTGOING_AUDIO_BITRATE_KBIT = 128

git()
heroku()
bot = Bot()
user = Userbot()


from team import *

from langs import *
