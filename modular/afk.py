################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty
"""
################################################################

import time

from pyrogram import *
from pyrogram.types import *

from Mix import *
from Mix.core.waktu import get_time, put_cleanmode

__modles__ = "Afk"
__help__ = """
 Help Command Afk

• Perintah : <code>{0}afk or unafk</code> [reason]
• Penjelasan : Untuk mengaktifkan atau menonaktifkan mode afk.

• Perintah : <code>{0}afkdel</code> [on/off]
• Penjelasan : Untuk mengaktifkan hapus otomatis pesan afk anda.
"""


@ky.ubot("afk", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id = c.me.id
    if m.sender_chat:
        return await m.reply_text(
            f"{em.gagal} **Tidak dapat menggunakan akun channel.**"
        )
    if len(m.command) == 1 and not m.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(m.command) > 1 and not m.reply_to_message:
        _reason = (m.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(m.command) == 1 and m.reply_to_message.animation:
        _data = m.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(m.command) > 1 and m.reply_to_message.animation:
        _data = m.reply_to_message.animation.file_id
        _reason = (m.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(m.command) == 1 and m.reply_to_message.photo:
        await c.download_media(m.reply_to_message, file_name=f"{user_id}.jpg")
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(m.command) > 1 and m.reply_to_message.photo:
        await c.download_media(m.reply_to_message, file_name=f"{user_id}.jpg")
        _reason = m.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(m.command) == 1 and m.reply_to_message.video:
        await c.download_media(m.reply_to_message, file_name=f"{user_id}.mp4")
        details = {
            "type": "video",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(m.command) > 1 and m.reply_to_message.video:
        await c.download_media(m.reply_to_message, file_name=f"{user_id}.mp4")
        _reason = m.text.split(None, 1)[1].strip()
        details = {
            "type": "video",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(m.command) == 1 and m.reply_to_message.sticker:
        if m.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        elif m.reply_to_message.photo:
            await c.download_media(m.reply_to_message, file_name=f"{user_id}.jpg")
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await c.download_media(m.reply_to_message, file_name=f"{user_id}.mp4")
            details = {
                "type": "video",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(m.command) > 1 and m.reply_to_message.sticker:
        _reason = (m.text.split(None, 1)[1].strip())[:100]
        if m.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        elif m.reply_to_message.photo:
            await c.download_media(m.reply_to_message, file_name=f"{user_id}.jpg")
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await c.download_media(m.reply_to_message, file_name=f"{user_id}.mp4")
            details = {
                "type": "video",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    udB.add_afk(user_id, details)
    formatted_text = "{a} Sekarang Afk!!".format(
        a=em.warn,
    )
    send = await m.reply_text(formatted_text)
    await put_cleanmode(c.me.id, send.id)

"""
@ky.ubot("afkdel")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.command) == 1:
        return await m.reply_text(f"{em.gagal} Gunakan format : `afkdel` on/off.")
    chat_id = c.me.id
    state = m.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        udB.cleanmode_on(chat_id)
        await m.reply_text(f"{em.warn} Afk Delete Diaktifkan!")
    elif state == "off":
        udB.cleanmode_off(chat_id)
        await m.reply_text(f"{em.gagal} Afk Delete Dinonaktifkan!")
    else:
        await m.reply_text(f"{em.gagal} Gunakan format : `afkdel` on/off.")
