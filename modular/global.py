################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import asyncio
from io import BytesIO

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *
from Mix.core.parser import remove_markdown_and_html

dbgb = GBan()
dbgm = GMute()

__modles__ = "Global"
__help__ = get_cgr("help_global")


@ky.ubot("gban", sudo=True)
@ky.devs("cgban")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    if nyet in DEVS:
        await xx.edit(cgr("glbl_3").format(em.gagal))
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await xx.edit(cgr("glbl_4").format(em.gagal))
        return
    if m.reply_to_message:
        alasan = m.text.split(None, 1)[1]
    else:
        alasan = m.text.split(None, 2)[2]
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("all")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if dbgb.check_gban(nyet):
            await xx.edit(cgr("glbl_5").format(em.gagal))
            return
        try:
            await c.ban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)

        except FloodWait as e:
            await asyncio.sleep(int(e.value))
            await c.ban_chat_member(chat, nyet)
            bs += 1
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgb.add_gban(nyet, alasan, c.me.id)
    mmg = cgr("glbl_6").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention, em.block, alasan
    )
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("ungban", sudo=True)
@ky.devs("cungban")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    await c.get_users(nyet)
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("all")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if not dbgb.check_gban(nyet):
            await xx.edit(cgr("glbl_7").format(em.gagal))
            return
        try:
            await c.unban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgb.remove_gban(nyet)
    mmg = cgr("glbl_8").format(em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention)
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("gmute", sudo=True)
@ky.devs("cgmute")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    if nyet in DEVS:
        await xx.edit(cgr("glbl_3").format(em.gagal))
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await xx.edit(cgr("glbl_9").format(em.gagal))
        return
    if m.reply_to_message:
        alasan = m.text.split(None, 1)[1]
    else:
        alasan = m.text.split(None, 2)[2]
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("group")

    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if dbgm.check_gmute(nyet):
            await xx.edit(cgr("glbl_10").format(em.gagal))
            return
        try:
            await c.restrict_chat_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.add_gmute(nyet, alasan, c.me.id)
    mmg = cgr("glbl_11").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention, em.block, alasan
    )
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("ungmute", sudo=True)
@ky.devs("cungmute")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    await c.get_users(nyet)
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("group")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if not dbgm.check_gmute(nyet):
            await xx.edit(cgr("glbl_12").format(em.gagal))
            return
        try:
            await c.unban_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.remove_gmute(nyet)
    mmg = cgr("glbl_13").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention
    )
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("gbanlist|listgban", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gbanu = dbgb.load_from_db()
    msg = await m.reply(cgr("proses").format(em.proses))

    if not gbanu:
        return await msg.edit(cgr("glbl_22").format(em.gagal))
    dftr = cgr("glbl_14").format(em.profil)
    for ii in gbanu:
        dftr += cgr("glbl_15").format(em.block, ii["_id"])
        if ii["reason"]:
            dftr += cgr("glbl_16").format(
                em.warn, ii["reason"], em.sukses, dbgb.count_gbans()
            )
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gbanlist.txt"
            await m.reply_document(document=f, caption=cgr("glbl_17").format(em.profil))
    await msg.delete()
    return


@ky.ubot("gmutelist|listgmute", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gmnu = dbgm.load_from_db()
    msg = await m.reply(cgr("proses").format(em.proses))
    if not gmnu:
        await msg.edit(cgr("glbl_2").format(em.gagal))
        return
    dftr = cgr("glbl_18").format(em.profil)
    for ii in gmnu:
        dftr += cgr("glbl_19").format(em.warn, ii["_id"])
        if ii["reason"]:
            dftr += cgr("glbl_20").format(
                em.warn, ii["reason"], em.sukses, dbgm.count_gmutes()
            )
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gmutelist.txt"
            await m.reply_document(document=f, caption=cgr("glbl_21").format(em.profil))
    await msg.delete()
    return
