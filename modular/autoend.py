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


@ky.ubot("autoread", sudo=True)
async def _(_, m):
    em = Emojik()
    em.initialize()
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        await m.reply("**Kasih argumen Goblok**")
    tag = m.command[1].strip()
    if tag.startswith("@"):
        user_id = tag[1:]
        try:
            org = await c.get_users(user_id)
        except Exception as e:
            await m.reply(cgr("err").format(em.gagal, e))
        info = await user.resolve_peer(org)
        await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        await m.reply(f"{em.sukses} **Mampus lu jing {org.mention}!! Gw EndChat!!")
    elif tag.isnumeric():
        if int(tag):
            user_id = tag[1:]
            try:
                org = await c.get_users(user_id)
            except Exception as e:
                await m.reply(cgr("err").format(em.gagal, e))
            info = await user.resolve_peer(org)
            await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            await m.reply(f"{em.sukses} **Mampus lu jing {org.mention}!! Gw EndChat!!")
    elif tag == "all":
        biji = await refresh_dialog("users")
        for kelot in biji:
            try:
                info = await user.resolve_peer(kelot)
                await user.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                continue
        await m.reply(f"{em.sukses} **Mampus {len(biji)} pesan Gw EndChat!!")
    else:
        await m.reply("**Kasih argumen Goblok**")
    await mek.delete()
    return
