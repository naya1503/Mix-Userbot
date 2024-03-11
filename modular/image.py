################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

import os
from io import BytesIO

import requests
from pyrogram.types import InputMediaPhoto
from SafoneAPI import SafoneAPI

from Mix import *

__modles__ = "Image"
__help__ = "Image"


async def search_image_and_reply(query, m, lim=None):
    meki = SafoneAPI()
    results = await meki.image(query, lim)
    img_res = results.get("results", [])
    for img_inf in img_res:
        image_url = img_inf.get("imageUrl")
        if image_url and image_url.startswith("http"):
            response = requests.get(image_url)
            if response.status_code == 200:
                img = BytesIO(response.content)
                media = InputMediaPhoto(img)
                await m.reply_media_group([media], reply_to_message_id=ReplyCheck(m))
                os.remove(media)
            else:
                continue
        else:
            continue


@ky.ubot("image", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    if not rep and len(m.command) < 2:
        await m.reply(f"{em.gagal} **MINIMAL KASIH QUERY BWANG!!**")
    pros = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) == 2 and rep.text:
        txt = rep.text
        await search_image_and_reply(txt, m, 1)
    elif len(m.command) == 3:
        txt = m.text.split(None, 2)[1]
        lim = m.text.split(None, 2)[2]
        await search_image_and_reply(txt, m, lim)
    else:
        await m.reply(f"{em.gagal} **MINIMAL KASIH QUERY BWANG!!**")
    await pros.delete()
    return
