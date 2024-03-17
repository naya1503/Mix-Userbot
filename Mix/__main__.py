import asyncio
from os import execvp
from sys import executable

from pyrogram import *
from pyrogram.errors import *
from uvloop import install
from Mix.mix_client import check_logger, getFinish
from Mix import *

lool = asyncio.get_event_loop()


async def start_user():
    LOGGER.info(f"Starting Telegram User Client...")
    try:
        await nlx.start()
    except (SessionExpired, ApiIdInvalid, UserDeactivatedBan):
        LOGGER.info("Check your session or api id!!")
        sys.exit(1)


async def start_bot():
    LOGGER.info(f"Starting Telegram Bot Client...")
    if TOKEN_BOT is None:
        await autobot()
    try:
        await bot.start()
    except (AccessTokenExpired, SessionRevoked, AccessTokenInvalid):
        LOGGER.info("Token Expired.")
        ndB.del_key("BOT_TOKEN")
        execvp(executable, [executable, "-m", "Mix"])


async def starter():
    LOGGER.info(f"Check Updater...")
    await cek_updater()
    LOGGER.info(f"Updater Finished...")
    LOGGER.info(f"Connecting to {ndB.name}...")
    if ndB.ping():
        LOGGER.info(f"Connected to {ndB.name} Successfully!")
    await start_user()
    if nlx.is_connected:
        await start_bot()
    if TAG_LOG is None:
        await check_logger()
    LOGGER.info("Successfully Started Userbot.")
    await asyncio.gather(refresh_cache(), getFinish(), auto_clean(), isFinish(), idle())


if __name__ == "__main__":
    install()
    # loop = asyncio.get_event_loop_policy()
    # event_loop = loop.get_event_loop()
    # asyncio.set_event_loop(event_loop)
    # event_loop.run_until_complete(starter())
    lool.run_until_complete(starter())
