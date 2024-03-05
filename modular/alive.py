################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from Mix import DEVS, bot, get_cgr, ky, udB, user
from Mix.core.waktu import get_time, start_time

from .gcast import refresh_dialog

__modles__ = "Alive"
__help__ = get_cgr("help_alive")


@ky.ubot("alive", sudo=True)
async def _(c: user, m):
    try:
        x = await c.get_inline_bot_results(bot.me.username, "alive")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await m.reply(error)