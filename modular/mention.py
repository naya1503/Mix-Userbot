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


@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: user, m: Message):
    em = Emojik()
    em.initialize()
    global berenti
    chat_id = m.chat.id
    admins = False
    berenti = True
    progres = await m.edit(cgr("proses").format(em.proses))
    rep = m.reply_to_message

    try:
        mention_texts = []
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

    if not rep:
        await m.reply(cgr("ment_2").format(em.gagal))
        return

    await progres.delete()

    text = " ".join(m.command[1:]) if len(m.command) >= 2 else None
    rep.text if rep.text else None
    repli_teks = c.get_m(m)
    [repli_teks]
    mention_texts = []
    members = c.get_chat_members(chat_id)
    berenti = True
    count = 0
    async for member in members:
        if not berenti:
            break
        if not member.user.is_bot:
            mention_texts.append(f"[{random_emoji()}](tg://user?id={member.user.id})")
            count += 1
            if len(mention_texts) == 4:
                mention_text = f"{repli_teks}\n\n"  # if reply_text else f"{repli}\n\n"
                mention_text += " ".join(mention_texts)
                try:
                    await c.send_message(chat_id, mention_text)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await c.send_message(chat_id, mention_text)
                await asyncio.sleep(2)
                mention_texts = []

    if mention_texts:
        mention_text = f"{repli_teks}\n\n"  # if reply_text else f"{repli}\n\n"
        mention_text += "\n".join(mention_texts)
        try:
            await c.send_message(chat_id, mention_text)
        except FloodWait as e:
            tunggu = asyncio.slee(e.x)
            await c.send_message(chat_id, f"Silahkan tunggu `{tunggu}` detik")
            await asyncio.sleep(e.x)
            await c.send_message(chat_id, mention_text)
        await asyncio.sleep(2)
    berenti = False
    await m.reply(
        f"{em.sukses} <b>Berhasil melakukan mention kepada <code>{count}</code> anggota.</b>"
    )


@ky.ubot("stop", sudo=True)
async def stop_tagall(c: user, m: Message):
    em = Emojik()
    em.initialize()
    global berenti
    if not berenti:
        await m.reply(cgr("ment_3").format(em.gagal))
        return

    berenti = False
    await m.reply(cgr("ment_4").format(em.sukses))
