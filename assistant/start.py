################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from Mix import *
import asyncio
import os
import time
from gc import get_objects
from time import time

from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *

COPY_ID = {}

nyolong_jalan = False

def clbk_strt():
    return okb(
        [
            [
                (cgr("asst_3"), "clbk.bhsa"),
            ],
        ],
        False,
        "close_asst",
    )


def clbk_strto():
    return okb(
        [
            [
                (cgr("ttup"), "clbk.info"),
            ],
        ],
        False,
        "close_asst",
    )


@ky.bots("start")
async def _(c, m):
    udB.add_served_user(m.from_user.id)
    owner_nih = user.me.id
    user_name = f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name} {m.from_user.last_name or ''}</a>"
    ts_1 = cgr("asst_1").format(user_name)
    ts_2 = cgr("asst_2").format(user_name, user.me.mention)
    if m.from_user.id == owner_nih:
        await m.reply(ts_1, reply_markup=clbk_strt())
    else:
        await m.reply(ts_2, reply_markup=clbk_strto())


@ky.bots("copy")
async def _(c, m):
    if m.from_user.id != user.me.id:
        return
    xx = await m.reply("Tunggu Sebentar...")
    link = user.get_arg(m)
    if not link:
        return await xx.edit(f"<b><code>{m.text}</code> [link]</b>")
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            g = await c.get_messages(chat, msg_id)
            await g.copy(m.chat.id)
            await xx.delete()
        except Exception as error:
            await xx.edit(error)
    else:
        await xx.edit("Link tidak valid.")
