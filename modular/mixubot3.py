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

__modles__ = "MixUbot3"
__help__ = "MixUbot3"


@ky.ubot("mix", sudo=True)
async def _(c: user, m):
    uputt = await m.edit("**Hai... Perkenalkan Saya Adalah Mix-Userbot**")
    sleep(3)
    await uputt.edit("**Userbot base on Pyrogram**")
    sleep(2)
    await uputt.edit("**Part Of @KynanSupport... Salam Kenal yaaa ><**")
    sleep(3)
    await uputt.edit(
        "**Repository [Mix-Userbot](https://github.com/naya1503/Mix-Userbot)**"
    )


# Create by myself @AyiinXd


@ky.ubot("sayang", sudo=True)
async def _(c: user, m):
    xx = await m.edit("**Aku Cuma Mau Bilang...**")
    sleep(3)
    await xx.edit("**Aku Sayang Kamu Mwaahh** 😘❤")


# Create by myself @AyiinXd


@ky.ubot("semangat", sudo=True)
async def _(c: user, m):
    uputt = await m.edit("**Apapun Yang Terjadi...**")
    await asyncio.sleep(0.2)
    await uputt.edit("**Tetaplah Bernafas...**")
    await asyncio.sleep(0.2)
    await uputt.edit("**Dan Bersyukur...**")


# Create by myself @AyiinXd


@ky.ubot("mengeluh", sudo=True)
async def _(c: user, m):
    uputt = await m.edit("**Apapun Yang Terjadi...**")
    await asyncio.sleep(0.2)
    await uputt.edit("**Tetaplah Mengeluh...**")
    await asyncio.sleep(0.2)
    await uputt.edit("**Dan Putus Asa...**")


# Create by myself @AyiinXd
