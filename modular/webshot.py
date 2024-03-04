################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 @ CREDIT : NAN-DEV
"""
################################################################


from base64 import b64decode
from io import BytesIO

from Mix import *
from Mix.core.http import post

__modles__ = "Webshot"
__help__ = get_cgr("help_webss")


async def ss(url, full: bool = False):
    url = "https://" + url if not url.startswith("http") else url
    payload = {
        "url": url,
        "width": 1920,
        "height": 1080,
        "scale": 1,
        "format": "jpeg",
    }
    if full:
        payload["full"] = True
    data = await post(
        "https://webscreenshot.vercel.app/api",
        data=payload,
    )
    if "image" not in data:
        return None
    b = data["image"].replace("data:image/jpeg;base64,", "")
    file = BytesIO(b64decode(b))
    file.name = "webss.jpg"
    return file


@ky.ubot("webss|webshot|ss", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.command) < 2:
        await m.reply(f"{em.gagal} Silahkan berikan link tautan!")
        return
    if len(m.command) == 2:
        url = m.text.split(None, 1)[1]
        full = False
    elif len(m.command) == 3:
        url = m.text.split(None, 2)[1]
        full = m.text.split(None, 2)[2].lower().strip() in [
            "yes",
            "y",
            "1",
            "true",
        ]
    else:
        await m.reply(f"{em.gagal} Berikan link yang valid!")
        return

    tit = await m.reply(f"{em.proses} Processing...")

    try:
        photo = await ss(url, full)
        if not photo:
            await tit.edit(f"{em.gagal} Gagal mendapatkan gambar!")
            return
        await tit.delete()

        tot = await m.reply(f"{em.proses} Uploading...")

        if not full:
            await m.reply_photo(photo)
        else:
            await m.reply_document(photo)
        await tot.delete()
        return
    except Exception as r:
        await m.reply(f"{em.gagal} Error : `{r}`\n\nLaporke @KynanSupport!")
        return
