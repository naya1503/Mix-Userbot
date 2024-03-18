################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
 
 MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
"""
################################################################

import base64
import io
import json
import os
import random

from pyrogram.types import *

from Mix import *
from Mix.core.tools_quote import *

__modles__ = "Quote"
__help__ = get_cgr("help_qot")


async def consu(dok):
    try:
        with open(dok, "rb") as file:
            data_bytes = file.read()
        json_data = json.loads(data_bytes)
        image_data_base64 = json_data.get("image")
        if not image_data_base64:
            raise ValueError("Tidak ada data gambar dalam JSON")
        image_data = base64.b64decode(image_data_base64)
        image_io = io.BytesIO(image_data)
        image_io.name = "quotly.webp"
        return image_io
    except Exception as e:
        print("Error:", e)
        raise


@ky.ubot("qcolor", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    iymek = f"\n• ".join(loanjing)
    jadi = cgr("qot_1").format(em.proses)
    if len(iymek) > 4096:
        with open("qcolor.txt", "w") as file:
            file.write(iymek)
        await m.reply_document("qcolor.txt", caption=cgr("qot_2").format(em.sukses))
        os.remove("qcolor.txt")
    else:
        await m.reply(jadi + iymek)


@ky.ubot("q", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    acak = None
    messages = None
    if len(m.command) > 1:
        tag = m.command[1].strip()
        if tag.startswith("@"):
            user_id = tag[1:]
            try:
                org = await c.get_users(user_id)
                if org.id in DEVS:
                    await m.reply(cgr("qot_3").format(em.gagal))
                    return
                rep = await c.get_messages(m.chat.id, m.reply_to_message.id, replies=0)
                rep.from_user = org
                messages = [rep]
            except Exception as e:
                return await m.reply(cgr("err").format(em.gagal, e))
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

        elif int(tag):
            if int(tag) > 10:
                return await m.reply(cgr("qot_4").format(em.gagal))
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
        acak = random.choice(loanjing)
        m_one = await c.get_messages(
            chat_id=m.chat.id, message_ids=m.reply_to_message.id, replies=0
        )
        messages = [m_one]
    try:
        hasil = await quotly(messages, acak)
        with open("hasil.json", "w") as file:
            file.write(hasil.decode())
        stik = await consu("hasil.json")
        await m.reply_sticker(stik)
    except Exception as e:
        return await m.reply(cgr("err").format(em.gagal, e))
