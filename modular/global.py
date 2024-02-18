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
from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from Mix import *


@ky.ubot("gban", sudo=True)
@ky.devs("cgban")
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    nyet, alasan = await c.extract_user_and_reason(m)
    xx = await m.reply(f"{emo.proses} Processing...")
    user = await c.get_users(nyet)
    if not user:
        await xx.edit(f"{emo.gg} Pengguna tidak ditemukan.")
        return
    if user.id in DEVS:
        await xx.edit(f"{emo.gagal} Dia adalah Developer Mix-Userbot.")
        return
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("all")
    gban_users = udB.get_list_from_var(c.me.id, "GBANNED", "USER")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = (
            m.reply_to_message.sender_chat.title
            if m.reply_to_message
            else "Anon")
    for chat in chats:
        if user.id in gban_users:
            await xx.edit(f"{emo.gagal} Pengguna sudah digban.")
            return
        try:
            udB.add_to_var(c.me.id, "GBANNED", user.id, "USER")
            GBAN_USER.add(user.id)
            await c.ban_chat_member(chat, user.id)
            bs += 1
            await asyncio.sleep(0.1)
        except Floodwait as e:
            await asyncio.sleep(int(e.value))
            await c.ban_chat_member(chat, user.id)
            bs += 1
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    mmg = f"{emo.alive} <b>Warning Global Banned\n\n{emo.sukses} Berhasil: `{bs}` Chat\n{emo.gagal} Gagal: `{gg}` Chat\n{emo.profil} User: `{mention}`</b>\n"
    if alasan:
        mmg += f"**Alasan: `{alasan}`**"
    await m.reply(mmg)
    await xx.delete()

@ky.ubot("ungban", sudo=True)
@ky.devs("cungban")
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    nyet = await c.extract_user(m)
    xx = await m.reply(f"{emo.proses} Processing...")
    user = await c.get_users(nyet)
    if not user:
        await xx.edit(f"{emo.gg} Pengguna tidak ditemukan.")
        return
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("all")
    gban_users = udB.get_list_from_var(c.me.id, "GBANNED", "USER")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = (
            m.reply_to_message.sender_chat.title
            if m.reply_to_message
            else "Anon")
    for chat in chats:
        if user.id not in gban_users:
            await xx.edit(f"{emo.gagal} Pengguna belum digban.")
            return
        try:
            udB.remove_from_var(c.me.id, "GBANNED", user.id, "USER")
            GBAN_USER.remove(user.id)
            await c.unban_chat_member(chat, user.id)
            bs += 1
            await asyncio.sleep(0.1)
        except Floodwait as e:
            await asyncio.sleep(int(e.value))
            await c.unban_chat_member(chat, user.id)
            bs += 1
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    mmg = f"{emo.alive} <b>Warning Global Unbanned\n\n{emo.sukses} Berhasil: `{bs}` Chat\n{emo.gagal} Gagal: `{gg}` Chat\n{emo.profil} User: `{mention}`</b>\n"
    await m.reply(mmg)
    await xx.delete()

@ky.ubot("gmute", sudo=True)
@ky.devs("cgmute")
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    nyet, alasan = await c.extract_user_and_reason(m)
    xx = await m.reply(f"{emo.proses} Processing...")
    user = await c.get_users(nyet)
    if not user:
        await xx.edit(f"{emo.gg} Pengguna tidak ditemukan.")
        return
    if user.id in DEVS:
        await xx.edit(f"{emo.gagal} Dia adalah Developer Mix-Userbot.")
        return
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("group")
    gmute_users = udB.get_list_from_var(c.me.id, "GMUTE", "USER")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = (
            m.reply_to_message.sender_chat.title
            if m.reply_to_message
            else "Anon")
    for chat in chats:
        if user.id in gmute_users:
            await xx.edit(f"{emo.gagal} Pengguna sudah digmute.")
            return
        try:
            udB.add_to_var(c.me.id, "GMUTE", user.id, "USER")
            GMUTE_USER.add(user.id)
            await c.restrict_chat_member(chat, user.id, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    mmg = f"{emo.alive} <b>Warning Global Gmute\n\n{emo.sukses} Berhasil: `{bs}` Chat\n{emo.gagal} Gagal: `{gg}` Chat\n{emo.profil} User: `{mention}`</b>\n"
    if alasan:
        mmg += f"**Alasan: `{alasan}`**"
    await m.reply(mmg)
    await xx.delete()
    

@ky.ubot("ungmute", sudo=True)
@ky.devs("cungmute")
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    nyet = await c.extract_user(m)
    xx = await m.reply(f"{emo.proses} Processing...")
    user = await c.get_users(nyet)
    if not user:
        await xx.edit(f"{emo.gg} Pengguna tidak ditemukan.")
        return
    if user.id in DEVS:
        await xx.edit(f"{emo.gagal} Dia adalah Developer Mix-Userbot.")
        return
    bs = 0
    gg = 0
    chats = await c.get_user_dialog("group")
    gmute_users = udB.get_list_from_var(c.me.id, "GMUTE", "USER")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = (
            m.reply_to_message.sender_chat.title
            if m.reply_to_message
            else "Anon")
    for chat in chats:
        if user.id not in gmute_users:
            await xx.edit(f"{emo.gagal} Pengguna belum pernah digmute.")
            return
        try:
            udB.remove_from_var(c.me.id, "GMUTE", user.id, "USER")
            GMUTE_USER.remove(user.id)
            await c.unban_member(chat, user.id, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except BaseException:
            gg += 1
            await asyncio.sleep(0.1)
    mmg = f"{emo.alive} <b>Warning Global Ungmute\n\n{emo.sukses} Berhasil: `{bs}` Chat\n{emo.gagal} Gagal: `{gg}` Chat\n{emo.profil} User: `{mention}`</b>\n"
    await m.reply(mmg)
    await xx.delete()
    
    
@ky.ubot("gbanlist|listgban", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    gban_list = []
    msg = await m.reply(f"{emo.proses} <b>Processing...</b>")
    gbanu = udB.get_list_from_var(c.me.id, "GBANNED", "USER")
    if not gbanu:
        return await msg.edit(f"{emo.gagal} <b>Tidak ada pengguna ditemukan.</b>")
    for x in gbanu:
        try:
            user = await c.get_users(int(x))
            gban_list.append(
                f" {emo.profil} • [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code>")
        except:
            continue
    if gban_list:
       stak = (
            f"{emo.profil} <b>Daftar Pengguna:</b>\n"
            + "\n".join(gban_list)
            + f"\n{emo.sukses} <code>{len(gban_list)}</code>"
        )
        return await msg.edit(stak)
    else:
        return await msg.edit(f"{emo.gagal} <b>Eror</b>")
        
        

@ky.ubot("gmutelist|listgmute", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    gmute_list = []
    msg = await m.reply(f"{emo.proses} <b>Processing...</b>")
    gmute = udB.get_list_from_var(c.me.id, "GMUTE", "USER")
    if not gmute:
        return await msg.edit(f"{emo.gagal} <b>Tidak ada pengguna ditemukan.</b>")
    for x in gmute:
        try:
            user = await c.get_users(int(x))
            gmute_list.append(
                f" {emo.profil} • [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code>")
        except:
            continue
    if gmute_list:
       stak = (
            f"{emo.profil} <b>Daftar Pengguna:</b>\n"
            + "\n".join(gmute_list)
            + f"\n{emo.sukses} <code>{len(gmute_list)}</code>"
        )
        return await msg.edit(stak)
    else:
        return await msg.edit(f"{emo.gagal} <b>Eror</b>")