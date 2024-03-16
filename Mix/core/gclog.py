################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty
 
 MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
"""
################################################################


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
