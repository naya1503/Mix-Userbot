################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio
from io import BytesIO
from Mix import *

__modles__ = "Carbon"
__help__ = """
 Help Command Carbon

• Perintah: <code>{0} carbon</code
• Penjelasan: Untuk membuat teks carbonara.
"""

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@ky.ubot("carbon|carbonara", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    text = (
        m.text.split(None, 1)[1]
        if len(
            m.command,
        )
        != 1
        else None
    )
    if m.reply_to_message:
        text = m.reply_to_message.text or m.reply_to_message.caption
    if not text:
        return await m.reply(f"{em.gagal} Teks tidak boleh kosong!")
    ex = await m.reply(f"{em.proses} Processing...")
    carbon = await make_carbon(text)
    await ex.edit(f"{em.proses} Uploading...")
    await asyncio.gather(
        ex.delete(),
        c.send_photo(
            m.chat.id,
            carbon,
            caption=f"**{em.sukses} Carbonara by {user.me.mention}**"
        ),
    )
    carbon.close()
