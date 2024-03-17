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

__modles__ = "Ping"
__help__ = get_cgr("help_ping")


@ky.ubot("ping", sudo=True)
@ky.devs("mping")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    start = datetime.now()
    await c.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    upnya = await get_time((time() - start_time))
    _ping = cgr("ping_1").format(
        em.ping, str(delta_ping).replace(".", ","), em.pong, upnya
    )
    await m.reply(_ping)
