################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

import os

from SafoneAPI import SafoneAPI

from Mix import *

__modles__ = "Nulis"
__help__ = "Nulis"


async def nulis(text, page, font, color="black"):
    meki = SafoneAPI()
    imgs = await meki.write(text, page, font, color)
    img_paths = []
    for i, img in enumerate(imgs):
        img_path = f"img{i}.png"
        with open(img_path, "wb") as file:
            file.write(img.getvalue())
        img_paths.append(img_path)
    return img_paths


@ky.ubot("nulis|write", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    if rep:
        text = rep.text or rep.caption
        page = m.text.split(None, 3)[1] if len(m.command) > 1 else None
        font = m.text.split(None, 3)[2] if len(m.command) > 2 else None
        kolor = m.text.split(None, 3)[3] if len(m.command) > 3 else None
        meko = await nulis(text, page, font, kolor)
    elif not rep and len(m.command) > 4:
        text = m.text.split(None, 4)[1]
        page = m.text.split(None, 4)[2] if len(m.command) > 2 else None

        font = m.text.split(None, 4)[3] if len(m.command) > 3 else None

        kolor = m.text.split(None, 4)[4] if len(m.command) > 4 else None
        meko = await nulis(text, page, font, kolor)
    else:
        meko = await nulis(text)
    await m.reply_photo(meko)
    os.remove(meko)
