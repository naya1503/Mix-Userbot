################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 @ CREDIT : NAN-DEV
"""
################################################################

import re

import aiofiles
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

__modles__ = "Pastebin"
__help__ = """
 Help Command Pastebin

• Perintah : <code>{0}paste</code> [balas pesan]
• Penjelasan : Untuk mengupload teks ke pastebin.
"""


@ky.ubot("paste", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(f"{em.gagal} Silahkan balas ke pesan.")
    r = m.reply_to_message
    if not r.text and not r.document:
        return await m.reply_text(
            f"{em.gagal} Silahkan balas ke pesan teks atau dokumen teks?"
        )
    if r.text:
        content = str(r.text)
    else:
        if r.document.file_size > 40000:
            return await m.reply(f"{em.gagal} Ukuran file harus dibawah 40kb")
        doc = await m.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    try:
        await m.reply_photo(
            photo=link, caption=f"{em.sukses} **Paste Link:** [Klik Disini]({link})"
        )
    except Exception:
        await m.reply(f"{em.sukses} **Paste Link:** [Klik Disini]({link})")
