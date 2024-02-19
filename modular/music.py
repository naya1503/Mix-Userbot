################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 @ CREDIT : NAN-DEV
"""
################################################################

from asyncio import QueueEmpty
from gc import get_objects
from random import randint

from pyrogram import *
from pyrogram.errors import QueryIdInvalid
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.types import *
from pytgcalls.exceptions import NoActiveGroupCall, NotInGroupCallError
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio,
                                                  HighQualityVideo)
from team.nandev import queues
from team.nandev.class_pytgc import *
from yt_dlp import YoutubeDL

from Mix import *

__modles__ = "Music"
__help__ = """
Help Command Music

• Perintah: <code>{0}play</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}end</code>
• Penjelasan: Untuk mengakhiri voice chat grup.

• Perintah: <code>{0}skip</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}pause</code>
• Penjelasan: Untuk mengakhiri voice chat grup.
"""


@ky.ubot("play", sudo=True)
async def _(c, m):
    if m.reply_to_message:
        if len(m.command) < 2:
            chat_id = m.chat.id
        else:
            chat_id = int(m.text.split()[1])
        if m.reply_to_message.audio or m.reply_to_message.voice:
            if chat_id in daftar_join:
                return await m.reply("<b>Ada proses yang sedang berlangsung...</b>")
            daftar_join.append(chat_id)
            _play_ = await m.reply_to_message.reply("<b>❏ Processing Audio...</b>")
            dl = await c.download_media(m.reply_to_message)
            link = m.reply_to_message.link
            if chat_id in c.call_py.calls:
                pos = await queues.put(chat_id, file=AudioPiped(dl, HighQualityAudio()))
                await _play_.delete()
                __play__ = await m.reply_to_message.reply(
                    f"<b>❏ <a href={link}>Audio</a> Antrian » {pos}</b>",
                    disable_web_page_preview=True,
                )
                await m.delete()
                daftar_join.remove(chat_id)
            else:
                await c.call_py.join_group_call(
                    chat_id,
                    AudioPiped(dl, HighQualityAudio()),
                )
                await _play_.delete()
                __play__ = await m.reply_to_message.reply(
                    f"<b>❏ Memutar <a href={link}>Audio</a></b>",
                    disable_web_page_preview=True,
                )
                await m.delete()
                daftar_join.remove(chat_id)
        if m.reply_to_message.video or m.reply_to_message.document:
            if chat_id in daftar_join:
                return await m.reply("<b>Ada proses yang sedang berlangsung...</b>")
            daftar_join.append(chat_id)
            _play_ = await m.reply_to_message.reply("<b>❏ Processing Video...</b>")
            dl = await c.download_media(m.reply_to_message)
            link = m.reply_to_message.link
            if chat_id in c.call_py.calls:
                pos = await queues.put(
                    chat_id,
                    file=AudioVideoPiped(dl, HighQualityAudio(), HighQualityVideo()),
                )
                await _play_.delete()
                __play__ = await m.reply_to_message.reply(
                    f"<b>❏ <a href={link}>Video</a> Antrian » {pos}</b>",
                    disable_web_page_preview=True,
                )
                await m.delete()
                daftar_join.remove(chat_id)
            else:
                await c.call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(dl, HighQualityAudio(), HighQualityVideo()),
                )
                await _play_.delete()
                __play__ = await m.reply_to_message.reply(
                    f"<b>❏ Memutar <a href={link}>Video</a></b>",
                    disable_web_page_preview=True,
                )
                await m.delete()
                daftar_join.remove(chat_id)
    else:
        if len(m.text.split()) < 2:
            return await m.reply_text(
                "<b>Silakan masukkan judul lagu atau video.</b>",
            )
        if "-1001" not in m.text:
            query = f"_yts {id(m)}"
            chat_id = m.chat.id
        else:
            query = f"_x {id(m)}"
            chat_id = int(m.text.split()[1])
        if chat_id in daftar_join:
            return await m.reply("<b>Ada proses yang sedang berlangsung...</b>")
        daftar_join.append(chat_id)
        infomsg = await m.reply_text("<b>❏ Searching...</b>")
        x = await c.get_inline_bot_results(bot.me.username, query)
        try:
            await m.reply_inline_bot_result(x.query_id, x.results[0].id)
            daftar_join.remove(chat_id)
            await infomsg.delete()
            await m.delete()
        except Exception as error:
            await m.reply(error)
            daftar_join.remove(chat_id)


@ky.ubot("end", sudo=True)
async def _(c, m):
    if len(m.command) < 2:
        chat_id = m.chat.id
    else:
        chat_id = int(m.text.split()[1])
    try:
        queues.clear(chat_id)
    except QueueEmpty:
        pass
    try:
        await c.call_py.leave_group_call(chat_id)
        await m.reply_text(
            "❏ <b>Berhasil Meninggalkan Voice Chat Grup.</b>", quote=False
        )
        await m.delete()
    except (NotInGroupCallError, NoActiveGroupCall):
        pass


@ky.ubot("skip", sudo=True)
async def _(c, m):
    if len(m.command) < 2:
        chat_id = m.chat.id
    else:
        chat_id = int(m.text.split()[1])
    queues.task_done(chat_id)
    await c.call_py.change_stream(chat_id, queues.get(chat_id)["file"])
    await m.reply_text("❏ <b>Memutar lagu berikutnya...</b>", quote=False)
    await m.delete()


@ky.ubot("pause", sudo=True)
async def _(c, m):
    if len(m.command) < 2:
        chat_id = m.chat.id
    else:
        chat_id = int(m.text.split()[1])
    await c.call_py.pause_stream(chat_id)
    await m.reply_text(
        "❏ <b>Lagu dijeda.</b>\n\n• Untuk melanjutkan pemutaran, gunakan <b>perintah</b> » resume.",
        quote=False,
    )
    await m.delete()


@ky.ubot("resume", sudo=True)
async def _(c, m):
    if len(m.command) < 2:
        chat_id = m.chat.id
    else:
        chat_id = int(m.text.split()[1])
    await c.call_py.resume_stream(chat_id)
    await m.reply_text(
        "❏ <b>Melanjutkan pemutaran lagu yang dijeda.</b>\n\n• Untuk menjeda pemutaran, gunakan <b>perintah</b> » pause.",
        quote=False,
    )
    await m.delete()


@ky.inline("^_yts")
async def _(c, q):
    m = [obj for obj in get_objects() if id(obj) == int(q.query.split(None, 1)[1])][0]
    query = (m.text or m.caption).split(None, 1)[1]
    results = YouTubeSearch(query, max_results=10).to_dict()
    videoid = results[0]["id"]
    title = results[0]["title"]
    duration = results[0]["duration"]
    thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="📀 Music",
                    callback_data=f"_p 0|{videoid}|{q.query.split(None, 1)[1]}",
                ),
                InlineKeyboardButton(
                    text="Video 📽️",
                    callback_data=f"_v 0|{videoid}|{q.query.split(None, 1)[1]}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="≪",
                    callback_data=f"_c B|0|{q.query.split(None, 1)[1]}",
                ),
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data=f"1_cls {m.from_user.id}",
                ),
                InlineKeyboardButton(
                    text="≫",
                    callback_data=f"_c F|0|{q.query.split(None, 1)[1]}",
                ),
            ],
        ]
    )
    msg = f"""
