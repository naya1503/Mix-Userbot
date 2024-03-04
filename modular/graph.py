################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from telegraph import Telegraph, exceptions, upload_file

from Mix import *

__modles__ = "Telegraph"
__help__ = get_cgr("help_graph")


@ky.ubot("tg", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} Processing...")
    if not m.reply_to_message:
        return await xx.edit(f"{em.gagal} Silakan balas ke pesan teks atau media!")
    telegraph = Telegraph()
    if m.reply_to_message.media:
        m_d = await c.dl_pic(m.reply_to_message)
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as r:
            return await xx.edit(
                f"{em.gagal} <code>{r}</code>\n\nLapor ke @KynanSupport!"
            )
        dnbg = f"{em.sukses} <b>Diupload ke : </b> <a href='https://telegra.ph/{media_url[0]}'>Klik Disini</a>"
        await xx.edit(dnbg)
    elif m.reply_to_message.text:
        page_title = f"{c.me.first_name} {c.me.last_name or ''}"
        page_text = m.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as r:
            return await xx.edit(
                f"{em.gagal} <code>{r}</code>\n\nLapor ke @KynanSupport!"
            )
        ybg = f"{em.sukses} <b>Diupload ke :</b> <a href='https://telegra.ph/{response['path']}'>Klik Disini</a>"
        await xx.edit(ybg)
