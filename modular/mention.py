import asyncio
import random

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Mention"
__help__ = "Mention"

berenti = False


def random_emoji():
    emojis = ["👤", "👥", "🧑‍💼", "🧑‍🔬", "🧑‍🚀"]
    return random.choice(emojis)


@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: user, m: Message):
    em = Emojik()
    em.initialize()
    global berenti
    chat_id = m.chat.id
    admins = False
    msg = await m.reply(cgr("proses").format(em.proses))
    berenti = True
    try:
        administrator = []
        async for admin in c.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            administrator.append(admin)
        await c.get_chat_member(chat_id, m.from_user.id)
        admins = administrator
    except Exception as e:
        await m.reply(f"Error : {e}")
        print(e)

    if not admins:
        await m.reply_text("Anda harus menjadi admin untuk menggunakan perintah ini!")
        return

    if berenti:
        await m.reply_text(
            "Proses tagall sedang berlangsung. Harap tunggu sampai selesai atau gunakan perintah stop."
        )
        return

    berenti = False

    if len(m.command) < 2:
        await m.reply_text("Harap berikan teks untuk di-mention.")
        return

    text = " ".join(m.command[1:])

    mention_texts = []
    members = c.get_chat_members(chat_id)
    async for member in members:
        if not berenti:
            break
        if not member.user.is_bot:
            mention_texts.append(f"{random_emoji()} @{member.user.username}")
            if len(mention_texts) == 4:
                mention_text = f"{text}\n"
                mention_text += "\n".join(mention_texts)
                await c.send_message(chat_id, mention_text)
                await asyncio.sleep(2.5)
                mention_texts = []

    if mention_texts:
        mention_text = f"{text}\n"
        mention_text += "\n".join(mention_texts)
        await c.send_message(chat_id, mention_text)
        await asyncio.sleep(2.5)

    berenti = False


@ky.ubot("stop", sudo=True)
async def stop_tagall(c: user, m: Message):
    global berenti
    if not berenti:
        await m.reply_text("Tidak ada proses tagall yang sedang berlangsung.")
        return

    berenti = True
    await m.reply_text("Tagall telah dihentikan.")