❏ <b>Judul: <a href='https://youtu.be/{videoid}'>{title}</a></b>
 <b>├ Durasi:</b> {duration}
 <b>╰  <a href='https://t.me/{bot.me.username}?start=InfoLagu_{videoid}'>More information</a></b>"""
    await q.answer(
        [
            InlineQueryResultPhoto(
                photo_url=thumb,
                title="search",
                caption=msg,
                reply_markup=buttons,
            )
        ]
    )


@ky.inline("^_x")
async def _(c, q):
    m = [obj for obj in get_objects() if id(obj) == int(q.query.split(None, 1)[1])][0]
    query = (m.text or m.caption).split(None, 2)[2]
    results = YouTubeSearch(query, max_results=10).to_dict()
    videoid = results[0]["id"]
    title = results[0]["title"]
    duration = results[0]["duration"]
    thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="📀 Music",
                    callback_data=f"_xp 0|{videoid}|{q.query.split(None, 1)[1]}",
                ),
                InlineKeyboardButton(
                    text="Video 📽️",
                    callback_data=f"_mxv 0|{videoid}|{q.query.split(None, 1)[1]}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data=f"1_cls {m.from_user.id}",
                ),
            ],
        ]
    )
    msg = f"""
❏ <b>Judul: <a href='https://youtu.be/{videoid}'>{title}</a></b>
 <b>├ Durasi:</b> {duration}
 <b>╰ <a href='https://t.me/{bot.me.username}?start=InfoLagu_{videoid}'>More information</a></b>"""
    await q.answer(
        [
            InlineQueryResultPhoto(
                photo_url=thumb,
                title="search",
                caption=msg,
                reply_markup=buttons,
            )
        ]
    )


@ky.callback("^_c")
async def _(_, cq):
    try:
        await cq.answer()
    except QueryIdInvalid:
        pass
    what, type, idm = cq.data.strip().split(None, 1)[1].split("|")
    m = [obj for obj in get_objects() if id(obj) == int(idm)][0]
    if not cq.from_user or cq.from_user.id != int(m.from_user.id):
        return
    what = str(what)
    type = int(type)
    if what == "F":
        if type == 9:
            query_type = 0
        else:
            query_type = int(type + 1)
        query = (m.text or m.caption).split(None, 1)[1]
        results = YouTubeSearch(query, max_results=10).to_dict()
        videoid = results[query_type]["id"]
        title = results[query_type]["title"]
        duration = results[query_type]["duration"]
        thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="📀 Music",
                        callback_data=f"_p {query_type}|{videoid}|{idm}",
                    ),
                    InlineKeyboardButton(
                        text="Video 📽️",
                        callback_data=f"_v {query_type}|{videoid}|{idm}",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="≪",
                        callback_data=f"_c B|{query_type}|{idm}",
                    ),
                    InlineKeyboardButton(
                        text="Tutup",
                        callback_data=f"1_cls {m.from_user.id}",
                    ),
                    InlineKeyboardButton(
                        text="≫",
                        callback_data=f"_c F|{query_type}|{idm}",
                    ),
                ],
            ]
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"""
❏ <b>Judul: <a href='https://youtu.be/{videoid}'>{title}</a></b>
 <b>├ Durasi:</b> {duration}
 <b>╰ <a href='https://t.me/{bot.me.username}?start=InfoLagu_{videoid}'>More information</a></b>""",
        )
        return await cq.edit_message_media(
            media=med,
            reply_markup=buttons,
        )
    if what == "B":
        if type == 0:
            query_type = 9
        else:
            query_type = int(type - 1)
        query = (m.text or m.caption).split(None, 1)[1]
        results = YouTubeSearch(query, max_results=10).to_dict()
        videoid = results[query_type]["id"]
        title = results[query_type]["title"]
        duration = results[query_type]["duration"]
        thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="📀 Music",
                        callback_data=f"_p {query_type}|{videoid}|{idm}",
                    ),
                    InlineKeyboardButton(
                        text="Video 📽️",
                        callback_data=f"_v {query_type}|{videoid}|{idm}",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="≪",
                        callback_data=f"_c B|{query_type}|{idm}",
                    ),
                    InlineKeyboardButton(
                        text="Tutup",
                        callback_data=f"1_cls {m.from_user.id}",
                    ),
                    InlineKeyboardButton(
                        text="≫",
                        callback_data=f"_c F|{query_type}|{idm}",
                    ),
                ],
            ]
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"""
❏ <b>Judul: <a href='https://youtu.be/{videoid}'>{title}</a></b>
 <b>├ Durasi:</b> {duration}
 <b>╰ <a href='https://t.me/{bot.me.username}?start=InfoLagu_{videoid}'>More information</a></b>""",
        )
        return await cq.edit_message_media(
            media=med,
            reply_markup=buttons,
        )


@ky.callback("^_p")
async def _(_, cq):
    try:
        await cq.answer()
    except QueryIdInvalid:
        pass
    what, type, idm = cq.data.strip().split(None, 1)[1].split("|")
    m = [obj for obj in get_objects() if id(obj) == int(idm)][0]
    if cq.from_user.id != m.from_user.id:
        return
    await cq.edit_message_text(f"<b>❏ Processing...</b>")
    url = f"https://youtu.be/{type}"
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    yt = await run_sync(ydl.extract_info, url, download=True)
    title = yt["title"]
    duration = yt["duration_string"]
    file_path = ydl.prepare_filename(yt)
    thumb = f"https://img.youtube.com/vi/{yt['id']}/hqdefault.jpg"
    pl_btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• Tutup •",
                    callback_data=f"1_cls {m.from_user.id}",
                ),
            ],
        ]
    )
    capt1 = f"""
