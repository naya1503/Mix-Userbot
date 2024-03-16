################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################


from pyrogram.enums import ChatType
from pyrogram.errors import *

from Mix import *

__modles__ = "AutoRead"
__help__ = get_cgr("help_autoread")


async def diread_dong(q):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
        "bot": [ChatType.BOT],
        "ch": [ChatType.CHANNEL],
        "allread": [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
            ChatType.PRIVATE,
            ChatType.BOT,
        ],
    }
    async for dialog in nlx.get_dialogs():
        if dialog.chat.type in chat_types[q]:
            chats.append(dialog.chat.id)

    return chats


@ky.ubot("autoread", sudo=True)
@ky.devs("otored")
async def _(_, m):
    em = Emojik()
    em.initialize()
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        await mek.edit(cgr("autoread_1").format(em.gagal))
        return
    biji, peler = m.command[:2]
    if peler.lower() == "gc":
        bcgc = await diread_dong("group")
        for gc in bcgc:
            try:
                await nlx.read_chat_history(gc, max_id=0)
            except (
                ChannelPrivate,
                PeerIdInvalid,
                UserBannedInChannel,
                UsernameInvalid,
            ):
                continue
        await mek.edit(cgr("autoread_2").format(em.sukses, len(bcgc)))
        return
    elif peler.lower() == "us":
        bcus = await diread_dong("users")
        for us in bcus:
            try:
                await nlx.read_chat_history(us, max_id=0)
            except (
                ChannelPrivate,
                PeerIdInvalid,
                UserBannedInChannel,
                UsernameInvalid,
            ):
                continue
        await mek.edit(cgr("autoread_3").format(em.sukses, len(bcus)))
        return
    elif peler.lower() == "bot":
        bcbot = await diread_dong("bot")
        for bt in bcbot:
            try:
                await nlx.read_chat_history(bt, max_id=0)
            except (
                ChannelPrivate,
                PeerIdInvalid,
                UserBannedInChannel,
                UsernameInvalid,
            ):
                continue
        await mek.edit(cgr("autoread_7").format(em.sukses, len(bcbot)))
        return
    elif peler.lower() == "ch":
        bcch = await diread_dong("ch")
        for ch in bcch:
            try:
                await nlx.read_chat_history(ch, max_id=0)
            except (
                ChannelPrivate,
                PeerIdInvalid,
                UserBannedInChannel,
                UsernameInvalid,
            ):
                continue
        await mek.edit(cgr("autoread_4").format(em.sukses, len(bcch)))
        return
    elif peler.lower() == "all":
        bcall = await diread_dong("allread")
        for aih in bcall:
            try:
                await nlx.read_chat_history(aih, max_id=0)
            except (
                ChannelPrivate,
                PeerIdInvalid,
                UserBannedInChannel,
                UsernameInvalid,
            ):
                continue
        await mek.edit(cgr("autoread_5").format(em.sukses, len(bcall)))
        return
    else:
        await mek.edit(cgr("autoread_6").format(em.gagal))
        return
