import random
import re

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Mention"
__help__ = "Mention"

takolanjing = False


def random_emoji():
    emojis = ["👤", "👥", "🧑‍💼", "🧑‍🔬", "🧑‍🚀"]
    return random.choice(emojis)


@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: user, m: Message):
    global takolanjing
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

    if takolanjing:
        await m.reply_text(
            "Proses tagall sedang berlangsung. Harap tunggu sampai selesai atau gunakan perintah stop."
        )
        return

    takolanjing = True

    if len(m.command) < 2:
        await m.reply_text("Harap berikan teks untuk di-mention.")
        return

    text = " ".join(m.command[1:])

    username_pattern = re.compile(r"@[\w\d_]+")
    members = c.get_chat_members(chat_id)
    mention_text = f"{text}\n"
    member_count = 0
    mention_texts = []
    for member in members:
        if not member.user.is_bot:
            mention_texts.append(f"{random_emoji()} @{member.user.username}")
            member_count += 1
            if member_count == 4:
                mention_text += "\n".join(mention_texts)
                mention_texts = []
                member_count = 0
                await m.reply_text(mention_text)
                mention_text = f"{text}\n"

    if mention_texts:
        mention_text += "\n".join(mention_texts)
        await m.reply_text(mention_text)

    takolanjing = False


@ky.ubot("stop", sudo=True)
async def stop_tagall(c: user, m: Message):
    global takolanjing
    if not takolanjing:
        await m.reply_text("Tidak ada proses tagall yang sedang berlangsung.")
        return

    takolanjing = False
    await m.reply_text("Tagall telah dihentikan.")
