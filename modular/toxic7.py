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


@ky.ubot("ywc", sudo=True)
async def _(c: nlx, m):
    await m.reply("**Oke Sama-sama**", reply_to_message_id=ReplyCheck(m))


@ky.ubot("jamet", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**WOIII**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.5)
    await uputt.edit("**JAMETTT**")
    await asyncio.sleep(1.5)
    await uputt.edit("**CUMA MAU BILANG**")
    await asyncio.sleep(1.5)
    await uputt.edit("**GAUSAH SO ASIK**")
    await asyncio.sleep(1.5)
    await uputt.edit("**EMANG KENAL?**")
    await asyncio.sleep(1.5)
    await uputt.edit("**GAUSAH REPLY**")
    await asyncio.sleep(1.5)
    await uputt.edit("**KITA BUKAN KAWAN**")
    await asyncio.sleep(1.5)
    await uputt.edit("**GASUKA PC ANJING**")
    await asyncio.sleep(1.5)
    await uputt.edit("**BOCAH KAMPUNG**")
    await asyncio.sleep(1.5)
    await uputt.edit("**MENTAL TEMPE**")
    await asyncio.sleep(1.5)
    await uputt.edit("**LEMBEK NGENTOT🔥**")


@ky.ubot("pp", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("dp", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("so", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("met", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("war", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("wartai", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("kismin", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("ded", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("sokab", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("gembel", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("cuih", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("dih", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("skb", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    await m.reply(
        "**EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK**",
        reply_to_message_id=ReplyCheck(m),
    )


@ky.ubot("virtual", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply(
        "**OOOO... INI YANG VIRTUAL**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.5)
    await uputt.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await uputt.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await uputt.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await uputt.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await uputt.edit("**APALAGI OMONGANNYA**")
    await asyncio.sleep(1.5)
    await uputt.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await uputt.edit("**KASIAN MANA MASIH MUDA**")
