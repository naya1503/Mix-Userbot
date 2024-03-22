################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################
import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import *
from pyrogram.raw.functions.messages import ReadMentions
from team.nandev.class_log import LOGGER
from team.nandev.database import udB

from Mix import nlx


async def dasar_laknat(client):
    LOGGER.info("Check whether this account is a burden or not...")
    async for bb in client.get_dialogs(limit=500):
        if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            try:
                await client.read_chat_history(bb.chat.id, max_id=0)
            except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                continue
            except FloodWait as e:
                await asyncio.sleep(e.value)
                try:
                    await client.read_chat_history(bb.chat.id, max_id=0)
                except:
                    continue
    LOGGER.info("Finished Read Message..")
    # sys.exit(1)


async def autor_gc():
    if not udB.get_var(nlx.me.id, "read_gc"):
        return
    while not await asyncio.sleep(3600):
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


async def autor_mention():
    if not udB.get_var(nlx.me.id, "read_mention"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For Mention...")
        async for bb in nlx.get_dialogs(limit=500):
            if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                try:
                    await nlx.invoke(
                        ReadMentions(peer=await nlx.resolve_peer(bb.chat.id))
                    )
                except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    try:
                        await nlx.invoke(
                            ReadMentions(peer=await nlx.resolve_peer(bb.chat.id))
                        )
                    except:
                        continue
        LOGGER.info("Finished Read Mention...")


async def autor_ch():
    if not udB.get_var(nlx.me.id, "read_ch"):
        return
    while not await asyncio.sleep(3600):
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
    if not udB.get_var(nlx.me.id, "read_us"):
        return
    while not await asyncio.sleep(3600):
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
    if not udB.get_var(nlx.me.id, "read_bot"):
        return
    while not await asyncio.sleep(3600):
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
    if not udB.get_var(nlx.me.id, "read_all"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For All...")
        async for bb in nlx.get_dialogs(limit=500):
            if bb.chat.type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
                ChatType.PRIVATE,
                ChatType.BOT,
            ]:
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


# asyncio.get_event_loop().run_until_complete(dasar_laknat())
