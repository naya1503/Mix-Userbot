################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from Mix import *
from Mix.core.tools_media import *

__modles__ = "Memify"
__help__ = """
 Memify
• Perintah: `{0}mmf` text [balas stiker]
• Penjelasan: Untuk menambahkan teks ke stiker.

• Optional:
`{0}mmf teks atas; teks bawah`
"""


@ky.ubot("mmf|memify")
async def memify(c: nlx, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message_id:
        await m.reply(f"{em.gagal} **Balas ke pesan foto atau sticker!**")
        return
    rep = m.reply_to_message
    if not rep.media:
        await m.reply(f"{em.gagal} **Harap Balas ke foto atau sticker!**")
        return
    doc = await c.download_media(rep)
    pros = await m.reply(cgr("proses").format(em.proses))
    txt = c.get_m(m)
    if not txt:
        return await pros.edit(f"{em.gagal} **Harap Ketik `{m.command} text`**")
    meme = await add_text_img(doc, txt)
    await asyncio.gather(
        pros.delete(),
        c.send_sticker(
            m.chat.id,
            sticker=meme,
            reply_to_message_id=ReplyCheck(m),
        ),
    )
    os.remove(meme)