<b>❏ Nama:</b> <a href={url}>{title}</a>
<b>├ Durasi:</b> <code>{duration}</code>
<b>├ <a href=https://t.me/{bot.me.username}?start=InfoLagu_{yt["id"]}>Information</a></b>
<b>╰ Atas Permintaan:</b> <a href=tg://openmessage?user_id={cq.from_user.id}>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>
"""
    if m.chat.id in m._client.call_py.calls:
        position = await queues.put(
            m.chat.id, file=AudioPiped(file_path, HighQualityAudio())
        )
        capt2 = (
            f"<b>📝 Music Ditambahkan Ke Antrian</b> » <code>{position}</code>\n"
            + capt1
        )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption=capt2), reply_markup=pl_btn
        )
    else:
        try:
            await m._client.call_py.join_group_call(
                m.chat.id,
                AudioPiped(file_path, HighQualityAudio()),
            )
        except Exception as e:
            if "Already joined into group call" not in str(e):
                if "No active group call" in str(e):
                    try:
                        await m._client.invoke(
                            CreateGroupCall(
                                peer=await m._client.resolve_peer(m.chat.id),
                                random_id=randint(0, 2147483647),
                            )
                        )
                    except Exception:
                        await m._client.send_message(
                            m.chat.id,
                            "❏ Maaf, <b>tidak</b> ada obrolan video yang aktif!\n\n• untuk menggunakan saya, <b>mulai obrolan video</b>.",
                        )
                        unPacked = unpackInlineMessage(cq.inline_message_id)
                        return await m._client.delete_messages(
                            unPacked.chat_id, unPacked.message_id
                        )
                    await m._client.call_py.join_group_call(
                        m.chat.id,
                        AudioPiped(file_path, HighQualityAudio()),
                    )
                else:
                    await m._client.send_message(
                        m.chat.id,
                        str(e),
                    )
                    unPacked = unpackInlineMessage(cq.inline_message_id)
                    return await m._client.delete_messages(
                        unPacked.chat_id, unPacked.message_id
                    )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption="<b>❏ Sedang Memutar Music</b>\n" + capt1),
            reply_markup=pl_btn,
        )


@ky.callback("^_v")
async def _(_, cq):
    try:
        await cq.answer()
    except QueryIdInvalid:
        pass
    what, type, idm = cq.data.strip().split(None, 1)[1].split("|")
    m = [obj for obj in get_objects() if id(obj) == int(idm)][0]
    if not cq.from_user or cq.from_user.id != m.from_user.id:
        return
    await cq.edit_message_text(f"<b>❏ Processing...</b>")
    url = f"https://youtu.be/{type}"
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    yt = await run_sync(ydl.extract_info, url, download=True)
    title = yt["title"]
    duration = yt["duration_string"]
    file_path = ydl.prepare_filename(yt)
    thumb = f"https://img.youtube.com/vi/{yt['id']}/hqdefault.jpg"
    pl_btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• Tutup •",
                    callback_data=f"1_cls {m.from_user.id}",
                ),
            ],
        ]
    )
    capt1 = f"""
