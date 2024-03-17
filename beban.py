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

"""
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
    async with c:
        for bc in await c.get_dialogs():
            if bc.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]:
                LOGGER.info(f"Reading messages {bb.chat.title}")
                lastm = (await c.get_history(bb.chat.id, limit=1))[0].message_id
                await c.read_history(bb.chat.id, lastm)
