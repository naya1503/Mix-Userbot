################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio
import os
import time
from datetime import timedelta
from time import time

import wget
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.file_id import *
from pyrogram.raw.functions.messages import *
from pyrogram.types import *
from youtubesearchpython import VideosSearch

from Mix import Emojik, YoutubeDownload, cgr, get_cgr, ky, nlx, progress

__modles__ = "Download"
__help__ = get_cgr("help_download")


@ky.ubot("dtik", sudo=False)
async def _(self: nlx, m):
    em = Emojik()
    em.initialize()
    hm = "luciferbukanrobot_bot"
    await nlx.unblock_user(hm)
    await nlx.send_message(hm, f"/tiktok {m.command[1]}", disable_web_page_preview=True)
    pros = await m.reply(cgr("proses").format(em.proses))
    ai = await nlx.forward_messages(hm, m.chat.id, message_ids=m.id)
    await nlx.send_message(hm, "/tiktok", reply_to_message_id=ai.id)
    await asyncio.sleep(5)
    async for tai in nlx.search_messages(hm, limit=1):
        await asyncio.sleep(5)
        if tai.media:
            await tai.copy(m.chat.id)
    await pros.delete()
    ulat = await nlx.resolve_peer(hm)
    await nlx.invoke(DeleteHistory(peer=ulat, max_id=0, revoke=True))
    return


@ky.ubot("vtube", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    if len(m.command) < 2:
        return await m.reply(cgr("down_1").format(em.gagal, m.command))
    pros = await m.reply(cgr("proses").format(em.proses))
    try:
        search = VideosSearch(m.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await pros.reply_text(cgr("err").format(em.gagal, error))
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=True)
    except Exception as error:
        return await pros.reply_text(cgr("err").format(em.gagal, error))
    thumbnail = wget.download(thumb)
    await c.send_video(
        m.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format(
            "VIDEO",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            c.me.mention,
        ),
        progress=progress,
        progress_args=(
            pros,
            time(),
            cgr("proses").format(em.proses),
            f"{search['id']}.mp4",
        ),
        reply_to_message_id=m.id,
    )
    await pros.delete()
    await m.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)


@ky.ubot("stube", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    if len(m.command) < 2:
        return await m.reply(cgr("down_1").format(em.gagal, m.command))
    pros = await m.reply(cgr("proses").format(em.proses))
    try:
        search = VideosSearch(m.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await pros.edit(cgr("err").format(em.gagal, error))
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=False)
    except Exception as error:
        return await pros.edit(cgr("err").format(em.gagal, error))
    thumbnail = wget.download(thumb)
    await c.send_audio(
        m.chat.id,
        audio=file_name,
        thumb=thumbnail,
        file_name=title,
        performer=channel,
        duration=duration,
        caption=data_ytp.format(
            "AUDIO",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            c.me.mention,
        ),
        progress=progress,
        progress_args=(
            pros,
            time(),
            cgr("proses").format(em.proses),
            f"{search['id']}.mp3",
        ),
        reply_to_message_id=m.id,
    )
    await pros.delete()
    await m.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
