################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio
import os

from pyrogram import *
from pyrogram.errors import *

from Mix import *

__modles__ = "Gruplog"
__help__ = get_cgr("help_gruplog")


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


@ky.ubot("gruplog", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} Processing...")
    cek = c.get_arg(m)
    logs = udB.get_logger(c.me.id)
    if cek.lower() == "on":
        if not logs:
            await c.logger_grup()
            xx = await c.get_grup()
            ff = await c.export_chat_invite_link(int(xx.id))
            return await xx.edit(
                f"{em.sukses} **Log Group Berhasil Diaktifkan :\n\n{ff}**"
            )
            udB.set_logger(c.me.id, int(xx.id))
        else:
            return await xx.edit(f"{em.sukses} **Log Group Anda Sudah Aktif.**")
    if cek.lower() == "off":
        if logs:
            udB.rem_logger(c.me.id)
            xx = await c.get_grup()
            await c.delete_supergroup(int(xx.id))
            return await xx.edit(f"{em.gagal} **Log Group Berhasil Dinonaktifkan.**")
        else:
            return await xx.edit(f"{em.gagal} **Log Group Anda Sudah Dinonaktifkan.**")
    else:
        return await xx.edit(
            f"{em.gagal} **Format yang anda berikan salah. silahkan gunakan <code>gruplog on or off</code>.**"
        )


async def _(c, m):
    db = udB.get_logger(user.me.id)
    if not db:
        return
    org = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    lenk = m.link
    media = None
    teks = None
    if m.caption:
        teks = f"**📨 New Message\n\n• Grup : {m.chat.title}\n• Pengguna : {org}\n• Pesan: {m.caption}**"
    else:
        teks = f"""
**📨 New Message
• Grup : {m.chat.title}
• Pengguna : {org}
• Pesan: {m.text}**
"""
    donut = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Replied Message", url=lenk),
            ],
        ]
    )
    try:
        if m.photo:
            media = m.photo.file_id
            pat = await c.download_media(media, file_name=f"{m.from_user.id}.jpg")
            ret = await bot.send_photo(
                db,
                photo=pat,
                caption=teks,
                reply_markup=donut,
            )
            os.remove(pat)
        elif m.video:
            media = m.video.file_id
            pat = await c.download_media(media, file_name=f"{m.from_user.id}.mp4")
            ret = await bot.send_video(
                db,
                video=pat,
                caption=teks,
                reply_markup=donut,
            )
            os.remove(pat)
        else:
            ret = await bot.send_message(
                db, teks, disable_web_page_preview=True, reply_markup=donut
            )

    except FloodWait as e:
        await asyncio.sleep(e.value)
        ret = await bot.send_message(
            db, teks, disable_web_page_preview=True, reply_markup=donut
        )
    tag_add(ret.id, m.chat.id, m.id)


# @ky.replog()
async def _(c: user, m):
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


@user.on_message(
    filters.private & filters.incoming & ~filters.me & ~filters.bot & ~filters.service)
async def _(c: user, m):
    lg = ndB.get_key("TAG_LOG")
    if lg is None:
        return
    if m.chat.id == 777000:
        return
    if LOG_CHATS_.RECENT_USER != m.chat.id:
        LOG_CHATS_.RECENT_USER = m.chat.id
        if LOG_CHATS_.NEWPM:
            await LOG_CHATS_.NEWPM.edit(
                LOG_CHATS_.NEWPM.text.replace(
                    "**💌 #NEW_MESSAGE**", f" • `{LOG_CHATS_.COUNT}` **Pesan**"
                )
            )
            LOG_CHATS_.COUNT = 0
        LOG_CHATS_.NEWPM = await c.send_message(
            lg,
            f"💌 <b>#MENERUSKAN #PESAN_BARU</b>\n<b> • Dari :</b> {m.from_user.mention}\n<b> • User ID :</b> <code>{m.from_user.id}</code>",
            parse_mode=enums.ParseMode.HTML,
        )
    try:
        async for oiu in c.search_messages(m.chat.id, limit=1):
            await oiu.forward(lg)
        LOG_CHATS_.COUNT += 1
    except BaseException:
        pass
