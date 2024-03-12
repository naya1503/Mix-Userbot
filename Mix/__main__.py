import asyncio
import importlib
import sys

from pyrogram import *
from pyrogram.errors import *
import uvloop
from assistant import BOT_PLUGINS
from Mix import *
from modular import USER_MOD


async def start_user():
    LOGGER.info(f"Starting Telegram User Client...")
    try:
        await user.start()
        LOGGER.info(f"Importing All Modules...")
        for modul in USER_MOD:
            imported_module = importlib.import_module(f"modular." + modul)
            if hasattr(imported_module, "__modles__") and imported_module.__modles__:
                imported_module.__modles__ = imported_module.__modles__
                if hasattr(imported_module, "__help__") and imported_module.__help__:
                    CMD_HELP[imported_module.__modles__.replace(" ", "_").lower()] = (
                        imported_module
                    )
    except (SessionExpired, ApiIdInvalid, UserDeactivatedBan):
        LOGGER.info("Check your session or api id!!")
        sys.exit(1)


async def start_bot():
    LOGGER.info(f"Starting Telegram Bot Client...")
    if bot_token is None:
        await autobot()
    try:
        await bot.start()
        for plus in BOT_PLUGINS:
            imported_module = importlib.import_module("assistant." + plus)
            importlib.reload(imported_module)
    except (AccessTokenExpired, SessionRevoked, AccessTokenInvalid):
        LOGGER.info("Token Expired.")
        sys.exit(1)


async def starter():
    LOGGER.info(f"Check Updater...")
    await cek_updater()
    LOGGER.info(f"Updater Finished...")
    LOGGER.info(f"Connecting to {ndB.name}...")
    if ndB.ping():
        LOGGER.info(f"Connected to {ndB.name} Successfully!")
    await start_user()
    if user.is_connected:
        await start_bot()
    await asyncio.gather(refresh_cache(), check_logger())
    LOGGER.info("Successfully Started Userbot.")
    await asyncio.gather(getFinish(), isFinish(), idle(), aiohttpsession.close())


if __name__ == "__main__":
    uvloop.install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(starter())
