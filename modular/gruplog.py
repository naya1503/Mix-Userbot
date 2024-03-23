################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio
import os

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *

from Mix import *

__modles__ = "Gruplog"
__help__ = get_cgr("help_gruplog")


@ky.ubot("gruplog", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(cgr("proses").format(em.proses))
    cek = c.get_arg(m)
    if cek.lower() == "on":
        if not TAG_LOG:
            await c.logger_grup()
            xx = await c.get_grup()
            ff = await c.export_chat_invite_link(int(xx.id))
            return await xx.edit(cgr("grplog_1").format(em.sukses, ff))
            ndB.set_key("TAG_LOG", int(xx.id))
        else:
            return await xx.edit(cgr("grplog_2").format(em.sukses))
    if cek.lower() == "off":
        if TAG_LOG:
            ndB.del_key("TAG_LOG")
            xx = await c.get_grup()
            await c.delete_supergroup(int(xx.id))
            return await xx.edit(cgr("grplog_3").format(em.gagal))
        else:
            return await xx.edit(cgr("grplog_4").format(em.gagal))
    else:
        return await xx.edit(cgr("grplog_5").format(em.gagal))


@ky.gc()
async def _(c, m):
    if not udB.get_var(nlx.me.id, "TAG_LOGGER"):
        return

    org = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    lenk = m.link
    media = None
    teks = None
    if m.caption:
        teks = cgr("grplog_6").format(m.chat.title, org, m.caption)
    else:
        teks = cgr("grplog_6").format(m.chat.title, org, m.text)
    donut = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(cgr("grplog_7"), url=lenk),
            ],
        ]
    )
    try:
        if m.photo:
            media = m.photo.file_id
            pat = await c.download_media(media, file_name=f"{m.from_user.id}.jpg")
            ret = await bot.send_photo(
                TAG_LOG,
                photo=pat,
                caption=teks,
                reply_markup=donut,
            )
            os.remove(pat)
        elif m.video:
            media = m.video.file_id
            pat = await c.download_media(media, file_name=f"{m.from_user.id}.mp4")
            ret = await bot.send_video(
                TAG_LOG,
                video=pat,
                caption=teks,
                reply_markup=donut,
            )
            os.remove(pat)
        else:
            ret = await bot.send_message(
                TAG_LOG, teks, disable_web_page_preview=True, reply_markup=donut
            )

    except FloodWait as e:
        await asyncio.sleep(e.value)
        ret = await bot.send_message(
            TAG_LOG, teks, disable_web_page_preview=True, reply_markup=donut
        )
    tag_add(ret.id, m.chat.id, m.id)


@ky.replog()
async def _(c: nlx, m):
    reply_ = m.reply_to_message
    chat, msg = who_tag(reply_.id)
    media = None
    if chat and msg:
        try:
            if m.photo:
                media = m.photo.file_id
                pat = await c.download_media(media, file_name=f"{m.from_user.id}.jpg")
                await c.send_photo(
                    chat,
                    photo=pat,
                    caption=m.text or m.caption,
                    reply_to_message_id=msg,
                )
                os.remove(pat)
            elif m.video:
                media = reply_.video.file_id
                pat = await c.download_media(media, file_name=f"{m.from_user.id}.mp4")
                await c.send_video(
                    chat,
                    video=pat,
                    caption=m.text or m.caption,
                    reply_to_message_id=msg,
                )
                os.remove(pat)
            else:
                await c.send_message(chat, m.text, reply_to_message_id=msg)
        except Exception as e:
            await m.reply(f"{e}")
            await c.send_message(chat, m.text, reply_to_message_id=msg)
            return