<b>❏ Nama:</b> <a href={url}>{title}</a>
<b>├ Durasi:</b> <code>{duration}</code>
<b>╰ <a href=https://t.me/{bot.me.username}?start=InfoLagu_{yt["id"]}>Information</a></b>
<b>╰ Atas Permintaan:</b> <a href=tg://openmessage?user_id={cq.from_user.id}>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>
"""
    if m.chat.id in m._client.call_py.calls:
        position = await queues.put(
            m.chat.id,
            file=AudioVideoPiped(file_path, HighQualityAudio(), HighQualityVideo()),
        )
        capt2 = (
            f"<b>❏ Video Ditambahkan Ke Antrian</b> » <code>{position}</code>\n" + capt1
        )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption=capt2), reply_markup=pl_btn
        )
    else:
        try:
            await m._client.call_py.join_group_call(
                m.chat.id,
                AudioVideoPiped(file_path, HighQualityAudio(), HighQualityVideo()),
            )
        except Exception as e:
            if "Already joined into group call" not in str(e):
                if "No active group call" in str(e):
                    try:
                        await m._client.invoke(
                            CreateGroupCall(
                                peer=await m._client.resolve_peer(m.chat.id),
                                random_id=randint(0, 2147483647),
                            )
                        )
                    except Exception:
                        await m._client.send_message(
                            m.chat.id,
                            "❏ Maaf, <b>tidak</b> ada obrolan video yang aktif!\n\n• untuk menggunakan saya, <b>mulai obrolan video</b>.",
                        )
                        unPacked = unpackInlineMessage(cq.inline_message_id)
                        return await m._client.delete_messages(
                            unPacked.chat_id, unPacked.message_id
                        )
                    await m._client.call_py.join_group_call(
                        m.chat.id,
                        AudioVideoPiped(
                            file_path, HighQualityAudio(), HighQualityVideo()
                        ),
                    )
                else:
                    await m._client.send_message(
                        m.chat.id,
                        str(e),
                    )
                    unPacked = unpackInlineMessage(cq.inline_message_id)
                    return await m._client.delete_messages(
                        unPacked.chat_id, unPacked.message_id
                    )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption="<b>❏ Sedang Memutar Video</b>\n" + capt1),
            reply_markup=pl_btn,
        )


@ky.callback("^_xp")
async def _(_, cq):
    try:
        await cq.answer()
    except QueryIdInvalid:
        pass
    what, type, idm = cq.data.strip().split(None, 1)[1].split("|")
    m = [obj for obj in get_objects() if id(obj) == int(idm)][0]
    chat_id = int((m.text or m.caption).split(None, 2)[1])
    if not cq.from_user or cq.from_user.id != m.from_user.id:
        return
    await cq.edit_message_text(f"<b>❏ Processing...</b>")
    url = f"https://youtu.be/{type}"
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    yt = await run_sync(ydl.extract_info, url, download=True)
    title = yt["title"]
    duration = yt["duration_string"]
    file_path = ydl.prepare_filename(yt)
    thumb = f"https://img.youtube.com/vi/{yt['id']}/hqdefault.jpg"
    pl_btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data=f"1_cls {m.from_user.id}",
                ),
            ],
        ]
    )
    capt1 = f"""