"""

@ky.ubot("unafk", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id = c.me.id
    verifier, reasondb = udB.is_afk(user_id)
    if verifier:
        udB.remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = await get_time((int(time.time() - timeafk)))
            if afktype == "animation":
                send = (
                    await m.reply_animation(
                        data,
                        caption="**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**".format(
                            a=em.warn,
                            c=seenago,
                        ),
                    )
                    if str(reasonafk) == "None"
                    else await m.reply_animation(
                        data,
                        caption="**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**\n**Alasan : `{d}`**".format(
                            a=em.warn, c=seenago, d=reasonafk
                        ),
                    )
                )
            elif afktype == "photo":
                send = (
                    await m.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption="**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**".format(
                            a=em.warn,
                            c=seenago,
                        ),
                    )
                    if str(reasonafk) == "None"
                    else await m.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption="**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**\n**Alasan : `{d}`**".format(
                            a=em.warn,
                            c=seenago,
                            d=reasonafk,
                        ),
                    )
                )
            elif afktype == "video":
                send = (
                    await m.reply_video(
                        video=f"downloads/{user_id}.mp4",
                        caption="**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**".format(
                            a=em.warn,
                            c=seenago,
                        ),
                    )
                    if str(reasonafk) == "None"
                    else await m.reply_video(
                        video=f"downloads/{user_id}.mp4",
                        caption="**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**\n**Alasan : `{d}`**".format(
                            a=em.warn,
                            c=seenago,
                            d=reasonafk,
                        ),
                    )
                )
            elif afktype == "text":
                send = await m.reply_text(
                    "**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**".format(
                        a=em.warn, c=seenago
                    ),
                    disable_web_page_preview=True,
                )
            elif afktype == "text_reason":
                send = await m.reply_text(
                    "**{a} Online kembali!\nDurasi AFK! : `{c}` yang lalu.**\n**Alasan : `{d}`**".format(
                        a=em.warn, c=seenago, d=reasonafk
                    ),
                )
        except Exception:
            send = await m.reply_text(
                "**{a} Sedang AFK sejak : `{c}` yang lalu.**".format(
                    a=em.warn,
                    c=seenago,
                ),
                disable_web_page_preview=True,
            )
        await put_cleanmode(c.me.id, send.id)
        return


@user.on_message(
    filters.mentioned
    & ~filters.me & ~filters.bot & filters.incoming
)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    msg = ""
    verifier, reasondb = udB.is_afk(user.me.id)
    cek = udB.is_afk(user.me.id)
    if cek:
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = await get_time((int(time.time() - timeafk)))
            if afktype == "text":
                msg += "**{a} Sedang AFK sejak :** `{c}` yang lalu.".format(
                    a=em.warn, c=seenago
                )
            if afktype == "text_reason":
                msg += "**{a} Sedang AFK sejak :** `{c}` yang lalu.\n **Alasan:** `{d}`".format(
                    a=em.warn, c=seenago, d=reasonafk
                )
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await m.reply_animation(
                        data,
                        caption="**{a} Sedang AFK sejak :** `{c}` yang lalu.".format(
                            a=em.warn, c=seenago
                        ),
                    )
                else:
                    send = await m.reply_animation(
                        data,
                        caption="**{a} Sedang AFK sejak :** `{c}` yang lalu.\n **Alasan:** `{d}`".format(
                            a=em.warn, c=seenago, d=reasonafk
                        ),
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await m.reply_photo(
                        photo=f"downloads/{c.me.id}.jpg",
                        caption="**{a} Sedang AFK sejak :** `{c}` yang lalu.".format(
                            a=em.warn, c=seenago
                        ),
                    )
                else:
                    send = await m.reply_photo(
                        photo=f"downloads/{c.me.id}.jpg",
                        caption="**{a} Sedang AFK sejak :** `{c}` yang lalu.\n **Alasan:** `{d}`".format(
                            a=em.warn, c=seenago, d=reasonafk
                        ),
                    )
            if afktype == "video":
                if str(reasonafk) == "None":
                    send = await m.reply_video(
                        video=f"downloads/{c.me.id}.mp4",
                        caption="**{a} Sedang AFK sejak :** `{c}` yang lalu.".format(
                            a=em.warn, c=seenago
                        ),
                    )
                else:
                    send = await m.reply_video(
                        video=f"downloads/{c.me.id}.mp4",
                        caption="**{a} Sedang AFK sejak :** `{c}` yang lalu.\n **Alasan:** `{d}`".format(
                            a=em.warn, c=seenago, d=reasonafk
                        ),
                    )
        except Exception:
            msg += "**{a} Sedang AFK sejak :** `{c}` yang lalu.\n **Alasan:** `{d}`".format(
                a=em.warn, c=seenago, d=reasonafk
            )
    if msg != "":
        try:
            send = await m.reply_text(msg, disable_web_page_preview=True)
        except:
            pass
    try:
        await put_cleanmode(c.me.id, send.id)
    except:
        pass
