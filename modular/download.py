################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import aiohttp
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Download"
__help__ = "Download"


@ky.ubot("sosmed", sudo=True)
async def _(c, m):
    if len(m.command) < 2:
        await m.reply_text(
            "Gunakan perintah `/sosmed [URL_MEDIA]` untuk mengunduh media dari sosial media."
        )
        return

    url = m.command[1]

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    filename = url.split("/")[-1]
                    with open(filename, "wb") as f:
                        f.write(await resp.read())

                    # await c.send_message(
                    #     chat_id=m.chat.id,
                    #     text="Media berhasil diunduh!",
                    #     reply_to_message_id=m.message_id,
                    # )

                    await c.send_document(
                        chat_id=m.chat.id,
                        document=filename,
                        caption="Berikut adalah media yang Anda unduh dari sosial media.",
                    )

                else:
                    await m.reply_text(
                        f"Gagal mengunduh media dengan status {resp.status}"
                    )

    except Exception as e:
        await m.reply_text(f"Terjadi kesalahan: {str(e)}")
