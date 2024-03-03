################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio
import os
import time
from gc import get_objects
from time import time

from pyrogram import *
from pyrogram.types import *

from Mix import Emojik, bot, cgr, ky, progress, user

COPY_ID = {}

nyolong_jalan = False


__modles__ = "Content"
__help__ = """
 Bantuan Untuk Copy

• Perintah : <code>{0}copy</code> [link]
• Penjelasan : Untuk mengambil pesan melalui link telegram.
  """

#### TomiXtomi


async def gas_download(g, c: user, inf, m):
    msg = m.reply_to_message or m
    text = g.caption or ""

    if g.photo:
        media = await c.download_media(
            g,
            progress=progress,
            progress_args=(
                inf,
                time(),
                "Download Photo",
                g.photo.file_id,
            ),
        )
        await c.send_photo(
            m.chat.id,
            media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await inf.delete()
        os.remove(media)

    elif g.animation:
        media = await c.download_media(
            g,
            progress=progress,
            progress_args=(
                inf,
                time(),
                "Download Animation",
                g.animation.file_id,
            ),
        )
        await c.send_animation(
            m.chat.id,
            animation=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await inf.delete()
        os.remove(media)

    elif g.voice:
        media = await c.download_media(
            g,
            progress=progress,
            progress_args=(inf, time(), "Download Voice", g.voice.file_id),
        )
        await c.send_voice(
            m.chat.id,
            voice=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await inf.delete()
        os.remove(media)

    elif g.audio:
        media = await c.download_media(
            g,
            progress=progress,
            progress_args=(
                inf,
                time(),
                "Download Audio",
                g.audio.file_id,
            ),
        )
        thumbnail = await c.download_media(g.audio.thumbs[-1]) or None
        await c.send_audio(
            m.chat.id,
            audio=media,
            duration=g.audio.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
        )
        await inf.delete()
        os.remove(media)
        os.remove(thumbnail)

    elif g.document:
        media = await c.download_media(
            g,
            progress=progress,
            progress_args=(
                inf,
                time(),
                "Download Document",
                g.document.file_id,
            ),
        )
        await c.send_document(
            m.chat.id,
            document=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await inf.delete()
        os.remove(media)

    elif g.video:
        media = await c.download_media(
            g,
            progress=progress,
            progress_args=(
                inf,
                time(),
                "Download Video",
                g.video.file_name,
            ),
        )
        thumbnail = await c.download_media(g.video.thumbs[-1]) or None
        await c.send_video(
            m.chat.id,
            video=media,
            duration=g.video.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
        )
        await inf.delete()
        os.remove(media)
        os.remove(thumbnail)


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


@ky.ubot("copy", sudo=True)
async def _(c: user, m):
    global nyolong_jalan
    em = Emojik()
    em.initialize()
    msg = m.reply_to_message or m
    inf = await m.reply(cgr("proses").format(em.proses))
    link = c.get_arg(m)
    if not link:
        return await inf.edit(cgr("cpy_1").format(em.gagal, m.comand))

    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])

        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
            try:
                g = await c.get_messages(chat, msg_id)
                try:
                    await g.copy(m.chat.id, reply_to_message_id=msg.id)
                    await inf.delete()
                except Exception:
                    await gas_download(g, c, inf, m)
            except Exception as e:
                await inf.edit(str(e))
        else:
            chat = str(link.split("/")[-2])
            try:
                g = await c.get_messages(chat, msg_id)
                await g.copy(m.chat.id, reply_to_message_id=msg.id)
                await inf.delete()
            except Exception:
                try:
                    nyolong_jalan = True
                    text = f"get_msg {id(m)}"
                    x = await c.get_inline_bot_results(bot.me.username, text)
                    results = await c.send_inline_bot_result(
                        m.chat.id,
                        x.query_id,
                        x.results[0].id,
                        reply_to_message_id=msg.id,
                    )
                    COPY_ID[c.me.id] = int(results.updates[0].id)
                    await inf.delete()
                    nyolong_jalan = False
                except Exception as error:
                    await inf.edit(f"{str(error)}")

    else:
        await inf.edit(cgr("cpy_2").format(em.sukses))


@ky.inline("^get_msg")
async def _(c, iq):
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="message",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text=cgr("klk_1"),
                                    callback_data=f"copymsg_{int(iq.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTexxxessageContent(cgr("cpy_3")),
                )
            )
        ],
    )


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


@ky.ubot("cancel_copy", sudo=True)
async def _(c, m):
    global nyolong_jalan

    if not nyolong_jalan:
        return await m.reply_text(
            f"{c.gagal} <b>Tidak ada penyolongan konten berlangsung.</b>"
        )
    nyolong_jalan = False
    await m.delete()
