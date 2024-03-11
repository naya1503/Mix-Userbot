################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import aiohttp
import mimetypes
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
                    content_type = resp.headers.get("content-type", "").split(";")[0]

                    ext = mimetypes.guess_extension(content_type.split("/")[1])

                    filename = f"media{ext}"
                    with open(filename, "wb") as f:
                        f.write(await resp.read())

                    if content_type.startswith("image"):
                        await c.send_photo(
                            chat_id=m.chat.id,
                            photo=filename,
                            caption="Berikut adalah foto yang Anda unduh dari sosial media.",
                        )
                    elif content_type.startswith("video"):
                        await c.send_video(
                            chat_id=m.chat.id,
                            video=filename,
                            caption="Berikut adalah video yang Anda unduh dari sosial media.",
                        )
                    elif content_type.startswith("audio"):
                        await c.send_audio(
                            chat_id=m.chat.id,
                            audio=filename,
                            caption="Berikut adalah audio yang Anda unduh dari sosial media.",
                        )
                    else:
                        await m.reply_text("Media yang diunduh tidak didukung.")

                else:
                    await m.reply_text(
                        f"Gagal mengunduh media dengan status {resp.status}"
                    )

    except Exception as e:
        await m.reply_text(f"Terjadi kesalahan: {str(e)}")