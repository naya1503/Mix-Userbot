################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import os

from Mix import *

__modles__ = "Carbon"
__help__ = get_cgr("help_carbon")


async def buat_bon(code, language, theme):
    meki = SafoneAPI()
    bg = {
        "backgroundColor": "navy",
        "fontFamily": "Roboto",
        "fontSize": "14px",
        "language": language,
        "theme": theme,
    }
    img = await meki.carbon(code, **bg)
    with open("carbon.png", "wb") as file:
        file.write(img.getvalue())
    return "carbon.png"


@ky.ubot("carbon|carbonara", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    text = m.reply_to_message.text or m.reply_to_message.caption
    if not text:
        return await m.reply(cgr("crbn_1").format(em.gagal))
    ex = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) == 1 and text:
        meg = await buat_bon(text, "python", "light")
        await m.reply_photo(
            meg, caption=cgr("crbn_2").format(em.sukses, user.me.mention)
        )
        os.remove(meg)
    elif len(m.command) == 2:
        lague = m.text.split(None, 1)[1]
        meg = await buat_bon(text, lague, "light")
        await m.reply_photo(
            meg, caption=cgr("crbn_2").format(em.sukses, user.me.mention)
        )
        os.remove(meg)
    elif len(m.command) == 3:
        lague = m.text.split(None, 2)[1]
        tem = m.text.split(None, 2)[2]
        meg = await buat_bon(text, lague, tem)
        await m.reply_photo(
            meg, caption=cgr("crbn_2").format(em.sukses, user.me.mention)
        )
        os.remove(meg)
    else:
        await m.reply(cgr("crbn_1").format(em.gagal))
    await ex.delete()
    return
