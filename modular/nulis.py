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


async def nulis(text):
    meki = SafoneAPI()
    imgs = await meki.write(text)
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
    else:
        text = m.text.split(None, 1)[1]
    meko = await nulis(text)
    await m.reply_media_group([meko], reply_to_message_id=ReplyCheck(m))
    os.remove(meko)
