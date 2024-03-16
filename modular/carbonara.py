################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

import os
import random

from SafoneAPI import SafoneAPI

from Mix import *
from Mix.core.tools_quote import *

__modles__ = "Carbon"
__help__ = get_cgr("help_carbon")


async def buat_bon(code, bgne, language, theme):
    meki = SafoneAPI()
    bg = {
        "backgroundColor": bgne,
        "fontFamily": "Roboto",
        "fontSize": "14px",
        "language": language,
        "theme": theme,
    }
    img = await meki.carbon(code, **bg)
    with open("carbon.png", "wb") as file:
        file.write(img.getvalue())
    return "carbon.png"


@ky.ubot("bglist", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    iymek = f"\n• ".join(loanjing)
    jadi = cgr("qot_1").format(em.proses)
    if len(iymek) > 4096:
        with open("bglist.txt", "w") as file:
            file.write(iymek)
        await m.reply_document("bglist.txt", caption=cgr("qot_2").format(em.sukses))
        os.remove("bglist.txt")
    else:
        await m.reply(jadi + iymek)


@ky.ubot("carbon|carbonara", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    text = m.reply_to_message.text or m.reply_to_message.caption
    acak = None
    if not text:
        return await m.reply(cgr("crbn_1").format(em.gagal))
    ex = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) == 1 and text:
        acak = random.choice(loanjing)
        tem = random.choice(loanjing)
        meg = await buat_bon(text, acak, "python", tem)
        await m.reply_photo(
            meg,
            caption=cgr("crbn_2").format(
                em.sukses, nlx.me.mention, reply_to_message_id=ReplyCheck(m)
            ),
        )
        os.remove(meg)
    elif len(m.command) == 2:
        warna = m.text.split(None, 1)[1] if len(m.command) > 1 else None
        if warna:
            acak = warna
        else:
            acak = random.choice(loanjing)
        tem = random.choice(loanjing)
        meg = await buat_bon(text, acak, "python", tem)
        await m.reply_photo(
            meg,
            caption=cgr("crbn_2").format(
                em.sukses, nlx.me.mention, reply_to_message_id=ReplyCheck(m)
            ),
        )
        os.remove(meg)
    elif len(m.command) == 3:
        warna = m.text.split(None, 2)[1] if len(m.command) > 2 else None
        if warna:
            acak = warna
        else:
            acak = random.choice(loanjing)
        tema = m.text.split(None, 2)[2] if len(m.command) > 3 else None
        if tema:
            tem = tema
        else:
            tem = random.choice(loanjing)
        meg = await buat_bon(text, acak, "python", tem)
        await m.reply_photo(
            meg,
            caption=cgr("crbn_2").format(
                em.sukses, nlx.me.mention, reply_to_message_id=ReplyCheck(m)
            ),
        )
        os.remove(meg)
    elif len(m.command) == 4:
        warna = m.text.split(None, 3)[1] if len(m.command) > 1 else None
        if warna:
            acak = warna
        else:
            acak = random.choice(loanjing)
        tema = m.text.split(None, 2)[2] if len(m.command) > 2 else None
        if tema:
            tem = tema
        else:
            tem = random.choice(loanjing)
        lague = m.text.split(None, 3)[3] if len(m.command) > 3 else "python"
        meg = await buat_bon(text, acak, lague, tem)
        await m.reply_photo(
            meg,
            caption=cgr("crbn_2").format(
                em.sukses, nlx.me.mention, reply_to_message_id=ReplyCheck(m)
            ),
        )
        os.remove(meg)
    else:
        await m.reply(cgr("crbn_1").format(em.gagal))
    await ex.delete()
    return
