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

from .webshot import ss

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

__modles__ = "Pastebin"
__help__ = get_cgr("help_paste")


@ky.ubot("paste", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(cgr("paste_1").format(em.gagal))
    r = m.reply_to_message
    if not r.text and not r.document:
        return await m.reply_text(cgr("paste_1").format(em.gagal))
    if r.text:
        content = str(r.text)
    else:
        if r.document.file_size > 40000:
            return await m.reply(cgr("paste_2").format(em.gagal))
        doc = await m.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    photo = await ss(link, True)
    try:
        await m.reply_document(photo, caption=cgr("paste_3").format(em.sukses, link))
    except Exception:
        await m.reply(cgr("paste_3").format(em.sukses, link))
        return
