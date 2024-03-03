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
    if str(chat_id) in blacklist:
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


# @Tomi


@ky.ubot("send", sudo=True)
async def _(c: user, m):
    if m.reply_to_message:
        chat_id = m.chat.id if len(m.command) < 2 else m.text.split()[1]
        try:
            if c.me.id != bot.me.id:
                if m.reply_to_message.reply_markup:
                    x = await c.get_inline_bot_results(
                        bot.me.username, f"_send_ {id(m)}"
                    )
                    return await c.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await m.reply(error)
        else:
            try:
                return await m.reply_to_message.copy(chat_id)
            except Exception as t:
                return await m.reply(f"{t}")
    else:
        if len(m.command) < 3:
            return
        chat_id, chat_text = m.text.split(None, 2)[1:]
        try:
            if "/" in chat_id:
                to_chat, msg_id = chat_id.split("/")
                return await c.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
            else:
                return await c.send_message(chat_id, chat_text)
        except Exception as t:
            return await m.reply(f"{t}")


@ky.inline("^_send_")
async def send_inline(c, iq):
    try:
        _id = int(iq.query.split()[1])
        m = [obj for obj in get_objects() if id(obj) == _id][0]

        if m.reply_to_message.photo:
            m_d = await m.reply_to_message.download()
            photo_tg = upload_file(m_d)
            cp = m.reply_to_message.caption
            text = cp if cp else ""
            hasil = [
                InlineQueryResultPhoto(
                    photo_url=f"https://telegra.ph/{photo_tg[0]}",
                    title="kon",
                    reply_markup=m.reply_to_message.reply_markup,
                    caption=text,
                ),
            ]
            os.remove(m_d)
        else:
            hasil = [
                InlineQueryResultArticle(
                    title="kon",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ]
        await c.answer_inline_query(
            iq.id,
            cache_time=0,
            results=hasil,
        )
    except Exception as e:
        LOGGER.info(f"Error: {e}")
