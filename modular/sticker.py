################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty || William || Gojo_Satoru
"""
################################################################

__modles__ = "Sticker"
__help__ = """
Help Command Sticker

• Perintah: <code>{0}gstik</code> [reply sticker]
• Penjelasan: Untuk mengambil sticker.
"""

import os

from Mix import *
from Mix.core.stick_tools import *


@ky.ubot("gstik|getstiker|getsticker", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    stick = rep.sticker
    if not rep:
        await m.reply(f"{em.gagal} Silahkan balas ke sticker!")
        return
    else:
        if stick.is_video == True:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.mp4")
            await m.reply_to_message.reply_document(
                document=pat,
                caption=f"<b>Emoji:</b> {stick.emoji}\n"
                f"<b>Sticker ID:</b> <code>{stick.file_id}</code>",
            )
        elif stick.is_animated == True:
            pat = await user.download_media(stick)
            file_name = f"{stick.set_name}.tgs"
            gif_, mp4_ = await con_tgs(pat, file_name)
            if gif_:
                await m.reply_animation(gif_)
            else:
                await m.reply_video(mp4_)
            # await m.reply_to_message.reply_document(
            # document=pat,
            # caption=f"<b>Emoji:</b> {sticker.emoji}\n"
            # f"<b>Sticker ID:</b> <code>{sticker.file_id}</code>")

        else:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.png")
            await m.reply_to_message.reply_document(
                document=pat,
                caption=f"<b>Emoji:</b> {stick.emoji}\n"
                f"<b>Sticker ID:</b> <code>{stick.file_id}</code>",
            )
        return
    os.remove(pat)
