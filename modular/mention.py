import asyncio
import random

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Mention"
__help__ = get_cgr("help_mention")

berenti = False


def random_emoji():
    emojis = "🍎 🍌 🍉 🍇 🍓 🍒 🍍 🥭 🥝 🍑".split(" ")
    return random.choice(emojis)


"""
@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: nlx, m: Message):
    em = Emojik()
    em.initialize()
    global berenti
    chat_id = m.chat.id
    admins = False
    berenti = True
    progres = await m.edit(cgr("proses").format(em.proses))
    try:
        administrator = []
        async for admin in c.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if not berenti:
                break
            administrator.append(admin)
        await c.get_chat_member(chat_id, m.from_user.id)
        admins = administrator
    except Exception as e:
        await m.reply(cgr("err").format(em.gagal))
        print(e)

    if not admins:
        await m.reply(cgr("ment_1").format(em.gagal))
        return

    if not m.reply_to_message and len(m.command) < 2:
        await m.reply(cgr("ment_2").format(em.gagal))
        return

    send = c.get_text(m)
    text = " ".join(m.command[1:])
    mention_texts = []
    members = c.get_chat_members(chat_id)
    berenti = True
    count = 0
    async for member in members:
        if not berenti:
            break
        if not member.user.is_bot:
            full_name = (
                member.user.first_name + member.user.last_name
                if member.user.last_name
                else member.user.first_name
            )
            mention_texts.append(f"[{random_emoji()}](tg://user?id={member.user.id})")
            count += 1
            if len(mention_texts) == 4:
                mention_text = f"{send}\n\n"
                mention_text += " ".join(mention_texts)
                try:
                    await c.send_message(chat_id, mention_text)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await c.send_message(chat_id, mention_text)
                await asyncio.sleep(2.5)
                mention_texts = []

    if mention_texts:
        repl_text = m.reply_to_message.text
        if repl_text:
            repl_text += "\n\n" + "\n".join(mention_texts)
        else:
            repl_text = " ".join(mention_texts)
        try:
            await c.send_message(chat_id, repl_text)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await c.send_message(chat_id, repl_text)
        await asyncio.sleep(2.5)
    berenti = False
    await progres.delete()
    await m.reply(
        f"{em.sukses} <b>Berhasil melakukan mention kepada <code>{count}</code> anggota.</b>"
    )
"""


@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: nlx, m: Message):
    em = Emojik()
    em.initialize()
    global berenti
    chat_id = m.chat.id
    admins = False
    berenti = True
    progres = await m.edit(cgr("proses").format(em.proses))

    try:
        administrator = []
        async for admin in c.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if not berenti:
                break
            administrator.append(admin)
        await c.get_chat_member(chat_id, m.from_user.id)
        admins = administrator
    except Exception as e:
        await m.reply(cgr("err").format(em.gagal))
        print(e)

    if not admins:
        await m.reply(cgr("ment_1").format(em.gagal))
        return

    if not m.reply_to_message and len(m.command) < 2:
        await m.reply(cgr("ment_2").format(em.gagal))
        return

    send = c.get_text(m)
    text = " ".join(m.command[1:])
    mention_texts = []
    members = c.get_chat_members(chat_id)
    berenti = True
    count = 0

    async for member in members:
        if not berenti:
            break
        if not member.user.is_bot and member.status != "user_status_empty":
            mention_texts.append(f"[{random_emoji()}](tg://user?id={member.user.id})")
            count += 1
            if len(mention_texts) == 4:
                mention_text = f"{send}\n\n"
                mention_text += " ".join(mention_texts)
                try:
                    await c.send_message(chat_id, mention_text)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await c.send_message(chat_id, mention_text)
                await asyncio.sleep(2.5)
                mention_texts = []

    if mention_texts:
        repl_text = m.reply_to_message.text if m.reply_to_message else None
        if repl_text:
            repl_text += "\n\n" + "\n".join(mention_texts)
        else:
            repl_text = " ".join(mention_texts)
        try:
            await c.send_message(chat_id, repl_text)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await c.send_message(chat_id, repl_text)
        await asyncio.sleep(2.5)

    berenti = False
    await progres.delete()
    await m.reply(
        f"{em.sukses} <b>Berhasil melakukan mention kepada <code>{count}</code> anggota.</b>"
    )


@ky.ubot("stop", sudo=True)
async def stop_tagall(c: nlx, m: Message):
    em = Emojik()
    em.initialize()
    global berenti
    if not berenti:
        await m.reply(cgr("ment_3").format(em.gagal))
        return

    berenti = False
    await m.reply(cgr("ment_4").format(em.sukses))
