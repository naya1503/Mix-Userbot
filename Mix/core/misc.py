#
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import socket
from os import execvp
from sys import executable
from sys import version as pyver

import heroku3
import wget
from aiohttp import ClientSession
from pyrogram import *
from pyrogram import __version__ as pyrover
from pyrogram.errors import *
from pyrogram.types import ChatPrivileges
from pytgcalls import __version__ as pytgver
from team.nandev.class_handler import TAG_LOG
from team.nandev.class_log import LOGGER
from team.nandev.database import ndB

from config import *

HAPP = None

aiohttpsession = ClientSession()


def on_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(heroku_api),
    "https",
    str(heroku_app_name),
    "HEAD",
    "dev",
]


def heroku():
    global HAPP
    if on_heroku:
        if heroku_api and heroku_app_name:
            try:
                Heroku = heroku3.from_key(heroku_api)
                HAPP = Heroku.app(heroku_app_name)
                LOGGER.info(f"Heroku App Configured")
            except BaseException:
                LOGGER.warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )


async def check_logger():
    LOGGER.info(f"Check Grup Log User...")
    if TAG_LOG is not None:
        return
    LOGGER.info(f"Creating Grup Log...")
    nama = f"Mix-Userbot Logs"
    des = "Jangan Keluar Dari Grup Log Ini\n\nPowered by: @KynanSupport"
    log_pic = "https://telegra.ph//file/ee7fc86ab183a0ff90392.jpg"
    gc = await nlx.create_supergroup(nama, des)
    bhan = wget.download(f"{log_pic}")
    gmbr = {"video": bhan} if bhan.endswith(".mp4") else {"photo": bhan}
    kntl = gc.id
    await nlx.set_chat_photo(kntl, **gmbr)
    await nlx.promote_chat_member(
        kntl,
        bot.me.username,
        privileges=ChatPrivileges(
            can_change_info=True,
            can_invite_users=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_chat=True,
            can_manage_video_chats=True,
        ),
    )
    ndB.set_key("TAG_LOG", kntl)
    await nlx.send_message(kntl, f"<b>Group Log Berhasil Dibuat.</b>")
    LOGGER.info(f"Group Logger Enable...")
    execvp(executable, [executable, "-m", "Mix"])


async def getFinish():
    emut = await nlx.get_prefix(nlx.me.id)
    xx = " ".join(emut)
    try:
        await bot.send_message(
            TAG_LOG,
            f"""
<b>Userbot Successfully Deploy !!</b>

<b>Modules : {len(CMD_HELP)}</b>
<b>Python : {pyver.split()[0]}</b>
<b>Pyrogram : {pyrover}</b>
<b>Pytgcalls : {pytgver}</b>
<b>Prefixes : {xx}</b>
""",
        )
    except (ChannelInvalid, PeerIdInvalid):
        ndB.del_key("TAG_LOG")
        execvp(executable, [executable, "-m", "Mix"])
