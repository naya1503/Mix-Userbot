import asyncio
import re
import random

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Mention"
__help__ = "Mention"


@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: user, m: Message):
    global tagall_active
    chat_id = m.chat.id
    admins = False
    try:
        administrator = []
        async for admin in c.get_chat_members(
            chat_id=m.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
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

    if tagall_active:
        await m.reply_text(
            "Proses tagall sedang berlangsung. Harap tunggu sampai selesai atau gunakan perintah stop."
        )
        return

    tagall_active = True

    if len(m.command) < 2:
        await m.reply_text("Harap berikan teks untuk di-mention.")
        return

    text = " ".join(m.command[1:])

    username_pattern = re.compile(r"@[\w\d_]+")
    for member in await c.get_chat_members(chat_id):
        if not member.user.is_bot:
            profile_link_emoji = random.choice(["👤", "👥", "🧑‍💼", "🧑‍🔬", "🧑‍🚀"])
            mention_text = f"{text}\n\n{profile_link_emoji} [{member.user.first_name}](tg://user?id={member.user.id})"
            await c.send_message(chat_id, mention_text)
            await asyncio.sleep(2)

    tagall_active = False


@ky.ubot("stop", sudo=True)
async def _(c: user, m: Message):
    global tagall_active
    tagall_active = False
    await m.reply_text("Tagall telah dihentikan.")
