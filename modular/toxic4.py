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


@ky.ubot("sadboy", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("`Pertama-tama kamu cantik`")
    await asyncio.sleep(1.8)
    await uputt.edit("`Kedua kamu manis`")
    await asyncio.sleep(1.8)
    await uputt.edit("`Dan yang terakhir adalah kamu bukan milikku`")


# Create by myself @localheart


@ky.ubot("lah", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**Lah, Lu tolol?**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**Apa dongok?**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Gausah sok keras**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Gua ga ketrigger sama bocah baru nyemplung!**")


@ky.ubot("sok", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**WOII**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**KONTOL**")
    await asyncio.sleep(1.8)
    await uputt.edit("**KALO MENTAL MASIH PATUNGAN**")
    await asyncio.sleep(1.8)
    await uputt.edit("**GAUSAH SOK KERAS DEH**")
    await asyncio.sleep(1.8)
    await uputt.edit("**GA KEREN LO BEGITU NGENTOT**")


@ky.ubot("wah", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply(
        "**Wahh, War nya keren bang**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**Tapi, Yang gua liat, kok Kaya lawakan**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Oh iya, Kan lo badut 🤡**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Kosa kata pas ngelawak, Jangan di pake war bang**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Kesannya lo ngasih kita hiburan.**")
    await asyncio.sleep(1.8)
    await uputt.edit(
        "**Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk**"
    )
    await asyncio.sleep(1.8)
    await uputt.edit(
        "**Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak**"
    )


@ky.ubot("alay", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("eh kamu, iya kamu", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**ALAY bnget sih**")
    await asyncio.sleep(1.8)
    await uputt.edit("**spam bot mulu**")
    await asyncio.sleep(1.8)
    await uputt.edit("**baru pande bikin userbot ya?? xixixi**")
    await asyncio.sleep(1.8)
    await uputt.edit("**pantes NORAK**")


@ky.ubot("erpe", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("Hai, Kamu Anak Erpe Ya", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("Kok Pake Muka Orang sih?")
    await asyncio.sleep(1.8)
    await uputt.edit("Oh iya, Muka Anak Erpe Kan")
    await asyncio.sleep(1.8)
    await uputt.edit("**BURIK - BURIK**")
    await asyncio.sleep(1.8)
    await uputt.edit("Jadinya Pake Muka Orang")
    await asyncio.sleep(1.8)
    await uputt.edit("Karena Muka Anak erpe")
    await asyncio.sleep(1.8)
    await ayiin.edit("**BURIK - BURIK**")
    await asyncio.sleep(1.8)
    await uputt.edit("Canda **BURIK**")
    await asyncio.sleep(1.8)
    await uputt.edit("Lari Ada Plastik KePanasan")


@ky.ubot("tittle", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    uputt = await m.reply("**OI ANAK TITLE**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(1.8)
    await uputt.edit("**OOO INI YANG SOK JADI PAHLAWAN DI TELEGRAM?**")
    await asyncio.sleep(1.8)
    await uputt.edit("**TITLE KEMANA MANA SAMPE MENUHIN NAMA**")
    await asyncio.sleep(1.8)
    await uputt.edit("**ADA YANG SAMPE 18+ LAH SEGALA MACEM**")
    await asyncio.sleep(1.8)
    await uputt.edit("**LO KIRA KEREN KEK GITU?**")
    await asyncio.sleep(1.8)
    await uputt.edit("**KERJAAN CUMA NGURUSIN GRUP DI TELEGRAM SAMA NGAJAK ORANG WAR**")
    await asyncio.sleep(1.8)
    await uputt.edit("**YAELAH BRO MENTAL LO CUMA DI SOSMED APA GIMANE?**")
    await asyncio.sleep(1.8)
    await uputt.edit(
        "**PERASAAN DULU TELEGRAM GAADA DEH BOCAH BOCAH SOK JAGO KEK GINI**"
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**GILIRAN TITLE NYA DI EJEK NGADU KE OWNER NYA**")
    await asyncio.sleep(1.8)
    await uputt.edit("**TRUS NGAJAK WAR**")
    await asyncio.sleep(1.8)
    await uputt.edit("**BUSET DAH BANG**")
    await asyncio.sleep(1.8)
    await uputt.edit("**UDAH SEJAGO APESI SAMPE GC DIBELA BELA**")
    await asyncio.sleep(1.8)
    await uputt.edit("**ORANG TUA LO NOH ADA YANG NAGIH UTANG UDA LO BELA BELOM?**")
    await asyncio.sleep(1.8)
    await uputt.edit("**RELA NGUTANG DEMI NGIDUPIN LU**")
    await asyncio.sleep(1.8)
    await uputt.edit("**EH ANAKNYA MALAH NGEBELAIN GC GAJELAS HAHAHA**")
    await asyncio.sleep(1.8)
    await uputt.edit("**MANA VIRTUAL LAGI, SOK JAGO LAGI DUH**")
    await asyncio.sleep(1.8)
    await uputt.edit("**SEMOGA CEPET SADAR YA HAHAHAHA**")
