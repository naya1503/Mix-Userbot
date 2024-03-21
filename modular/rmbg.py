################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

import os

from SafoneAPI import SafoneAPI
from telegraph import upload_file

from Mix import *

__modles__ = "RemoveBg"
__help__ = """
 Removal Background
• Perintah: `{0}rmbg` [balas ke foto]
• Penjelasan: Untuk menghapus latar belakang foto tersebut.
"""


async def rem_bg(image_data):
    meki = SafoneAPI()
    img = await meki.removebg(image_data)
    with open("rmbg.png", "wb") as file:
        file.write(img.getvalue())
    return "rmbg.png"


@ky.ubot("rmbg", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    pros = await m.reply(cgr("proses").format(em.proses))
    if rep.photo:
        kk = await rep.download()
        media_url = upload_file(kk)
        mmk = f"https://telegra.ph/{media_url[0]}"
        hasil = await rem_bg(mmk)
        if hasil:
            await m.reply_document(hasil, reply_to_message_id=ReplyCheck(m))
            os.remove(hasil)
        else:
            await m.reply_text(
                "Maaf, terjadi kesalahan dalam menghapus latar belakang gambar.",
                reply_to_message_id=ReplyCheck(m),
            )
    else:
        await m.reply_text("Mohon balas ke gambar.", reply_to_message_id=ReplyCheck(m))
    await pros.delete()
    return
