# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.
import asyncio
import logging
import os
import threading

import ffmpeg
from pyrogram.errors import FloodWait, MessageNotModified
from yt_dlp import YoutubeDL

from .colong import *

stream_vc = {}
play_vc = {}


@run_in_exc
def convert_to_raw(audio_original, raw_file_name):
    ffmpeg.input(audio_original).output(
        raw_file_name,
        format="s16le",
        acodec="pcm_s16le",
        ac=2,
        ar="48k",
        loglevel="error",
    ).overwrite_output().run()
    return raw_file_name


def edit_msg(client, message, to_edit):
    try:
        client.loop.create_task(message.edit(to_edit))
    except MessageNotModified:
        pass
    except FloodWait as e:
        client.loop.create_task(asyncio.sleep(e.x))
    except TypeError:
        pass


def download_progress_hook(d, message, client, start):
    if d["status"] == "downloading":
        current = d.get("_downloaded_bytes_str") or humanbytes(
            d.get("downloaded_bytes", 1)
        )
        total = d.get("_total_bytes_str") or d.get("_total_bytes_estimate_str")
        file_name = d.get("filename")
        eta = d.get("_eta_str", "N/A")
        percent = d.get("_percent_str", "N/A")
        speed = d.get("_speed_str", "N/A")
        to_edit = f"<b><u>Downloading File</b></u> \n<b>File Name :</b> <code>{file_name}</code> \n<b>File Size :</b> <code>{total}</code> \n<b>Speed :</b> <code>{speed}</code> \n<b>ETA :</b> <code>{eta}</code> \n<i>Download {current} out of {total}</i> (__{percent}__)"
        threading.Thread(target=edit_msg, args=(client, message, to_edit)).start()


@run_in_exc
def yt_dl(url, client, message, start):
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "progress_hooks": [lambda d: download_progress_hook(d, message, client, start)],
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=True)
    return str(ytdl_data["id"]) + ".mp3"


RD_ = {}
FFMPEG_PROCESSES = {}


async def get_chat_(client, chat_):
    chat_ = str(chat_)
    if chat_.startswith("-100"):
        try:
            return (await client.get_chat(int(chat_))).id
        except ValueError:
            chat_ = chat_.split("-100")[1]
            chat_ = "-" + str(chat_)
            return int(chat_)


async def playout_ended_handler(group_call, filename):
    client_ = group_call.client
    chat_ = await get_chat_(client_, f"-100{group_call.full_chat.id}")
    chat_ = int(chat_)
    s = stream_vc.get((chat_, client_.me.id))
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    if not s:
        await group_call.stop()
        del play_vc[(chat_, client_.me.id)]
        return

    name_ = s[0]["song_name"]
    singer_ = s[0]["singer"]
    dur = s[0]["dur"]
    raw_file = s[0]["raw"]
    link = s[0]["url"]
    thumb_ = s[0]["thumb"]
    humanbytes(os.stat(raw_file).st_size)
    orgu = f"<a href='tg://user?id={client_.me.id}'>{client_.me.first_name} {client_.me.last_name or ''}</a>"
    bij = f'<a href="{link}">{name_}</a>'
    song_info = """
<u><b>🎼 Sekarang Diputar 🎶</b></u>

**🎵 Judul : {}**
**🎸 Artist : `{}`**
**⏲️️ Durasi : `{}`**
**📩 Permintaan : {}**
"""
    try:
        await client_.send_photo(
            chat_,
            photo=thumb_,
            caption=song_info.format(bij, singer_, dur, orgu),
        )
    except:
        await client_.send_message(
            chat_,
            song_info.format(bij, singer_, dur, orgu),
        )
    s.pop(0)
    logging.debug(song_info)
    group_call.song_name = name_
    group_call.input_filename = raw_file
