################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 @ CREDIT : NAN-DEV
"""
################################################################

__modles__ = "Webshot"
__help__ = """
 Help Command Webshot

• Perintah : <code>{0}webss or ss</code>
• Penjelasan : Untuk mengambil tangkapan layar link.
"""

from Mix import *


@ky.ubot("webss|webshot|ss", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    # if len(m.command) == 1:
    # await m.reply(f"{em.gagal} Silahkan berikan link atau belas pesan tautan!")
    # return

    if len(m.command) > 1:
        lonk = m.text.split(None, 1)[1]
    else:
        lonk = c.get_arg(m)
        try:
            linkk = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{lonk}"
            await m.reply(photo=linkk)
        except Exception as r:
            await m.reply(f"{em.gagal} Error : `{r}`\n\nLaporke @KynanSupport!")
            return
