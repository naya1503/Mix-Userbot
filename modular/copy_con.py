################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import os
import time
from time import time

from Mix import Emojik, bot, cgr, get_cgr, ky, nlx, progress

COPY_ID = {}

nyolong_jalan = False


__modles__ = "Content"
__help__ = get_cgr("help_copy")

#### TomiXtomi


async def gas_download(g, c: nlx, inf, m):
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


@ky.ubot("copy", sudo=True)
async def _(c: nlx, m):
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


@ky.ubot("cancel_copy", sudo=True)
async def _(c, m):
    global nyolong_jalan

    if not nyolong_jalan:
        return await m.reply_text(
            f"{c.gagal} <b>Tidak ada penyolongan konten berlangsung.</b>"
        )
    nyolong_jalan = False
    await m.delete()
