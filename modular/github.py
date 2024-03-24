################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

import requests

from Mix import *

__modles__ = "Github"
__help__ = """
 Github
• Perintah: `{0}github` username
• Penjelasan: Untuk melihat profil akun github seseorang.
"""


@ky.ubot("github", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    txt = c.get_text(m)
    if not txt:
        await pros.edit(f"{em.gagal} **Masukkan username github!!**")
        return
    url = f"https://api.github.com/users/{txt}"
    r = requests.get(url)
    if r.status_code != 404:
        b = r.json()
        avatar_url = b.get("avatar_url")
        html_url = b.get("html_url")
        gh_type = b.get("type")
        name = b.get("name")
        company = b.get("company")
        blog = b.get("blog")
        location = b.get("location")
        bio = b.get("bio")
        created_at = b.get("created_at")
        cap = f"{em.sukses} **Nama**: [{name}]({html_url})\n**Jenis**: {gh_type}\n**Perusahaan**: {company}\n**Blog**: {blog}\n**Lokasi**: {location}\n**Biografi**: {bio}\n**Profil Dibuat**: {created_at}"
        if avatar_url:
            await pros.delete()
            await c.send_photo(m.chat.id, avatar_url, caption=cap)
            return
        else:
            await pros.edit(cap)
            return
    else:
        await pros.edit(f"{em.gagal} **404 : Pengguna Tidak Ditemukan!!**")
        return
