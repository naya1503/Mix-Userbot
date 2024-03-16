# Copyright (C) 2021 Kyy - Userbot
# Credit by kyy
# Recode by @AyiinXd


import asyncio

from pyrogram import *

from Mix import *


@ky.ubot("lipkol", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**Ayaaang** 🥺")
    await asyncio.sleep(1.8)
    await uputt.edit("**Kangeeen** 👉👈")
    await asyncio.sleep(1.8)
    await uputt.edit("**Pingiinn Slipkool Yaaang** 🥺👉👈")


# Create by myself @localheart


@ky.ubot("nakal", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**Ayaaang Ih** 🥺", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**Nakal Banget Dah Ayang** 🥺")
    await asyncio.sleep(1.8)
    await uputt.edit("**Aku Gak Like Ayang** 😠")
    await asyncio.sleep(1.8)
    await uputt.edit("**Pokoknya Aku Gak Like Ih** 😠")


@ky.ubot("favboy", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply(
        "**Duuhh Ada Cowo Ganteng** 👉👈", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**You Are My Favorit Boy** 😍")
    await asyncio.sleep(1.8)
    await uputt.edit("**Kamu Harus Jadi Cowo Aku Ya** 😖")
    await asyncio.sleep(1.8)
    await uputt.edit("**Pokoknya Harus Jadi Cowo Aku** 👉👈")
    await asyncio.sleep(1.8)
    await uputt.edit("**Gak Boleh Ada Yang Lain** 😠")


@ky.ubot("favgirl", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply(
        "**Duuhh Ada Cewe Cantik** 👉👈", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**You Are My Favorit Girl** 😍")
    await asyncio.sleep(1.8)
    await uputt.edit("**Kamu Harus Jadi Cewe Aku Ya** 😖")
    await asyncio.sleep(1.8)
    await uputt.edit("**Pokoknya Harus Jadi Cewe Aku** 👉👈")
    await asyncio.sleep(1.8)
    await uputt.edit("**Gak Boleh Ada Yang Lain** 😠")


@ky.ubot("canlay", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply(
        "**Eh Kamu Cantik-cantik**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**Kok Alay Banget**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Spam Bot Mulu**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Baru Bikin Userbot Ya??**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Pantes Norak Xixixi**")


@ky.ubot("ganlay", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply(
        "**Eh Kamu Ganteng-ganteng**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**Kok Alay Banget**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Spam Bot Mulu**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Baru Bikin Userbot Ya??**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Pantes Norak Xixixi**")


@ky.ubot("ange", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**Ayanggg 😖**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**Aku Ange 😫**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Ayuukk Picies Yang 🤤**")
