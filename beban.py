################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from pyrogram.enums import ChatType
from team.nandev.class_log import LOGGER
from Mix import nlx
from team.nandev.database import udB


async def dasar_laknat(c):
    LOGGER.info("Check whether this account is a burden or not...")
    async for bb in c.get_dialogs(limit=500):
        if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            try:
                await c.read_chat_history(bb.chat.id, max_id=0)
            except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                continue
            except FloodWait as e:
                await asyncio.sleep(e.value)
                try:
                    await c.read_chat_history(bb.chat.id, max_id=0)
                except:
                    continue
    LOGGER.info("Finished Read Message...")
    

async def autor_gc():
    if udB.get_var(nlx.me.id, "read_gc") is None:
        return
    while not await asyncio.sleep(300):
        LOGGER.info("Running Autoread For Group...")
        async for bb in nlx.get_dialogs(limit=500):
            if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                try:
                    await nlx.read_chat_history(bb.chat.id, max_id=0)
                except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    try:
                        await nlx.read_chat_history(bb.chat.id, max_id=0)
                    except:
                        continue
        LOGGER.info("Finished Read Message...")
        

async def autor_ch():
    if udB.get_var(nlx.me.id, "read_ch") is None:
        return
    while not await asyncio.sleep(300):
        LOGGER.info("Running Autoread For Channel...")
        async for bb in nlx.get_dialogs(limit=500):
            if bb.chat.type == ChatType.CHANNEL:
                try:
                    await nlx.read_chat_history(bb.chat.id, max_id=0)
                except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    try:
                        await nlx.read_chat_history(bb.chat.id, max_id=0)
                    except:
                        continue
        LOGGER.info("Finished Read Message...")
        

async def autor_us():
    if udB.get_var(nlx.me.id, "read_us") is None:
        return
    while not await asyncio.sleep(300):
        LOGGER.info("Running Autoread For Users...")
        async for bb in nlx.get_dialogs(limit=500):
            if bb.chat.type == ChatType.PRIVATE:
                try:
                    await nlx.read_chat_history(bb.chat.id, max_id=0)
                except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    try:
                        await nlx.read_chat_history(bb.chat.id, max_id=0)
                    except:
                        continue
        LOGGER.info("Finished Read Message...")
        
        
async def autor_bot():
    if udB.get_var(nlx.me.id, "read_bot") is None:
        return
    while not await asyncio.sleep(300):
        LOGGER.info("Running Autoread For Users...")
        async for bb in nlx.get_dialogs(limit=500):
            if bb.chat.type == ChatType.BOT:
                try:
                    await nlx.read_chat_history(bb.chat.id, max_id=0)
                except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    try:
                        await nlx.read_chat_history(bb.chat.id, max_id=0)
                    except:
                        continue
        LOGGER.info("Finished Read Message...")
        
        
async def autor_all():
    if udB.get_var(nlx.me.id, "read_all") is None:
        return
    while not await asyncio.sleep(300):
        LOGGER.info("Running Autoread For All...")
        async for bb in nlx.get_dialogs(limit=500):
            if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL, ChatType.PRIVATE, ChatType.BOT]:
                try:
                    await nlx.read_chat_history(bb.chat.id, max_id=0)
                except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    try:
                        await nlx.read_chat_history(bb.chat.id, max_id=0)
                    except:
                        continue
        LOGGER.info("Finished Read Message...")