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
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        await m.reply("**Kasih argumen Goblok**")
    tag = m.command[1].strip()
    puki = await user.extract_user(m)
    try:
        who = (await user.get_users(puki)).id
    except Exception:
        try:
            who = int(m.command[1])
        except Exception as err:
            return await m.reply(cgr("err").format(em.gagal, err))
    if tag.startswith("@") or tag.isnumeric():
        try:
            info = await user.resolve_peer(who)
            await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
                pass
        await m.reply(f"{em.sukses} **Mampus lu jing {who.mention}!! Gw EndChat!!**")
    elif tag == "all":
        biji = await refresh_dialog("users")
        for kelot in biji:
            try:
                info = await user.resolve_peer(kelot)
                await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                continue
        await m.reply(f"{em.sukses} **Mampus {len(biji)} pesan Gw EndChat!!**")
    else:
        await m.reply("**Kasih argumen Goblok**")
    await mek.delete()
    return
