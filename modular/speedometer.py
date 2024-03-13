################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping

from Mix import *
from Mix.core.waktu import get_time, start_time

__modles__ = "SpeedTest"
__help__ = "Speedometer"


@ky.ubot("speedtest|speed", sudo=True)
async def _(c: user, m):
    try:
        x = await c.get_inline_bot_results(bot.me.username, "speed")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id, reply_to_message_id=ReplyCheck(m))
    except Exception as error:
        await m.reply(error)