################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
"""
################################################################


__modles__ = "AutoRead"
__help__ = """
 Help Command AutoRead

• Perintah : <code>{0}autoread</code> [query]
• Penjelasan : Untuk membaca semua pesan diakun anda.

**Notes Optional:**
- `gc` untuk membaca semua pesan grup diakun anda.
- `ch` untuk membaca semua pesan channel diakun anda.
- `us` untuk membaca semua pesan pengguna diakun anda.
- `all` untuk membaca semua pesan gc, ch, us diakun anda.
"""

import asyncio

from pyrogram.errors import FloodWait

from Mix import *


@ky.ubot("autoread", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    mek = await m.reply(f"{em.proses} Processing...")
    if len(m.command) < 2:
        await mek.edit(
            f"{em.gagal} Gunakan Format : <code>autoread</code> [gc or us or ch or all]."
        )
        return
    bcgc = await c.get_user_dialog("group")
    bcus = await c.get_user_dialog("users")
    bcch = await c.get_user_dialog("ch")
    bcall = await c.get_user_dialog("allread")
    biji, peler = m.command[:2]
    if peler.lower() == "gc":
        for gc in bcgc:
            try:
                await c.read_chat_history(gc, max_id=0)
            except FloodWait as e:
                await mek.edit(f"{em.proses} Mohon tunggu {int(e.value)}...")
                await asyncio.sleep(int(e.value))
                await c.read_chat_history(gc, max_id=0)
            await mek.edit(f"{em.sukses} Berhasil membaca {len(bcgc)} pesan group.")
            return
    elif peler.lower() == "us":
        for us in bcus:
            try:
                await c.read_chat_history(us, max_id=0)
            except FloodWait as e:
                await mek.edit(f"{em.proses} Mohon tunggu {int(e.value)}...")
                await asyncio.sleep(int(e.value))
                await c.read_chat_history(us, max_id=0)
            await mek.edit(f"{em.sukses} Berhasil membaca {len(bcus)} pesan pengguna.")
            return
    elif peler.lower() == "ch":
        for ch in bcch:
            try:
                await c.read_chat_history(ch, max_id=0)
            except FloodWait as e:
                await mek.edit(f"{em.proses} Mohon tunggu {int(e.value)}...")
                await asyncio.sleep(int(e.value))
                await c.read_chat_history(ch, max_id=0)
            await mek.edit(f"{em.sukses} Berhasil membaca {len(bcch)} pesan channel.")
            return
    elif peler.lower() == "all":
        for aih in bcall:
            try:
                await c.read_chat_history(aih, max_id=0)
            except FloodWait as e:
                await mek.edit(f"{em.proses} Mohon tunggu {int(e.value)}...")
                await asyncio.sleep(int(e.value))
                await c.read_chat_history(aih, max_id=0)
            await mek.edit(
                f"{em.sukses} Berhasil membaca {len(bcall)} semua pesan diakun anda."
            )
            return
    else:
        await mek.edit(f"{em.gagal} Sepertinya anda memasukkan query yang salah!")
        return