<b>❏ Nama:</b> <a href={url}>{title}</a>
<b>├ Durasi:</b> <code>{duration}</code>
<b>├ <a href=https://t.me/{bot.me.username}?start=InfoLagu_{yt["id"]}>Information</a></b>
<b>╰ Atas Permintaan:</b> <a href=tg://openmessage?user_id={cq.from_user.id}>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>
"""
    if chat_id in m._client.call_py.calls:
        position = await queues.put(
            chat_id, file=AudioPiped(file_path, HighQualityAudio())
        )
        capt2 = (
            f"<b>📝 Music Ditambahkan Ke Antrian</b> » <code>{position}</code>\n"
            + capt1
        )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption=capt2), reply_markup=pl_btn
        )
    else:
        try:
            await m._client.call_py.join_group_call(
                chat_id,
                AudioPiped(file_path, HighQualityAudio()),
            )
        except Exception as e:
            if "Already joined into group call" not in str(e):
                if "No active group call" in str(e):
                    try:
                        await m._client.invoke(
                            CreateGroupCall(
                                peer=await m._client.resolve_peer(chat_id),
                                random_id=randint(0, 2147483647),
                            )
                        )
                    except Exception:
                        await m._client.send_message(
                            m.chat.id,
                            "❏ Maaf, <b>tidak</b> ada obrolan video yang aktif!\n\n• untuk menggunakan saya, <b>mulai obrolan video</b>.",
                        )
                        unPacked = unpackInlineMessage(cq.inline_message_id)
                        return await m._client.delete_messages(
                            unPacked.chat_id, unPacked.message_id
                        )
                    await m._client.call_py.join_group_call(
                        m.chat.id,
                        AudioPiped(file_path, HighQualityAudio()),
                    )
                else:
                    await m._client.send_message(
                        m.chat.id,
                        str(e),
                    )
                    unPacked = unpackInlineMessage(cq.inline_message_id)
                    return await m._client.delete_messages(
                        unPacked.chat_id, unPacked.message_id
                    )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption="<b>❏ Sedang Memutar Music</b>\n" + capt1),
            reply_markup=pl_btn,
        )


@ky.callback("^_mxv")
async def _(_, cq):
    try:
        await cq.answer()
    except QueryIdInvalid:
        pass
    what, type, idm = cq.data.strip().split(None, 1)[1].split("|")
    m = [obj for obj in get_objects() if id(obj) == int(idm)][0]
    chat_id = int((m.text or m.caption).split(None, 2)[1])
    if not cq.from_user or cq.from_user.id != m.from_user.id:
        return
    await cq.edit_message_text(f"<b>❏ Processing...</b>")
    url = f"https://youtu.be/{type}"
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    yt = await run_sync(ydl.extract_info, url, download=True)
    title = yt["title"]
    duration = yt["duration_string"]
    file_path = ydl.prepare_filename(yt)
    thumb = f"https://img.youtube.com/vi/{yt['id']}/hqdefault.jpg"
    pl_btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data=f"1_cls {m.from_user.id}",
                ),
            ],
        ]
    )
    capt1 = f"""
