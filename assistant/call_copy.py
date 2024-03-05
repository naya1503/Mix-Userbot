
################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################
import asyncio
from gc import get_objects

from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *

from Mix import *
from modular.copy_con import nyolong_jalan

@ky.callback("copymsg_")
async def _(c, cq):
    global nyolong_jalan
    try:
        q = int(cq.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        await m._c.unblock_user(bot.me.username)
        await cq.edit_message_text(cgr("proses_1"))
        copy = await m._c.send_message(bot.me.username, f"/copy {m.text.split()[1]}")
        msg = m.reply_to_message or m
        await asyncio.sleep(1.5)
        await copy.delete()
        nyolong_jalan = True
        async for g in m._c.search_messages(bot.me.username, limit=1):
            await m._c.copy_message(
                m.chat.id, bot.me.username, g.id, reply_to_message_id=msg.id
            )
            await m._c.delete_messages(m.chat.id, COPY_ID[m._c.me.id])
            await g.delete()
            nyolong_jalan = False
    except Exception as e:
        await callback_query.edit_message_text(cgr("err_1").format(e))
        