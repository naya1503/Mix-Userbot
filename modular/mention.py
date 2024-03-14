import re

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from modular.info import *
from Mix import *
from Mix.modular.info import *

__modles__ = "Mention"
__help__ = "Mention"


@ky.ubot("tagall|mention", sudo=True)
async def mention_all(c: Client, m: Message):
    chat_id = m.chat.id
    administrator = False
    try:
        chat_member = await c.get_chat_member(chat_id, m.from_user.id)
        administrator = chat_member.status in ("administrator", "creator")
    except Exception as e:
        print(e)

    if not administrator:
        await m.reply_text("Anda harus menjadi admin untuk menggunakan perintah ini!")
        return

    if m.reply_to_message:
        target_message = m.reply_to_message
    else:
        target_message = m

    if len(m.command) > 1:
        text = " ".join(m.command[1:])
    else:
        text = None

    if text is None:
        await m.reply_text("Harap berikan saya teks atau balas sebuah pesan.")
        return

    username_pattern = re.compile(r"@[\w\d_]+")
    async for member in c.iter_chat_members(chat_id):
        if not member.user.is_bot:
            mention_text = re.sub(username_pattern, f"@{member.user.username}", text)
            await target_message.reply(mention_text)
