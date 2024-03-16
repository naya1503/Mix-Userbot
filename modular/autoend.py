################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from hydrogram.errors import *
from hydrogram.raw.functions.messages import DeleteHistory
from hydrogram.enums import ChatType
from Mix import *

__modles__ = "AutoEndChat"
__help__ = get_cgr("help_auend")

async def diend_chat(q):
    chats = []
    chat_types = {
        "bot": [ChatType.BOT],
        "all": [ChatType.PRIVATE, ChatType.BOT],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in nlx.get_dialogs():
        if dialog.chat.type in chat_types[q]
            chats.append(dialog.chat.id)

    return chats

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
        who = rep.from_user.id
        try:
            info = await nlx.resolve_peer(who)
            await nlx.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
            pass
        await m.reply(cgr("auend_2").format(em.sukses, who))
    else:
        if m.command[1].strip().lower() == "all":
            biji = await refresh_dialog("users")
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
