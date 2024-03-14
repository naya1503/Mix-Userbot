import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Mention"
__help__ = "Mention"



@ky.ubot("tagall|mention", sudo=True)
async def _(c, m):
    chat_id = m.chat.id
    if m.chat.type == ChatType.PRIVATE:
        return await m.reply(
            "Perintah ini hanya bisa digunakan untuk Grup atau Channel"
        )

    is_admin = False
    try:
        participant = await c.get_chat_member(chat_id, m.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR):
            is_admin = True
    if not is_admin:
        return await m.reply_text(
            "Hanya admin grup yang bisa menggunakan perintah ini!"
        )

    usrnum = 0
    usrtxt = ""
    if m.text and m.reply_to_message:
        return await m.reply_text("Berikan saya argumen!")
    elif m.text:
        mode = "text_on_cmd"
        msg = m.text
    elif m.reply_to_message:
        mode = "text_on_reply"
        msg = m.reply_to_message
        if msg is None:
            return await m.reply_text(
                "Saya tidak bisa melakukan tagall dari pesan yang sebelumnya tidak ada"
            )
    else:
        return await m.reply_text(
            "Berikan saya pesan atau balas pesan untuk melakukan tagall"
        )

    async for user in c.iter_chat_members(chat_id):
        if user.status == ChatMemberStatus.KICKED:
            continue
        usrnum += 1
        usrtxt += f"[{user.user.first_name}](tg://user?id={user.user.id}) "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await c.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply_text(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
