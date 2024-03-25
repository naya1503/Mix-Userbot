import json

import requests

from Mix import *

__modles__ = "Adzan"
__help__ = """
 Adzan
• Perintah: `{0}adzan` [nama kota]
• Penjelasan: Untuk mengetahui waktu adzan.
"""


@ky.ubot("adzan", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    lok = c.get_text(m)
    pros = await m.reply(cgr("proses").format(em.proses))
    if not lok:
        await pros.edit(f"{em.gagal} **Silahkan Masukkan Nama Kota Anda!!**")
        return
    url = f"http://muslimsalat.com/{lok}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    req = requests.get(url)
    if req.status_code != 200:
        await pros.edit(f"{em.gagal} **Maaf tidak menemukan Kota `{lok}`")
        return
    result = json.loads(req.text)
    txt = f"""
**Jadwal Shalat Wilayah <u>{lok}</u>
Tanggal `{result['items'][0]['date_for']}`
Kota `{result['query']} | {result['country']}`

Terbit : `{result['items'][0]['shurooq']}`
Subuh : `{result['items'][0]['fajr']}`
Zuhur :`{result['items'][0]['dhuhr']}`
Ashar : `{result['items'][0]['asr']}`
Maghrib : `{result['items'][0]['maghrib']}`
Isya : `{result['items'][0]['isha']}`**
"""
    await m.reply(txt)
    await pros.delete()
    return
