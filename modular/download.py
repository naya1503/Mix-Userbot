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

__modles__ = "Download"
__help__ = "Download"


async def kirim_pesan_dan_tunggu(chat_id, pesan):
    sent_message = await user.send_message(chat_id, pesan)
    await asyncio.sleep(10)
    replied_message = await user.get_messages(chat_id, sent_message.message_id)
    await user.send_message(chat_id, replied_message.text)


@ky.ubot("sos", sudo=True)
async def _(c, m):
    _, *args = m.text.split()
    
    if args and args[0].startswith("{") and args[0].endswith("}"):
        command = args[0].strip("{}")
        
        if command == "tik":
            if len(args) >= 2:
                link_tiktok = args[1]
                pesan_tiktok = f"/tiktok {link_tiktok}"
                await kirim_pesan_dan_tunggu(m.chat.id, pesan_tiktok)
        elif command == "tube":
            if len(args) >= 2:
                link_youtube = args[1]
                pesan_youtube = f"/youtube {link_youtube}"
                await kirim_pesan_dan_tunggu(m.chat.id, pesan_youtube)