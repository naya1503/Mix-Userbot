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


@ky.ubot("ganteng", sudo=True)
async def _(c: nlx, m):
    uputt = await m.reply(
        "`Lu Mau Tau Sebuah Fakta?`", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.2)
    await uputt.edit("`Fakta Yang Belum Terbongkar Selama Ini`")
    await asyncio.sleep(1.2)
    await uputt.edit("**GUA GANTENG FIX NO DEBAT😏**")


@ky.ubot("wibu", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("`Kata Emak`", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(2)
    await uputt.edit("`Kalo Ketemu Wibuu`")
    await asyncio.sleep(2)
    await uputt.edit("`Harus Lari Sekenceng Mungkin🏃🏻`")
    await asyncio.sleep(3)
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`ㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await uputt.edit("`🧎🏻‍♂️ huhh... akhirnya bisa lolos dari wibu mematikan`")


# create by ayiin


@ky.ubot("ssenggol", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply(
        "`Bapaknya Udin Di Makan Singkong`", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("`Cuma Sendiri ni Senggol Dong`")
