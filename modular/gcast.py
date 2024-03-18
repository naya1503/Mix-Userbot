################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import asyncio

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Broadcast"
__help__ = get_cgr("help_gcast")


async def digikes_(q):
    chats = []
    chat_types = {
        "gikes": [ChatType.GROUP, ChatType.SUPERGROUP],
        "gucast": [ChatType.PRIVATE],
    }
    async for dialog in nlx.get_dialogs():
        if dialog.chat.type in chat_types[q]:
            chats.append(dialog.chat.id)

    return chats


@ky.ubot("gcast", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    send = c.get_m(m)
    if not send:
        return await msg.edit(cgr("gcs_1").format(em.gagal))
    blacklist = udB.get_chat(c.me.id)
    chats = await digikes_("gikes")
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
                await asyncio.sleep(0.3)
            except (
                UserBannedInChannel,
                SlowmodeWait,
                PeerIdInvalid,
                Forbidden,
                ChatWriteForbidden,
            ):
                continue
            except FloodWait as e:
                await asyncio.sleep(e.value)
                try:
                    if m.reply_to_message:
                        await send.copy(chat)
                    else:
                        await c.send_message(chat, send)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    failed += 1
                    await asyncio.sleep(0.3)

    return await msg.edit(
        cgr("gcs_2").format(em.alive, em.sukses, done, em.gagal, failed)
    )


@ky.ubot("gucast", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    send = c.get_m(m)
    if not send:
        return await msg.edit(cgr("gcs_1").format(em.gagal))
    chats = await digikes_("gucast")
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
                await asyncio.sleep(0.3)
            except PeerIdInvalid:
                continue
            except FloodWait as e:
                await asyncio.sleep(e.value)
                try:
                    if m.reply_to_message:
                        await send.copy(chat)
                    else:
                        await c.send_message(chat, send)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    failed += 1
                    await asyncio.sleep(0.3)

    return await msg.edit(
        cgr("gcs_3").format(em.alive, em.sukses, done, em.gagal, failed)
    )


@ky.ubot("addbl", sudo=True)
async def _(c: nlx, m):
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
async def _(c: nlx, m):
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
async def _(c: nlx, m):
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
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    get_bls = udB.get_chat(c.me.id)
    if len(get_bls) == 0:
        return await msg.edit(cgr("gcs_13").format(em.gagal))
    for x in get_bls:
        udB.remove_chat(c.me.id, x)
    await msg.edit(cgr("gcs_14").format(em.sukses))


@ky.ubot("send", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message:
        chat_id = m.chat.id if len(m.command) < 2 else m.text.split()[1]
        try:
            if c.me.id != bot.me.id:
                if m.reply_to_message.reply_markup:
                    x = await c.get_inline_bot_results(
                        bot.me.username, f"_send_ {id(m)}"
                    )
                    await c.send_inline_bot_result(chat_id, x.query_id, x.results[0].id)
                    await m.delete()
                    return
        except Exception as error:
            return await m.reply(error)
        else:
            try:
                await m.reply_to_message.copy(chat_id)
                await m.delete()
                return
            except Exception as t:
                return await m.reply(f"{t}")
    else:
        if len(m.command) < 3:
            return
        chat_id, chat_text = m.text.split(None, 2)[1:]
        try:
            if "/" in chat_id:
                to_chat, msg_id = chat_id.split("/")
                await c.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
                await m.delete()
                return
            else:
                await c.send_message(chat_id, chat_text)
                await m.delete()
                return
        except Exception as t:
            return await m.reply(f"{t}")
