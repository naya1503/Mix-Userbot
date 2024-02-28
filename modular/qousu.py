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
    acak = None
    messages = None
    men = m.command[1].strip()
    if tag.startswith("@"):
        user_id = await c.extract_user(m)
        try:
            org = await c.get_users(user_id)
            if org.id in DEVS:
                await m.reply(f"{em.gagal} **Si anjing mengatasnamakan Developer!**"
                    )
                return
            rep = await c.get_messages(m.chat.id, m.reply_to_message.id)
            rep.from_user = org
            messages = [rep]
            warna = m.text.split(None, 2)[2]
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
        except Exception as e:
            return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
    else:
        warna = m.text.split(None, 1)[1]
        if warna:
             acak = warna
        else:
             acak = random.choice(loanjing)
        m_one = await c.get_messages(
            chat_id=m.chat.id,
            message_ids=m.reply_to_message.id,
            replies=0)
        messages = [m_one]
    try:
        hasil = await quotly(messages, acak)
        bs = BytesIO(hasil)
        bs.name = "mix.webp"
        await m.reply_sticker(bs)
    except Exception as e:
        return await m.reply(f"{em.gagal} Error : <code>{e}</code>")


 """
            if len(m.command) > 3:
                try:
                    angka = int(m.command[3].strip())
                    if angka > 10:
                        return await m.reply(f"{em.gagal} Batas pesan adalah 10")
                    messages = [
                        i
                        for i in await c.get_messages(
                            chat_id=m.chat.id,
                            message_ids=range(
                                m.reply_to_message.id,
                                m.reply_to_message.id + (angka + 5),
                            ),
                            replies=-1,
                        )
                        if not i.empty and not i.media
                    ]
                except ValueError:
                    pass
                except Exception as e:
                    return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
    else:
 """