################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

import asyncio
import random

from pyrogram import *
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import *

from Mix import *

__modles__ = "SangMata"
__help__ = get_cgr("help_sangmata")


@ky.ubot("sg", sudo=True)
@ky.devs("siapa")
async def _(c, m):
    em = Emojik()
    em.initialize()

    if len(m.command) < 2 and not m.reply_to_message:
        return await m.reply(cgr("sangmat_1").format(em.gagal))

    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        return await m.reply(
            f"{em.gagal} <b>DILARANG KERAS MENGGUNAKAN FITUR INI KEPADA SEORANG DEV MIX-USERBOT!</b>"
        )

    if (
        m.command[0] == "sg"
        and m.reply_to_message
        and m.reply_to_message.from_user.id in DEVS
    ):
        return await m.reply(
            f"{em.gagal} <b>DILARANG KERAS MENGGUNAKAN FITUR INI KEPADA SEORANG DEV MIX-USERBOT!</b>"
        )

    if m.reply_to_message:
        args = m.reply_to_message.from_user.id
    else:
        args = m.command[1]

    proses = await m.reply(cgr("proses").format(em.proses))

    if args:
        try:
            user = await c.get_users(f"{args}")
        except Exception:
            return await proses.edit(cgr("sangmat_2").format(em.gagal))

    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)

    try:
        a = await c.send_message(sg, f"{user.id}")
        await a.delete()
    except Exception as e:
        return await proses.edit(e)

    await asyncio.sleep(1)

    async for stalk in c.search_messages(a.chat.id):
        if stalk.text == None:
            continue
        if not stalk:
            await m.reply(cgr("sangmat_3").format(em.gagal))
        elif stalk:
            await m.reply(cgr("sangmat_4").format(em.sukses, stalk.text))
            break

    try:
        user_info = await c.resolve_peer(sg)
        await c.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await proses.delete()
