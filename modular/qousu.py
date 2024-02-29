################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty
 
 MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
"""
################################################################


__modles__ = "Quote"
__help__ = """
Help Command Quote

• Perintah: <code>{0}q</code> [reply message]
• Penjelasan: Untuk membuat quote teks.

• Perintah: <code>{0}qcolor</code>
• Penjelasan: Untuk melihat format warna latar belakang quote.

**Notes Optional:**
`q @username` - Menjadi fake quote.
`q warna` - Kostum latar belakang quote.
`q @username warna` Menjadi fake quote dengan latar belakang kostum.
"""

import os
import random
from io import BytesIO

from pyrogram.types import *

from Mix import *
from Mix.core.tools_quote import *


@ky.ubot("qcolor", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    iymek = "\n".join(loanjing)
    if len(iymek) > 4096:
        with open("qcolor.txt", "w") as file:
            file.write(iymek)
        await m.reply_document(
            "qcolor.txt",
            caption=f"{em.sukses} Ini adalah list warna untuk latar belakang quote.",
        )
        os.remove("qcolor.txt")
    else:
        await m.reply(iymek)


@ky.ubot("q", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    acak = None
    messages = None
    tag = m.command[1].strip()
    c.get_arg(m)
    if len(m.command) > 1:
        if tag.startswith("@"):
            user_id = tag[1:]
            try:
                org = await c.get_users(user_id)
                if org.id in DEVS:
                    await m.reply(
                        f"{em.gagal} **Si anjing mengatasnamakan Developer!**"
                    )
                    return
                rep = await c.get_messages(m.chat.id, m.reply_to_message.id, replies=0)
                rep.from_user = org
                messages = [rep]
            except Exception as e:
                return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
            warna = m.text.split(None, 2)[2] if len(m.command) > 2 else None
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
        elif not tag.startswith("@"):
            warna = m.text.split(None, 1)[1] if len(m.command) > 1 else None
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
            m_one = await c.get_messages(
                chat_id=m.chat.id, message_ids=m.reply_to_message.id, replies=0
            )
            messages = [m_one]
    else:
        if tag.isnumeric():
            if int(tag) > 10:
                return await m.reply(f"{em.gagal} Batas pesan adalah 10")
            warna = m.text.split(None, 2)[2] if len(m.command) > 2 else None
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
            messages = [
                i
                for i in await c.get_messages(
                    chat_id=m.chat.id,
                    message_ids=range(
                        m.reply_to_message.id,
                        m.reply_to_message.id + int(tag),
                    ),
                    replies=0,
                )
                if not i.empty and not i.media
            ]
        else:
            m_one = await c.get_messages(
                chat_id=m.chat.id, message_ids=m.reply_to_message.id, replies=0
            )
            messages = [m_one]
    try:
        hasil = await quotly(messages, acak)
        bs = BytesIO(hasil)
        bs.name = "mix.webp"
        await m.reply_sticker(bs)
    except Exception as e:
        return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
