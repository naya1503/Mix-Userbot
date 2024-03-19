"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
import sys
import time
import ffmpeg
import asyncio
import subprocess
from asyncio import sleep
from youtube_dl import YoutubeDL
from pytgcalls import GroupCallFactory
from youtubesearchpython import VideosSearch

import os
import subprocess
from asyncio import sleep
from os import path
from random import randint
from signal import SIGINT
from typing import Optional

import wget
from pyrogram import emoji
from pyrogram.errors import *
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, EditGroupCallTitle
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.utils import MAX_CHANNEL_ID
from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError
from yt_dlp import YoutubeDL

from Mix import *

CALL_STATUS = {}
FFMPEG_PROCESSES = {}
RADIO = {6}
msg = {}
playlist = []


ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "verbose": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


async def get_group_call(c: nlx, m, err_msg: str = "") -> Optional[InputGroupCall]:
    em = Emojik()
    em.initialize()
    chat_peer = await c.resolve_peer(m)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await c.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await c.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await m.reply_text(cgr("vc_1").format(em.gagal, err_msg))
    return False


group_call = GroupCallFactory(
    nlx, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
).get_file_group_call()

ydl_opts = {
        "quiet": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)


# pytgcalls handlers

@group_call.on_audio_playout_ended
async def _(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[INFO] - AUDIO_CALL ENDED !")

@group_call.on_video_playout_ended
async def _(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[INFO] - VIDEO_CALL ENDED !")
