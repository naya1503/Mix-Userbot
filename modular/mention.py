import random
import asyncio

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
    global berenti
    berenti = False
    chat_id = m.chat.id
    admins = False
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

    berenti = True

    if len(m.command) < 2:
        await m.reply_text("Harap berikan teks untuk di-mention.")
        return

    text = " ".join(m.command[1:])

    mention_texts = []
    members = c.get_chat_members(chat_id)  # Menggunakan get_chat_members tanpa await
    async for member in members:
        if not member.user.is_bot:
            mention_texts.append(f"{random_emoji()} @{member.user.username}")
            if len(mention_texts) == 4:
                mention_text = f"{text}\n"
                mention_text += "\n".join(mention_texts)
                await m.reply_text(mention_text)
                mention_texts = []
                await asyncio.sleep(2.5)  # Menambah jeda 2,5 detik

    if mention_texts:
        mention_text = f"{text}\n"
        mention_text += "\n".join(mention_texts)
        await m.reply_text(mention_text)

    berenti = False


@ky.ubot("cstop", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    global berenti
    if not berenti:
        return await m.reply(cgr("spm_3").format(em.gagal))
    berenti = False
    await m.reply(cgr("spm_4").format(em.sukses))
    return
