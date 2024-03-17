################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from pyrogram.enums import ChatType


async def akunbebanamat(c, q):
    chats = []
    chat_types = {
        "beban": [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL],
    }
    async for bb in c.get_dialogs():
        if bb.chat.type in chat_types[q]:
            chats.append(bb.chat.id)
    return chats
