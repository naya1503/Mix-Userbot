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
__help__ = get_cgr("help_notes")


def kontol_siapa(xi, tipe):
    return f"Mix/{xi}.{tipe}"


@ky.ubot("save", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gua = c.me.id
    cek = m.reply_to_message
    note_name, text, data_type, content = get_note_type(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    if not note_name:
        return await xx.edit(cgr("nts_1").format(em.gagal, m.command))

    if data_type == Types.TEXT:
        teks, _ = parse_button(text)
        if not teks:
            return await xx.edit(cgr("nts_2").format(em.gagal))
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
    await xx.edit(cgr("nts_3").format(em.sukses, note_name))


@ky.ubot("get", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(cgr("proses").format(em.proses))
    note = None
    if len(m.text.split()) >= 2:
        note = m.text.split()[1]
    else:
        await xx.edit(cgr("nts_4").format(em.gagal))
        return

    getnotes = udB.get_note(c.me.id, note)
    teks = None
    if not getnotes:
        return await xx.edit(cgr("nts_5").format(em.gagal, note))

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
                return await xx.edit(cgr("err").format(em.gagal, e))
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
                return await xx.edit(cgr("err").format(em.gagal, e))
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
                return await xx.edit(cgr("err").format(em.gagal, e))
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
                await m.edit(cgr("err").format(em.gagal, e))
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
    xx = await m.reply(cgr("proses").format(em.proses))
    getnotes = udB.get_all_notes(c.me.id)
    if not getnotes:
        await xx.edit(cgr("nts_6").format(em.gagal))
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
    getnotes = udB.get_all_notes(c.me.id)
    getnote = udB.get_note(c.me.id, note)

    if note not in getnotes:
        await xx.edit(
            f"{em.gagal} <b>Catatan <code>{note}</code> tidak ada dalam daftar catatan.</b>"
        )
        return

    if not getnote:
        await xx.edit(f"{em.gagal} <b>Catatan <code>{note}</code> tidak ditemukan!</b>")
        return

    if not udB.rm_note(c.me.id, note):
        await xx.edit(
            f"{em.sukses} <b>Catatan <code>{note}</code> berhasil dihapus!</b>"
        )
        return

    await xx.edit(f"{em.sukses} <b>Catatan <code>{note}</code> berhasil dihapus!</b>")
