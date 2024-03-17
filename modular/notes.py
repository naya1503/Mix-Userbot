################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
 
 EH KONTOL BAJINGAN !! KALO MO PAKE DIKODE PAKE AJA BANGSAT!! GAUSAH APUS KREDIT NGENTOT
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
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    gua = c.me.id
    cek = m.reply_to_message
    note_name, text, data_type, content = get_note_type(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    if not note_name:
        return await xx.edit(cgr("nts_1").format(em.gagal, m.command))

    if data_type == Types.TEXT:
        teks, _ = text_keyb(ikb, text)
        udB.save_note(c.me.id, note_name, text, data_type, content)
    elif data_type in [Types.PHOTO, Types.VIDEO]:
        teks, _ = text_keyb(ikb, text)
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
async def _(c: nlx, m):
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
        teks, button = text_keyb(ikb, getnotes.get("value"))
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
        teks, button = text_keyb(ikb, getnotes.get("value"))
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
        teks, button = text_keyb(ikb, getnotes.get("value"))
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
        teks, button = text_keyb(ikb, getnotes.get("value"))
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
    return


@ky.ubot("notes", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(cgr("proses").format(em.proses))
    getnotes = udB.get_all_notes(c.me.id)
    if not getnotes:
        await xx.edit(cgr("nts_6").format(em.gagal))
        return
    rply = cgr("nts_7").format(em.sukses)
    for x in getnotes:
        if len(rply) >= 1800:
            await xx.edit(rply)
        rply += cgr("nts_8").format(x)

    await xx.edit(rply)
    return


@ky.ubot("clear", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(cgr("proses").format(em.proses))
    if len(m.text.split()) <= 1:
        return await xx.edit(cgr("nts_9").format(em.gagal))

    note = m.text.split()[1]
    getnotes = udB.get_all_notes(c.me.id)
    rmnot = udB.rm_note(c.me.id, note)

    if note not in getnotes and not rmnot:
        await xx.edit(cgr("nts_10").format(em.gagal, note))
        return
    else:
        await xx.edit(cgr("nts_11").format(em.sukses, note))
    return
