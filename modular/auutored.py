################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################


from pyrogram.errors import *

from Mix import *

from .gcast import refresh_dialog

__modles__ = "AutoRead"
__help__ = get_cgr("help_autoread")


@ky.ubot("autoread", sudo=True)
async def _(_, m):
    em = Emojik()
    em.initialize()
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        await mek.edit(cgr("autoread_1").format(em.gagal))
        return
    biji, peler = m.command[:2]
    if peler.lower() == "gc":
        bcgc = await refresh_dialog("group")
        for gc in bcgc:
            try:
                await user.read_chat_history(gc, max_id=0)
            except ChannelPrivate:
                continue
            except ChannelInvalid:
                continue
        await mek.edit(cgr("autoread_2").format(em.sukses, len(bcgc)))
        return
    elif peler.lower() == "us":
        bcus = await refresh_dialog("users")
        for us in bcus:
            await user.read_chat_history(us, max_id=0)
        await mek.edit(cgr("autoread_3").format(em.sukses, len(bcus)))
        return
    elif peler.lower() == "bot":
        bcbot = await refresh_dialog("bot")
        for bt in bcbot:
            await user.read_chat_history(bt, max_id=0)
        await mek.edit(cgr("autoread_7").format(em.sukses, len(bcbot)))
        return
    elif peler.lower() == "ch":
        bcch = await refresh_dialog("ch")
        for ch in bcch:
            try:
                await user.read_chat_history(ch, max_id=0)
            except ChannelPrivate:
                continue
            except ChannelInvalid:
                continue
        await mek.edit(cgr("autoread_4").format(em.sukses, len(bcch)))
        return
    elif peler.lower() == "all":
        bcall = await refresh_dialog("allread")
        for aih in bcall:
            try:
                await user.read_chat_history(aih, max_id=0)
            except ChannelPrivate:
                continue
            except ChannelInvalid:
                continue
        await mek.edit(cgr("autoread_5").format(em.sukses, len(bcall)))
        return
    else:
        await mek.edit(cgr("autoread_6").format(em.gagal))
        return
