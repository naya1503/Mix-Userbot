################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from pyrogram.enums import ChatType
from pyrogram.errors import *
from team.nandev.class_log import LOGGER

async def akunbebanamat(c):
    chats = []
    async for bb in c.get_dialogs():
        if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]:
            chats.append(bb.chat.id)
    return chats
    

async def dasar_laknat(c):
    jml = await akunbebanamat(c)
    for jamet in jml:
        try:
            await c.read_chat_history(jamet, max_id=0)
        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
            continue
    LOGGER.info("Finished Read Message...")
        