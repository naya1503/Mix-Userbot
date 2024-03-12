################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from pyrogram.errors import PeerIdInvalid
from pyrogram.raw.functions.messages import DeleteHistory

from Mix import *
from modular.gcast import refresh_dialog

__modles__ = "AutoEndChat"
__help__ = "AutoEndChat"


@ky.ubot("clearchat|endchat|clchat", sudo=True)
async def _(_, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2 and not rep:
        await m.reply("**Kasih argumen Goblok**")
    if len(m.command) == 1 and rep:
        who = rep.from_user.id
        try:
            info = await user.resolve_peer(who)
            await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
            pass
        await m.reply(f"{em.sukses} **Mampus lu jing {who}!! Gw EndChat!!**")
    else:
        if m.command[1].strip().lower() == "all":
            biji = await refresh_dialog("users")
            for kelot in biji:
                try:
                    info = await user.resolve_peer(kelot)
                    await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await m.reply(f"{em.sukses} **Mampus {len(biji)} pesan Gw EndChat!!**")
        elif m.command[1].strip().lower() == "bot":
            biji = await refresh_dialog("bot")
            for kelot in biji:
                try:
                    info = await user.resolve_peer(kelot)
                    await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await m.reply(f"{em.sukses} **Mampus {len(biji)} pesan Gw EndChat!!**")
        else:
            who = m.text.split(None, 1)[1]
            try:
                info = await user.resolve_peer(who)
                await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                pass
            await m.reply(f"{em.sukses} **Mampus lu jing {who}!! Gw EndChat!!**")
    await mek.delete()
    return
