################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from pyrogram.enums import ChatType
from team.nandev.class_log import LOGGER


async def akunbebanamat(c):
    chats = []
    async for bb in c.get_dialogs():
        if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]:
            chats.append(bb.chat.id)
    return chats


async def dasar_laknat(c):
    LOGGER.info("Check whether this account is a burden or not...")
    jml = await akunbebanamat(c)
    for jamet in jml:
        try:
            await c.read_chat_history(jamet, max_id=0)
        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
            continue
        except FloodWait as e:
            await asyncio.slee(e.value)
            try:
                await c.read_chat_history(jamet, max_id=0)
            except:
                continue
    LOGGER.info("Finished Read Message...")
    
    
"""
async def dasar_laknat(c):
    async for bc in c.get_dialogs(limit=500):
        if bc.chat.type == ChatType.SUPERGROUP:
            LOGGER.info(f"Reading messages {bc.chat.title}")
            # lastm = (await c.get_history(bc.chat.id, limit=1))[0].message_id
            await c.read_chat_history(bc.chat.id, max_id=0)
"""