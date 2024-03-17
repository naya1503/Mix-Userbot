################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

import os
from io import BytesIO

from pyrogram.types import InputMediaPhoto
from SafoneAPI import SafoneAPI

from Mix import *

__modles__ = "Nulis"
__help__ = get_cgr("help_nul")


async def nulis(text):
    meki = SafoneAPI()
    imgs = await meki.write(text)
    media = []

    if isinstance(imgs, BytesIO):
        img_paths = ["nulis.png"]
    else:
        img_paths = [f"nulis_{i+1}.png" for i in range(len(imgs))]

    if isinstance(imgs, BytesIO):
        imgs = [imgs]

    for i, img in enumerate(imgs):
        img_path = img_paths[i]
        with open(img_path, "wb") as file:
            file.write(img.getvalue())
        media.append(InputMediaPhoto(img_path))
    return media


@ky.ubot("nulis|write", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    if rep:
        text = rep.text or rep.caption
    else:
        text = m.text.split(None, 1)[1]
    prose = await m.reply(cgr("proses").format(em.proses))
    try:
        meko = await nulis(text)
    except Exception as er:
        await m.reply(cgr("err").format(em.gagal, er))
        return
    await m.reply_media_group(meko, reply_to_message_id=ReplyCheck(m))
    await prose.delete()
    try:
        for mm in meko:
            os.remove(mm.media)
    except:
        pass
    return
