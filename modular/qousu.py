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


from base64 import b64decode

from pyrogram.types import *
from io import BytesIO

from Mix import *
from Mix.core.tools_quote import *


@ky.ubot("q", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    mk = await m.reply(f"{em.proses} Processing...")
    
    if len(m.text.split()) > 1:
        ct = m.command[1].strip()
        if ct.startswith("@"):
            user_id = await c.extract_user(m)
            try:
                user = await c.get_users(user_id)
                rep = await c.get_messages(m.chat.id, m.reply_to_message.id)
                message = Message(
                    id=rep.id,
                    from_user=user.first_name user.last_name or '',
                    date=rep.date,
                    chat=m.chat.id,
                    text=rep.text,
                )
                messages = [message]
            except Exception as e:
                return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
        else:
            ct = isArgInt(ct)
            if ct[0]:
                if ct[1] < 2 or ct[1] > 10:
                    return await m.reply(f"{em.gagal} Argumen yang anda berikan salah...")
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
            else:
                return await m.reply(f"{em.gagal} Argumen yang anda berikan salah...")
        try:
            hasil = await quotly(messages)
            bs = BytesIO(hasil)
            bs.name = "mix.webp"
            return await m.reply_sticker(bs)
        except Exception as e:
            return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
    try:
        m_one = await c.get_messages(
            chat_id=m.chat.id, message_ids=m.reply_to_message.id)
        messages = [m_one]
    except Exception as e:
        return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
    try:
        hasil = await quotly(messages)
        bs = BytesIO(hasil)
        bs.name = "mix.webp"
        return await m.reply_sticker(bs)
    except Exception as e:
        return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
    await mk.delete()