<b>❏ Nama:</b> <a href={url}>{title}</a>
<b>├ Durasi:</b> <code>{duration}</code>
<b>├ <a href=https://t.me/{bot.me.username}?start=InfoLagu_{yt["id"]}>Information</a></b>
<b>╰ Atas Permintaan:</b> <a href=tg://openmessage?user_id={cq.from_user.id}>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>
"""
    if chat_id in m._client.call_py.calls:
        position = await queues.put(
            chat_id,
            file=AudioVideoPiped(file_path, HighQualityAudio(), HighQualityVideo()),
        )
        capt2 = (
            f"<b>❏ Video Ditambahkan Ke Antrian</b> » <code>{position}</code>\n" + capt1
        )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption=capt2), reply_markup=pl_btn
        )
    else:
        try:
            await m._client.call_py.join_group_call(
                chat_id,
                AudioVideoPiped(file_path, HighQualityAudio(), HighQualityVideo()),
            )
        except Exception as e:
            if "Already joined into group call" not in str(e):
                if "No active group call" in str(e):
                    try:
                        await m._client.invoke(
                            CreateGroupCall(
                                peer=await m._client.resolve_peer(chat_id),
                                random_id=randint(0, 2147483647),
                            )
                        )
                    except Exception:
                        await m._client.send_message(
                            m.chat.id,
                            "❏ Maaf, <b>tidak</b> ada obrolan video yang aktif!\n\n• untuk menggunakan saya, <b>mulai obrolan video</b>.",
                        )
                        unPacked = unpackInlineMessage(cq.inline_message_id)
                        return await m._client.delete_messages(
                            unPacked.chat_id, unPacked.message_id
                        )
                    await m._client.call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(
                            file_path, HighQualityAudio(), HighQualityVideo()
                        ),
                    )
                else:
                    await m._client.send_message(
                        m.chat.id,
                        str(e),
                    )
                    unPacked = unpackInlineMessage(cq.inline_message_id)
                    return await m._client.delete_messages(
                        unPacked.chat_id, unPacked.message_id
                    )
        await cq.edit_message_media(
            InputMediaPhoto(thumb, caption="<b>❏ Sedang Memutar Video</b>\n" + capt1),
            reply_markup=pl_btn,
        )


@ky.callback("^1_cls")
async def _(_, cq):
    if not cq.from_user or cq.from_user.id != int(cq.data.split()[1]):
        return await cq.answer(
            f"Jangan Di Pencet Anjeng.",
            True,
        )
    unPacked = unpackInlineMessage(cq.inline_message_id)
    if cq.from_user.id == int(cq.data.split()[1]):
        await user.delete_messages(unPacked.chat_id, unPacked.message_id)

@ky.callback("closeru")
async def _(_, cq):
    unPacked = unpackInlineMessage(cq.inline_message_id)
    if cq.from_user.id == int(cq.data.split()[1]):
        await user.delete_messages(unPacked.chat_id, unPacked.message_id)
