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


from io import BytesIO

from pyrogram.types import *

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
            user_id = ct[1:]
            try:
                org = await c.get_users(user_id)
                rep = await c.get_messages(m.chat.id, m.reply_to_message.id)
                full = f"{org.first_name} {org.last_name or ''}"
                message = m(
                    id=rep.id,
                    from_user=full,
                    date=rep.date,
                    chat=Chat(id=m.chat.id),
                    text=rep.text,
                )
                messages = [message]
            except Exception as e:
                return await m.reply(f"{em.gagal} Error : <code>{e}</code>")
        else:
            ct = isArgInt(ct)
            if ct[0]:
                if ct[1] < 2 or ct[1] > 10:
                    return await m.reply(
                        f"{em.gagal} Argumen yang anda berikan salah..."
                    )
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
            chat_id=m.chat.id, message_ids=m.reply_to_message.id
        )
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


@ky.ubot("qf", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    mk = await m.reply(f"{em.proses} Processing...")
    mk = await message.reply(f"{em.proses} <b>Sedang proses...</b>")
    await asyncio.sleep(2)
    target_user, reason = await extract_user_and_reason(message)
    if target_user is None:
        return await mk.edit(f"{em.gagal} <b>Invalid username format.</b>")

    target_user = str(target_user)
    if not target_user:
        return await mk.edit(f"{em.gagal} <b>Invalid username format.</b>")
    try:
        user = await client.get_users(target_user)
    except errors.exceptions.bad_request_400.UsernameNotOccupied:
        return await mk.edit(f"{em.gagal} <b>Not found a username.</b>")
    except IndexError:
        return await mk.edit(f"{em.gagal} <b>Only for user.</b>")
    if message.reply_to_message:
        rep = message.reply_to_message.text
    else:
        rep = reason if reason else ""
    fake_quote_text = rep
    if not fake_quote_text:
        return await mk.edit(f"{em.gagal} <b>Empty message.</b>")
    q_message = await client.get_messages(message.chat.id, message.id)
    q_message.text = fake_quote_text
    q_message.entities = None
    q_message.from_user.id = user.id
    q_message.from_user.first_name = user.first_name
    q_message.from_user.last_name = user.last_name
    q_message.from_user.username = user.username
    q_message.from_user.photo = user.photo
    url = "https://quotes.fl1yd.su/generate"
    user_auth_1 = b64decode(
        "Y2llIG1hbyBueW9sb25nIGNpaWUuLi4uLCBjb2xvbmcgYWphIGJhbmcgamFkaWluIHByZW0gdHJ1cyBqdWFsLCBrYWxpIGFqYSBiZXJrYWggaWR1cCBsdS4uLi4="
    )
    params = {
        "messages": [await render_message(client, q_message)],
        "quote_color": "#1b1429",
        "text_color": "#fbfbfb",
    }
    response = requests.post(url, json=params)
    if not response.ok:
        return await mk.edit(
            f"{em.gagal} <b>Error!</b>\n" f"<code>{response.text}</code>"
        )
    resized = resize_image(BytesIO(response.content), img_type="webp")
    try:
        func = client.send_sticker
        chat_id = message.chat.id
        await func(chat_id, resized)
    except errors.RPCError as e:
        await mk.edit(e)
    else:
        await mk.delete()
