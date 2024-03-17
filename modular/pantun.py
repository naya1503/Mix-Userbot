################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || @iamuputt
"""
################################################################


import asyncio

from pyrogram import *

from Mix import *

__modles__ = "Pantun"
__help__ = get_cgr("help_cakep")


@ky.ubot("sepat", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Ikan sepat ikan tongkol**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Mukaa lu kek kontolll.**😆")


@ky.ubot("ngangkang", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Beli batik di tanah abang..**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**Kamu cantikkk, Tapi sayang...**")
    await asyncio.sleep(2)
    await putt.edit("**Hobby nya ngangkang** 😆🤪")


@ky.ubot("hancur", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Makan semur, Masih anget..**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Muka kamu hancur, Kok pakai banget.🤪**")


@ky.ubot("kenalan", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Barang antik, ditarik andong**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Haii cantikk, kenalan donggg. 😋**")


@ky.ubot("soms", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Makan sambel ulek pakai kedondong**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Gapapa jelekk yang penting sombong. 😋**")


@ky.ubot("sirik", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Rambut panjang di sisirin**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**Sambil seduh dua extra joss**")
    await asyncio.sleep(2)
    await putt.edit("**Cerita dikit di nyinyirin**")
    await asyncio.sleep(2)
    await putt.edit("**Kalo sirikk bilang bosss..**🖕")


@ky.ubot("imut", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply("**Wajahmu memang imut**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(2)
    await putt.edit("**Bodimu kaya siput**")
    await asyncio.sleep(2)
    await putt.edit("**Tingkahmu membuatku salutt**")
    await asyncio.sleep(2)
    await putt.edit("**Tapi sayang hobimu kentutt.** 😭🤌")
