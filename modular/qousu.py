################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty
 
 MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
"""
################################################################

"""
__modles__ = "Quote"
__help__ = "
Help Command Quote

• Perintah: <code>{0}q</code>
• Penjelasan: Untuk membuat qoute teks.
"""


import random
from io import BytesIO

from pyrogram.types import *

from Mix import *
from Mix.core.tools_quote import *


@ky.ubot("q", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    mk = await m.reply(f"{em.proses} Processing...")
    acak = None
    messages = None
    if len(m.command) == 1:
        m_one = await c.get_messages(
            chat_id=m.chat.id,
            message_ids=m.reply_to_message.id,
            replies=0,
        )
        messages = [m_one]
    elif len(m.command) > 2:
        tag = m.command[1].strip()
        ct = isArgInt(m.command[1])
        if tag.startswith("@"):
            user_id = tag[1:]
            try:
                org = await c.get_users(user_id)
                if org.id in DEVS:
                    await mk.edit(
                        f"{em.gagal} **Si anjing mengatasnamakan Developer!**"
                    )
                    return
                rep = await c.get_messages(m.chat.id, m.reply_to_message.id)
                rep.from_user = org
                messages = [rep]
            except Exception as e:
                return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
        else:
            warna = m.text.split()[2].strip().lower()
            if warna in loanjing:
                acak = warna
            else:
                acak = random.choice(loanjing)
            if ct[0]:
                if ct[1] < 2 or ct[1] > 10:
                    return await m.reply(f"{em.gagal} Batas pesan adalah 10")
                try:
                    messages = [
                        i
                        for i in await c.get_messages(
                            chat_id=m.chat.id,
                            message_ids=range(
                                m.reply_to_message.id,
                                m.reply_to_message.id + (ct[1] + 5),
                            ),
                            replies=-1,
                        )
                        if not i.empty and not i.media
                    ]
                except Exception as e:
                    return await m.reply(f"{em.gagal} Error : <code>{e}</code>")

    try:
        hasil = await quotly(messages, acak)
        bs = BytesIO(hasil)
        bs.name = "mix.webp"
        await m.reply_sticker(bs)
    except Exception as e:
        return await m.reply(f"{em.gagal} Error : <code>{e}</code>")

    await mk.delete()
    return
