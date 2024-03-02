################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
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


from pyrogram.errors import *

from Mix import *

from .gcast import refresh_dialog


@ky.ubot("autoread", sudo=True)
@bahasa()
async def _(c, m, cgr):
    em = Emojik()
    em.initialize()
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        await mek.edit(cgr("atored_1").format(em.gagal)
        return
    biji, peler = m.command[:2]
    if peler.lower() == "gc":
        bcgc = await refresh_dialog("group")
        for gc in bcgc:
            try:
                await user.read_chat_history(gc, max_id=0)
            except ChannelPrivate:
                continue
        await mek.edit(f"{em.sukses} Berhasil membaca {len(bcgc)} pesan group.")
        return
    elif peler.lower() == "us":
        bcus = await refresh_dialog("users")
        for us in bcus:
            await user.read_chat_history(us, max_id=0)
        await mek.edit(f"{em.sukses} Berhasil membaca {len(bcus)} pesan pengguna.")
        return
    elif peler.lower() == "ch":
        bcch = await refresh_dialog("ch")
        for ch in bcch:
            try:
                await user.read_chat_history(ch, max_id=0)
            except ChannelPrivate:
                continue
        await mek.edit(f"{em.sukses} Berhasil membaca {len(bcch)} pesan channel.")
        return
    elif peler.lower() == "all":
        bcall = await refresh_dialog("allread")
        for aih in bcall:
            try:
                await user.read_chat_history(aih, max_id=0)
            except ChannelPrivate:
                continue
        await mek.edit(
            f"{em.sukses} Berhasil membaca {len(bcall)} semua pesan diakun anda."
        )
        return
    else:
        await mek.edit(f"{em.gagal} Sepertinya anda memasukkan query yang salah!")
        return
