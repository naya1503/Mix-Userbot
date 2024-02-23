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
from team.nandev.new_database import GBan, GMute

from Mix import DEVS, Emojik, ky, user
from Mix.core.parser import remove_markdown_and_html

dbgb = GBan()
dbgm = GMute()


@ky.ubot("gban", sudo=True)
@ky.devs("cgban")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, alasan = await c.extract_user_and_reason(m)
    xx = await m.reply(f"{em.proses} Processing...")
    try:
        org = await c.get_users(nyet)
    except PeerIdInvalid:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if not org:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if org.id in DEVS:
        await xx.edit(f"{em.gagal} Dia adalah Developer Mix-Userbot.")
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await m.reply_text(f"{em.gagal} Silahkan berikan alasan untuk diGban!")
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
        if dbgb.check_gban(org.id):
            await xx.edit(f"{em.gagal} Pengguna sudah digban.")
            return
        try:
            await c.ban_chat_member(chat, org.id)
            bs += 1
            await asyncio.sleep(0.1)

        except FloodWait as e:
            await asyncio.sleep(int(e.value))
            await c.ban_chat_member(chat, org.id)
            bs += 1
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgb.add_gban(org.id, alasan, c.me.id)
    mmg = f"{em.warn} <b>Warning Global Banned\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n{em.block} **Alasan: `{alasan}`**"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("ungban", sudo=True)
@ky.devs("cungban")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet = await c.extract_user(m)
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
        if not dbgb.check_gban(org.id):
            await xx.edit(f"{em.gagal} Pengguna belum digban.")
            return
        try:
            await c.unban_chat_member(chat, org.id)
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgb.remove_gban(org.id)
    mmg = f"{em.warn} <b>Warning Global Unbanned\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("gmute", sudo=True)
@ky.devs("cgmute")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet, alasan = await c.extract_user_and_reason(m)
    xx = await m.reply(f"{em.proses} Processing...")
    org = await c.get_users(nyet)
    if not org:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if org.id in DEVS:
        await xx.edit(f"{em.gagal} Dia adalah Developer Mix-Userbot.")
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await m.reply_text(f"{em.gagal} Silahkan berikan alasan untuk diGMute!")
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
        if dbgm.check_gmute(org.id):
            await xx.edit(f"{em.gagal} Pengguna sudah digmute.")
            return
        try:
            await c.restrict_chat_member(chat, org.id, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.add_gmute(org.id, alasan, c.me.id)
    mmg = f"{em.warn} <b>Warning Global Gmute\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n{em.block} **Alasan: `{alasan}`**"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("ungmute", sudo=True)
@ky.devs("cungmute")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    nyet = await c.extract_user(m)
    xx = await m.reply(f"{em.proses} Processing...")
    org = await c.get_users(nyet)
    if not org:
        await xx.edit(f"{em.gagal} Pengguna tidak ditemukan.")
        return
    if org.id in DEVS:
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
        if not dbgm.check_gmute(org.id):
            await xx.edit(f"{em.gagal} Pengguna belum pernah diGMute.")
            return
        try:
            await c.unban_member(chat, org.id, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.remove_gmute(org.id)
    mmg = f"{em.warn} <b>Warning Global Ungmute\n\n{em.sukses} Berhasil: `{bs}` Chat\n{em.gagal} Gagal: `{gg}` Chat\n{em.profil} User: `{mention}`</b>\n"
    await m.reply(mmg)
    await xx.delete()


@ky.ubot("gbanlist|listgban", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gbanu = dbgb.load_from_db()
    msg = await m.reply(f"{em.proses} <b>Processing...</b>")
    dftr = f"{em.profil} **Daftar Pengguna :**\n\n"
    if not gbanu:
        return await msg.edit(f"{em.gagal} <b>Tidak ada pengguna ditemukan.</b>")
    for ii in gbanu:
        dftr += f"[x] <b>{Users.get_user_info(ii['_id'])['name']}</b> - <code>{ii['_id']}</code>\n"
        if ii["reason"]:
            dftr += f"<b>Alasan:</b> {ii['reason']}\n"
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gbanlist.txt"
            await m.reply_document(
                document=f, caption=f"{em.profil} **Daftar Pengguna GBan!!**\n\n"
            )


@ky.ubot("gmutelist|listgmute", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gmnu = dbgm.load_from_db()
    msg = await m.reply(f"{em.proses} <b>Processing...</b>")
    dftr = f"{em.profil} **Daftar Pengguna :**\n\n"
    if not gmnu:
        return await msg.edit(f"{em.gagal} <b>Tidak ada pengguna ditemukan.</b>")
    for ii in gmnu:
        dftr += f"[x] <b>{Users.get_user_info(ii['_id'])['name']}</b> - <code>{ii['_id']}</code>\n"
        if ii["reason"]:
            dftr += f"<b>Alasan:</b> {ii['reason']}\n"
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gmutelist.txt"
            await m.reply_document(
                document=f, caption=f"{em.profil} **Daftar Pengguna GMute!!**\n\n"
            )
