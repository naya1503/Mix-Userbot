################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


__modles__ = "Broadcast"
__help__ = """
 Help Command Gcast

• Perintah : <code>{0}gucast</code> [balas pesan/kirim pesan]
• Penjelasan : Untuk pengirim pesan ke semua pengguna.

• Perintah : <code>{0}gcast</code> [balas pesan/kirim pesan]
• Penjelasan : Untuk pengirim pesan ke semua grup.

• Perintah: <code>{0}addbl</code>
• Penjelasan: Menambahkan grup kedalam anti Gcast.

• Perintah: <code>{0}delbl</code>
• Penjelasan: Menghapus grup dari daftar anti Gcast.

• Perintah: <code>{0}rmall</code>
• Penjelasan: Menghapus semua grup dari daftar anti Gcast.

• Perintah: <code>{0}listbl</code>
• Penjelasan: Melihat daftar grup anti Gcast.

• Perintah : <code>{0}send</code> [username/user_id - teks/reply]
• Penjelasan : Untuk mengirim pesan ke pengguna/grup/channel.
"""

import asyncio
from gc import get_objects

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from telegraph import upload_file

from Mix import *


async def refresh_dialog(query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
        "all": [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL],
        "ch": [ChatType.CHANNEL],
        "allread": [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
            ChatType.PRIVATE,
        ],
    }
    async for xxone in user.get_dialogs():
        if xxone.chat.type in chat_types[query]:
            chats.append(xxone.chat.id)
    return chats


@ky.ubot("gcast", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    direp = m.reply_to_message
    if direp:
        send = direp.text
    else:
        send = c.get_m(m)
    if not send:
        return await msg.edit(cgr("gcs_1").format(em.gagal))
    chats = await refresh_dialog("group")
    blacklist = udB.get_chat(c.me.id)
    done = 0
    failed = 0
    for chat in chats:

        if chat not in blacklist and chat not in NO_GCAST:
            try:
                await c.send_message(chat, send)
                done += 1
                await asyncio.sleep(0.2)
            except UserBannedInChannel:
                continue
            except SlowmodeWait:
                continue
            except PeerIdInvalid:
                continue
            except FloodWait as e:
                await asyncio.sleep(int(e))
                try:
                    await c.send_message(chat, send)
                    done += 1
                except Exception:
                    failed += 1

    return await msg.edit(
        cgr("gcs_2").format(em.alive, em.sukses, done, em.gagal, failed)
    )


@ky.ubot("gucast", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    direp = m.reply_to_message
    if direp:
        send = direp.text
    else:
        send = c.get_m(m)
    if not send:
        return await msg.edit(cgr("gcs_1").format(em.gagal))
    chats = await refresh_dialog("users")
    blacklist = udB.get_chat(c.me.id)
    done = 0
    failed = 0
    for chat in chats:
        if chat not in blacklist and chat not in DEVS:
            try:
                await c.send_message(chat, send)
                done += 1
            except PeerIdInvalid:
                continue
            except FloodWait as e:
                await asyncio.sleep(int(e))
                try:
                    await c.send_message(chat, send)
                    done += 1
                except Exception:
                    failed += 1

    return await msg.edit(
        cgr("gcs_3").format(em.alive, em.sukses, done, em.gagal, failed)
    )


@ky.ubot("addbl", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    pp = await m.reply(cgr("proses").format(em.proses))
    chat_id = m.chat.id
    blacklist = udB.get_chat(c.me.id)
    if chat_id in blacklist:
        return await pp.edit(cgr("gcs_4").format(em.sukses))
    add_blacklist = udB.add_chat(c.me.id, chat_id)
    if add_blacklist:
        await pp.edit(cgr("gcs_5").format(em.sukses, m.chat.id, m.chat.title))
        return
    else:
        await pp.edit(cgr("gcs_6").format(em.sukses, m.chat.id))
        return


@ky.ubot("delbl", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    pp = await m.reply(cgr("proses").format(em.proses))
    try:
        if not c.get_arg(m):
            chat_id = m.chat.id
        else:
            chat_id = int(m.command[1])
        blacklist = udB.get_chat(c.me.id)
        if chat_id not in blacklist:
            return await pp.edit(cgr("gcs_7").format(em.gagal, m.chat.id, m.chat.title))
        del_blacklist = udB.remove_chat(c.me.id, chat_id)
        if del_blacklist:
            await pp.edit(cgr("gcs_8").format(em.sukses, chat_id))
            return
        else:
            await pp.edit(cgr("gcs_9").format(em.gagal, chat_id))
            return
    except Exception as error:
        await pp.edit(str(error))


@ky.ubot("listbl", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    pp = await m.reply(cgr("proses").format(em.proses))

    msg = cgr("gcs_10").format(em.sukses, int(len(udB.get_chat(c.me.id))))
    for x in udB.get_chat(c.me.id):
        try:
            get = await c.get_chat(x)
            msg += cgr("gcs_11").format(get.title, get.id)
        except:
            msg += cgr("gcs_12").format(x)
    await pp.delete()
    await m.reply(msg)


@ky.ubot("rmall", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    get_bls = udB.get_chat(c.me.id)
    if len(get_bls) == 0:
        return await msg.edit(cgr("gcs_13").format(em.gagal))
    for x in get_bls:
        udB.remove_chat(c.me.id, x)
    await msg.edit(cgr("gcs_14").format(em.sukses))