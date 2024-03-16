################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from hydrogram.errors import PeerIdInvalid
from hydrogram.raw.functions.messages import DeleteHistory

from Mix import *
from modular.gcast import refresh_dialog

__modles__ = "AutoEndChat"
__help__ = get_cgr("help_auend")


@ky.ubot("clearchat|endchat|clchat", sudo=True)
async def _(_, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2 and not rep:
        await m.reply(cgr("auend_1").format(em.gagal))
        return
    if len(m.command) == 1 and rep:
        who = rep.from_nlx.id
        try:
            info = await nlx.resolve_peer(who)
            await nlx.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
            pass
        await m.reply(cgr("auend_2").format(em.sukses, who))
    else:
        if m.command[1].strip().lower() == "all":
            biji = await refresh_dialog("nlxs")
            for kelot in biji:
                try:
                    info = await nlx.resolve_peer(kelot)
                    await nlx.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await m.reply(cgr("auend_3").format(em.sukses, len(biji)))
        elif m.command[1].strip().lower() == "bot":
            bijo = await refresh_dialog("bot")
            for kelot in bijo:
                try:
                    info = await nlx.resolve_peer(kelot)
                    await nlx.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await m.reply(cgr("auend_4").format(em.sukses, len(bijo)))
        else:
            who = m.text.split(None, 1)[1]
            try:
                info = await nlx.resolve_peer(who)
                await nlx.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                pass
            await m.reply(cgr("auend_2").format(em.sukses, who))
    await mek.delete()
    return
