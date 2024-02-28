################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################
import os

from pyrogram.errors import *
from pyrogram.types import *
from telegraph import upload_file

from Mix import *

__modles__ = "Notes"
__help__ = """
Help Command Notes

• Perintah: <code>{0}save</code> [nama catatan] [balas pesan]
• Penjelasan: Untuk menyimpan catatan.

• Perintah: <code>{0}get</code> [nama catatan]
• Penjelasan: Untuk mengambil catatan.

• Perintah: <code>{0}clear</code> [nama catatan]
• Penjelasan: Untuk menghapus catatan.

• Perintah: <code>{0}notes</code>
• Penjelasan: Untuk melihat semua catatan.

• Untuk menggunakan inline button silahkan ketik :
<code>{0}markdown</code>
"""


def kontol_siapa(xi, tipe):
    return f"Mix/{xi}.{tipe}"


@ky.ubot("save", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gua = c.me.id
    cek = m.reply_to_message
    note_name, text, data_type, content = get_note_type(m)
    xx = await m.reply(f"{em.proses} <b>Processing...</b>")
    if not note_name:
        return await xx.edit(
            f"{em.gagal} <b>Gunakan format :</b> <code>save</code> [nama catatan] [balas ke pesan]."
        )

    if data_type == Types.TEXT:
        teks, _ = parse_button(text)
        if not teks:
            return await xx.edit(f"{em.gagal} <b>Teks tidak dapat kosong.</b>")
        udB.save_note(c.me.id, note_name, text, data_type, content)
    elif data_type in [Types.PHOTO, Types.VIDEO]:
        teks, _ = parse_button(text)
        file_type = "jpg" if data_type == Types.PHOTO else "mp4"
        xo = kontol_siapa(gua, file_type)
        mek = await c.download_media(cek, xo)
        xo_url = upload_file(mek)
        mmk = f"https://telegra.ph/{xo_url[0]}"
        udB.save_note(c.me.id, note_name, text, data_type, mmk)
        os.remove(xo)
    elif data_type in [
        Types.STICKER,
        Types.VIDEO_NOTE,
        Types.ANIMATED_STICKER,
        Types.VOICE,
    ]:
        udB.save_note(c.me.id, note_name, text, data_type, content)
    await xx.edit(
        f"{em.sukses} <b>Catatan <code>{note_name}</code> berhasil disimpan.</b>"
    )


@ky.ubot("get", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} <b>Processing...</b>")
    note = None
    if len(m.text.split()) >= 2:
        note = m.text.split()[1]
    else:
        await xx.edit(f"{em.gagal} <b>Berikan nama catatan !</b>")
        return

    getnotes = udB.get_note(c.me.id, note)
    teks = None
    if not getnotes:
        return await xx.edit(f"{em.gagal} <b>{note} tidak ada dalam catatan.</b>")

    if getnotes["type"] == Types.TEXT:
        teks, button = parse_button(getnotes.get("value"))
        button = build_keyboard(button)
        if button:
            button = InlineKeyboardMarkup(button)
        else:
            button = None
        if button:
            try:
                inlineresult = await c.get_inline_bot_results(
                    bot.me.username, f"get_note_ {note}"
                )
                await m.delete()
                await c.send_inline_bot_result(
                    m.chat.id,
                    inlineresult.query_id,
                    inlineresult.results[0].id,
                    reply_to_message_id=ReplyCheck(m),
                )
            except Exception as e:
                return await xx.edit(f"Error {e}")
        else:
            await m.reply(teks)

    elif getnotes["type"] == Types.PHOTO:
        teks, button = parse_button(getnotes.get("value"))
        button = build_keyboard(button)
        if button:
            button = InlineKeyboardMarkup(button)
        else:
            button = None
        if button:
            try:
                inlineresult = await c.get_inline_bot_results(
                    bot.me.username, f"get_note_ {note}"
                )
                await m.delete()
                await c.send_inline_bot_result(
                    m.chat.id,
                    inlineresult.query_id,
                    inlineresult.results[0].id,
                    reply_to_message_id=ReplyCheck(m),
                )
            except Exception as e:
                return await xx.edit(f"Error {e}")
        else:
            await c.send_photo(
                m.chat.id,
                getnotes["file"],
                caption=getnotes["value"],
                reply_to_message_id=ReplyCheck(m),
            )
    elif getnotes["type"] == Types.VIDEO:
        teks, button = parse_button(getnotes.get("value"))
        button = build_keyboard(button)
        if button:
            button = InlineKeyboardMarkup(button)
        else:
            button = None
        if button:
            try:
                inlineresult = await c.get_inline_bot_results(
                    bot.me.username, f"get_note_ {note}"
                )
                await m.delete()
                await c.send_inline_bot_result(
                    m.chat.id,
                    inlineresult.query_id,
                    inlineresult.results[0].id,
                    reply_to_message_id=ReplyCheck(m),
                )
            except Exception as e:
                return await xx.edit(f"Error {e}")
        else:
            await c.send_video(
                m.chat.id,
                getnotes["file"],
                caption=getnotes["value"],
                reply_to_message_id=ReplyCheck(m),
            )
    elif getnotes["type"] == Types.STICKER:
        await c.send_sticker(
            m.chat.id, getnotes["file"], reply_to_message_id=ReplyCheck(m)
        )
    elif getnotes["type"] == Types.VOICE:
        await c.send_voice(
            m.chat.id,
            getnotes["file"],
            caption=getnotes["value"],
            reply_to_message_id=ReplyCheck(m),
        )
    elif getnotes["type"] == Types.VIDEO_NOTE:
        await c.send_video_note(
            m.chat.id,
            getnotes["file"],
            # caption=getnotes["value"],
            reply_to_message_id=ReplyCheck(m),
        )
    elif getnotes["type"] == Types.ANIMATED_STICKER:
        await c.send_sticker(
            m.chat.id,
            getnotes["file"],
            # caption=getnotes["value"],
            reply_to_message_id=ReplyCheck(m),
        )
    else:
        if getnotes.get("value"):
            teks, button = parse_button(getnotes.get("value"))
            button = build_keyboard(button)
            if button:
                button = InlineKeyboardMarkup(button)
            else:
                button = None
        else:
            teks = None
            button = None
        if button:
            try:
                xi = await c.get_inline_bot_results(
                    bot.me.username, f"get_note_ {note}"
                )
                await m.delete()
                await c.send_inline_bot_result(
                    m.chat.id,
                    xi.query_id,
                    xi.results[0].id,
                    reply_to_message_id=ReplyCheck(m),
                )
            except Exception as e:
                await m.edit(
                    f"{e} An error has accured! Check your assistant for more information!"
                )
                return
        else:
            await c.send_media_group(
                m.chat.id,
                getnotes["file"],
                caption=teks,
                reply_to_message_id=ReplyCheck(m),
            )
    await xx.delete()


@ky.ubot("notes", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} <b>Processing...</b>")
    getnotes = udB.get_all_notes(c.me.id)
    if not getnotes:
        await xx.edit(f"{em.gagal} <b>Tidak ada catatan satupun!</b>")
        return
    rply = f"{em.alive} <b>Daftar Catatan:</b>\n"
    for x in getnotes:
        if len(rply) >= 1800:
            await xx.edit(rply)
            rply = f"{em.alive} <b>Daftar Catatan:</b>\n"
        rply += f"{em.sukses} <code>{x}</code>\n"

    await xx.edit(rply)


@ky.ubot("clear", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} <b>Processing...</b>")
    if len(m.text.split()) <= 1:
        return await xx.edit(f"{em.gagal} <b>Catatan apa yang perlu dihapus ?</b>")

    note = m.text.split()[1]
    getnote = udB.rm_note(c.me.id, note)
    if note not in getnote:
        return await xx.edit(
            f"{em.gagal} <b>Tidak ada catatan!</b>"
        )

    else:
        return await xx.edit(f"{em.sukses} <b>Catatan <code>{note}</code> berhasil dihapus!</b>")


@ky.inline("^get_note_")
async def _(c, iq):
    q = iq.query.split(None, 1)
    notetag = q[1]
    noteval = udB.get_note(user.me.id, notetag)
    if not noteval:
        return
    note, button = parse_button(noteval.get("value"))
    button = build_keyboard(button)
    if noteval["type"] in [Types.PHOTO, Types.VIDEO]:
        file_type = "jpg" if noteval["type"] == Types.PHOTO else "mp4"
        biji = noteval.get("file")

        if noteval["type"] == Types.PHOTO:
            await c.answer_inline_query(
                iq.id,
                cache_time=0,
                results=[
                    InlineQueryResultPhoto(
                        title="Note Photo",
                        photo_url=biji,
                        caption=note,
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                ],
            )
        elif noteval["type"] == Types.VIDEO:
            await c.answer_inline_query(
                iq.id,
                cache_time=0,
                results=[
                    InlineQueryResultVideo(
                        title="Note Video",
                        video_url=biji,
                        caption=note,
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                ],
            )
    elif noteval["type"] == Types.TEXT:
        await c.answer_inline_query(
            iq.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="Tombol Notes!",
                    input_message_content=InputTextMessageContent(note),
                    reply_markup=InlineKeyboardMarkup(button),
                )
            ],
        )
