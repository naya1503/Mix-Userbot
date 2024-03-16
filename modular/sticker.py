################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty || William || Gojo_Satoru
 • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
 
"""
################################################################

import asyncio
import os

from pyrogram.errors import *
from pyrogram.file_id import *
from pyrogram.raw.functions.messages import *
from pyrogram.raw.functions.stickers import *
from pyrogram.raw.types import *

from Mix import Emojik, bot, cgr, get_cgr, ky, ndB, nlx

__modles__ = "Sticker"
__help__ = get_cgr("help_stick")

LOG_ME = ndB.get_key("TAG_LOG")


@ky.ubot("gstik|getstiker|getsticker", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    stick = rep.sticker
    if not rep:
        await m.reply(cgr("st_1").format(em.gagal))
        return
    else:
        if stick.is_video == True:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.mp4")
            await rep.reply_document(
                document=pat,
                caption=cgr("st_2").format(
                    em.sukses, stick.emoji, em.alive, stick.file_id
                ),
            )
        elif stick.is_animated == True:
            await m.reply(cgr("st_1").format(em.gagal))
            return

        else:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.png")
            await rep.reply_document(
                document=pat,
                caption=cgr("st_2").format(
                    em.sukses, stick.emoji, em.alive, stick.file_id
                ),
            )
        return
    os.remove(pat)


@ky.ubot("unkang", sudo=False)
async def _(self: nlx, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    await nlx.unblock_user(bot.me.username)
    if not rep:
        await m.reply(cgr("st_3").format(em.gagal))
        return
    if rep.sticker:
        pros = await m.reply(cgr("proses").format(em.proses))
        ai = await nlx.forward_messages(bot.me.username, m.chat.id, message_ids=rep.id)
        await nlx.send_message(bot.me.username, "/unkang", reply_to_message_id=ai.id)
        await asyncio.sleep(0.5)
        if await resleting(m) == "Stiker berhasil dihapus dari paket Anda.":
            await pros.edit(cgr("st_4").format(em.sukses))
            return
        else:
            await pros.edit(cgr("st_5").format(em.gagal))
            return
    else:
        await m.reply(cgr("st_6").format(em.gagal))


@ky.ubot("kang", sudo=False)
async def _(self: nlx, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    await nlx.unblock_user(bot.me.username)
    if not rep:
        await m.reply(cgr("st_7").format(em.gagal))
        return
    await nlx.send_message(bot.me.username, "/kang")
    pros = await m.reply(cgr("proses").format(em.proses))
    ai = await nlx.forward_messages(bot.me.username, m.chat.id, message_ids=rep.id)
    await nlx.send_message(bot.me.username, "/kang", reply_to_message_id=ai.id)
    await asyncio.sleep(5)
    async for tai in nlx.search_messages(
        bot.me.username, query="Sticker Anda Berhasil Dibuat!", limit=1
    ):
        await asyncio.sleep(5)
        await tai.copy(m.chat.id)
    await pros.delete()
    ulat = await nlx.resolve_peer(bot.me.username)
    await nlx.invoke(DeleteHistory(peer=ulat, max_id=0, revoke=True))
    return


async def resleting(m):
    return [x async for x in nlx.get_chat_history(bot.me.username, limit=1)][0].text
