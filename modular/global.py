################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

__modles__ = "Global"
__help__ = """
 Help Command Global

• Perintah : <code>{0}gban</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melakukan global banned.

• Perintah : <code>{0}ungban</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melakukan global ubanned.

• Perintah : <code>{0}listgban</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melihat daftar pengguna gban.

• Perintah : <code>{0}gmute</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melakukan global mute.

• Perintah : <code>{0}ungmute</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melakukan global unmute.

• Perintah : <code>{0}listgmute</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melihat daftar pengguna gmute.
"""


import asyncio
from io import BytesIO

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *
from Mix.core.parser import remove_markdown_and_html
from Mix.core.sender_tools import extract_user

dbgb = GBan()
dbgm = GMute()


@ky.ubot("gban", sudo=True)
@ky.devs("cgban")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, userid, _ = await extract_user(c, m)
    xx = await m.reply(f"{em.proses} Processing...")
    try:
        org = await c.get_users(nyet)
    except PeerIdInvalid:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if not org:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if nyet in DEVS:
        await xx.edit(f"{em.gagal} Dia adalah Developer Mix-Userbot.")
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await xx.edit(f"{em.gagal} Silahkan berikan alasan untuk diGban!")
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
            await xx.edit(f"{em.gagal} Pengguna sudah digban.")
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
    mmg = f"{em.warn} <b>Warning Global Banned\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n{em.block} **Alasan: `{alasan}`**"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("ungban", sudo=True)
@ky.devs("cungban")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, userid, _ = await extract_user(c, m)
    xx = await m.reply(f"{em.proses} Processing...")
    org = await c.get_users(nyet)
    if not org:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
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
            await xx.edit(f"{em.gagal} Pengguna belum digban.")
            return
        try:
            await c.unban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgb.remove_gban(nyet)
    mmg = f"{em.warn} <b>Warning Global Unbanned\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("gmute", sudo=True)
@ky.devs("cgmute")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, userid, _ = await extract_user(c, m)
    xx = await m.reply(f"{em.proses} Processing...")
    org = await c.get_users(nyet)
    if not org:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if nyet in DEVS:
        await xx.edit(f"{em.gagal} Dia adalah Developer Mix-Userbot.")
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await xx.edit(f"{em.gagal} Silahkan berikan alasan untuk diGMute!")
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
            await xx.edit(f"{em.gagal} Pengguna sudah digmute.")
            return
        try:
            await c.restrict_chat_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.add_gmute(nyet, alasan, c.me.id)
    mmg = f"{em.warn} <b>Warning Global Gmute\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n{em.block} **Alasan: `{alasan}`**"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("ungmute", sudo=True)
@ky.devs("cungmute")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, userid, _ = await extract_user(c, m)
    xx = await m.reply(f"{em.proses} Processing...")
    org = await c.get_users(nyet)
    if not org:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if nyet in DEVS:
        await xx.edit(f"{em.gagal} Dia adalah Developer Mix-Userbot.")
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
            await xx.edit(f"{em.gagal} Pengguna belum pernah diGMute.")
            return
        try:
            await c.unban_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.remove_gmute(nyet)
    mmg = f"{em.warn} <b>Warning Global Ungmute\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("gbanlist|listgban", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gbanu = dbgb.load_from_db()
    msg = await m.reply(f"{em.proses} <b>Processing...</b>")
    dftr = f"{em.profil} **Daftar GBanned :**\n\n"
    if not gbanu:
        return await m.reply(f"{em.gagal} <b>Tidak ada pengguna ditemukan.</b>")
    for ii in gbanu:
        dftr += f"{em.block} <b>{ii['_id']}</b>\n"
        if ii["reason"]:
            dftr += f"{em.warn} <b>Alasan:</b> {ii['reason']}\n\n{em.sukses} **Total :`{dbgb.count_gbans()}`**\n"
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gbanlist.txt"
            await m.reply_document(
                document=f, caption=f"{em.profil} **Daftar GBanned!!**\n\n"
            )
    await msg.delete()
    return


@ky.ubot("gmutelist|listgmute", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gmnu = dbgm.load_from_db()
    msg = await m.reply(f"{em.proses} <b>Processing...</b>")
    dftr = f"{em.profil} **Daftar GMute :**\n\n"
    if not gmnu:
        await m.reply(f"{em.gagal} <b>Tidak ada pengguna ditemukan.</b>")
    for ii in gmnu:
        dftr += f"{em.warn} <b>{ii['_id']}</b>\n"
        if ii["reason"]:
            dftr += f"{em.warn} <b>Alasan:</b> {ii['reason']}\n\n{em.sukses} **Total :`{dbgm.count_gmutes()}`**\n"
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gmutelist.txt"
            await m.reply_document(
                document=f, caption=f"{em.profil} **Daftar GMute!!**\n\n"
            )
    await msg.delete()
    return