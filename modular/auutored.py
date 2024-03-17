################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################


from pyrogram.errors import *

from Mix import *

__modles__ = "AutoRead"
__help__ = get_cgr("help_autoread")


@ky.ubot("autoread", sudo=True)
@ky.devs("otored")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 3:
        await mek.edit(cgr("autoread_1").format(em.gagal))
        return
    biji, peler, jembut = m.command[:3]
    if peler.lower() == "gc":
        if jembut.lower() == "on":
            udB.set_var(c.me.id, "read_gc", True)
            await mek.edit(cgr("autoread_2").format(em.sukses))
            return
        else:
            udB.remove_var(c.me.id, "read_gc")
            await mek.edit(cgr("autoread_8").format(em.sukses, peler))
            return
    elif peler.lower() == "us":
        if jembut.lower() == "on":
            udB.set_var(c.me.id, "read_us", True)
            await mek.edit(cgr("autoread_3").format(em.sukses))
            return
        else:
            udB.remove_var(c.me.id, "read_us")
            await mek.edit(cgr("autoread_8").format(em.sukses, peler))
            return
    elif peler.lower() == "bot":
        if jembut.lower() == "on":
            udB.set_var(c.me.id, "read_bot", True)
            await mek.edit(cgr("autoread_7").format(em.sukses))
            return
        else:
            udB.remove_var(c.me.id, "read_bot")
            await mek.edit(cgr("autoread_8").format(em.sukses, peler))
            return
    elif peler.lower() == "ch":
        if jembut.lower() == "on":
            udB.set_var(c.me.id, "read_ch", True)
            await mek.edit(cgr("autoread_4").format(em.sukses))
            return
        else:
            udB.remove_var(c.me.id, "read_ch")
            await mek.edit(cgr("autoread_8").format(em.sukses, peler))
            return

    elif peler.lower() == "tag":
        if jembut.lower() == "on":
            udB.set_var(c.me.id, "read_mention", True)
            await mek.edit(cgr("autoread_9").format(em.sukses))
            return
        else:
            udB.remove_var(c.me.id, "read_mention")
            await mek.edit(cgr("autoread_8").format(em.sukses, peler))
            return

    elif peler.lower() == "all":
        if jembut.lower() == "on":
            udB.set_var(c.me.id, "read_all", True)
            await mek.edit(cgr("autoread_5").format(em.sukses))
            return
        else:
            udB.remove_var(c.me.id, "read_all")
            await mek.edit(cgr("autoread_8").format(em.sukses, peler))
            return
    else:
        await mek.edit(cgr("autoread_6").format(em.gagal))
        return
