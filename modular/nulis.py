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


async def nulis(text, page=None, font=None, color="black"):
    meki = SafoneAPI()
    img = await meki.write(text, page, font, color)
    with open("nulis.png", "wb") as file:
        file.write(img.getvalue())
    return "nulis.png"


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
    await m.reply_photo(meko)
    os.remove(meko)
