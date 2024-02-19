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

from pyrogram.errors import *
from pyrogram.types import *
from telegraph import upload_file

from Mix import *


@ky.ubot("gcast", sudo=True)
async def _(c: user, m):

    msg = await m.reply(f"{proses} Processing...")
    send = c.get_m(m)
    if not send:
        return await msg.edit(f"{gagal} Silakan balas ke pesan atau berikan pesan.")
    chats = await c.get_user_dialog("group")
    blacklist = udB.get_chat(c.me.id)
    done = 0
    failed = 0
    for chat in chats:
        if chat not in blacklist and chat not in NO_GCAST:
            try:
                if m.reply_to_message:
                    await send.copy(chat)
                else:
                    await c.send_message(chat, send)
                done += 1
                await asyncio.sleep(2)
            except SlowmodeWait:
                continue
            except Exception:
                continue
            except BaseException:
                failed += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
    return await msg.edit(
        f"""
{alive} Broadcast Message Sent :
{sukses} Success in <code>{done}</code> Group.
{gagal} Failed at <code>{failed}</code> Group.""",
    )


@ky.ubot("gucast", sudo=True)
async def _(c: user, m):

    msg = await m.reply(f"{proses} Processing...")
    send = c.get_m(m)
    if not send:
        return await msg.edit(f"{gagal} Silakan balas ke pesan atau berikan pesan.")
    chats = await c.get_user_dialog("users")
    blacklist = udB.get_chat(c.me.id)
    done = 0
    failed = 0
    for chat in chats:
        if chat not in blacklist and chat not in DEVS:
            try:
                if m.reply_to_message:
                    await send.copy(chat)
                else:
                    await c.send_message(chat, send)
                done += 1
                await asyncio.sleep(2)
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception:
                continue
            except BaseException:
                failed += 1
    return await msg.edit(
        f"""
{alive} Broadcast Message Sent :
{sukses} Success in <code>{done}</code> Group.
{gagal} Failed at <code>{failed}</code> Group.""",
    )


@ky.ubot("addbl", sudo=True)
async def _(c: user, m):

    pp = await m.reply(f"{proses} Processing...")
    chat_id = m.chat.id
    blacklist = udB.get_chat(c.me.id)
    if str(chat_id) in blacklist:
        return await pp.edit(f"{sukses} <b>Grup ini sudah ada dalam blacklist</b>")
    add_blacklist = udB.add_chat(c.me.id, chat_id)
    if add_blacklist:
        await pp.edit(
            f"{sukses} <b><code>{m.chat.id}</code> | {m.chat.title} berhasil ditambahkan ke dalam blacklist.</b>"
        )
    else:
        await pp.edit(f"{gagal} <b>Error.</b>")


@ky.ubot("delbl", sudo=True)
async def _(c: user, m):

    pp = await m.reply(f"{proses} <b>Processing...</b>")
    try:
        if not c.get_arg(m):
            chat_id = m.chat.id
        else:
            chat_id = int(m.command[1])
        blacklist = udB.get_chat(c.me.id)
        if chat_id not in blacklist:
            return await pp.edit(
                f"{gagal} <b><code>{m.chat.id}</code> | {m.chat.title} tidak ada dalam daftar blacklist.</b>"
            )
        del_blacklist = udB.remove_chat(c.me.id, chat_id)
        if del_blacklist:
            await pp.edit(
                f"{sukses} <b><code>{chat_id}</code> berhasil dihapus dari daftar blacklist.</b>"
            )
        else:
            await pp.edit(f"{gagal} <b>Error.</b>")
    except Exception as error:
        await pp.edit(str(error))


@ky.ubot("listbl", sudo=True)
async def _(c: user, m):

    pp = await m.reply(f"{proses} <b>Processing...</b>")

    msg = f"{sukses} <b>• Total blacklist {int( len(udB.get_chat(c.me.id)))}</b>\n\n"
    for x in udB.get_chat(c.me.id):
        try:
            get = await c.get_chat(x)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await pp.delete()
    await m.reply(msg)


@ky.ubot("rmall", sudo=True)
async def _(c: user, m):

    msg = await m.reply(f"{proses} <b>Processing....</b>")
    get_bls = udB.get_chat(c.me.id)
    if len(get_bls) == 0:
        return await msg.edit(f"{gagal} <b>Daftar hitam Anda kosong.</b>")
    for x in get_bls:
        udB.remove_chat(c.me.id, x)
    await msg.edit(f"{sukses} <b>Semua daftar hitam telah berhasil dihapus.</b>")


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
            return await m.reply("Ga gitu.")
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
