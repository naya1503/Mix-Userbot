# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

import asyncio

from pyrogram import *

from Mix import *


@ky.ubot("cacad", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**Cacad 😏**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**Najis Akunnya Cacad 😂**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Hahahaha Cacad 🤣**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Canda Akun Cacad 😂🤣**")


@ky.ubot("hayo", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**Hayolo 😂**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**Hayoloo 😭**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Hayolooo 😆**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Hayoloooo 😭🕺**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Hayolooooo 👻**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Haayolooooo 🤭**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Botnya Mati Ya?**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Botnya Mati Ya? kasiaaaan** 😭🤌")
