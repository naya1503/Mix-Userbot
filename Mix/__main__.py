import asyncio
import sys
import importlib
from modular import USER_MOD
from pyrogram import *
from pyrogram.errors import *

from assistant import bot_plugins
from Mix import *


async def starter():
    LOGGER.info(f"Check Updater...")
    await cek_updater()
    LOGGER.info(f"Updater Finished...")
    LOGGER.info(f"Connecting to {ndB.name}...")
    if ndB.ping():
        LOGGER.info(f"Connected to {ndB.name} Successfully!")
    try:
        LOGGER.info(f"Starting Telegram Client...")
        await user.start()
        LOGGER.info(f"Importing All Modules...")
        for modul in USER_MOD:
            imported_module = importlib.import_module(f"modular.{modul}")
            if hasattr(imported_module, "__modles__") and imported_module.__modles__:
                imported_module.__modles__ = imported_module.__modles__
                if hasattr(imported_module, "__help__") and imported_module.__help__:
                    CMD_HELP[imported_module.__modles__.replace(" ", "_").lower()] = (
                        imported_module
                    )
    except (SessionExpired, ApiIdInvalid, UserDeactivatedBan):
        LOGGER.info("Check your session or api id!!")
    if bot_token is None:
        await autobot()
        await asyncio.sleep(1)
    try:
        await bot.start()
        await bot_plugins()
        await asyncio.sleep(1)
    except (AccessTokenExpired, SessionRevoked, AccessTokenInvalid):
        LOGGER.info("Token Expired.")
        sys.exit(1)
    await refresh_cache()
    await check_logger()
    await getFinish()
    LOGGER.info("Successfully Started Userbot.")
    await isFinish()
    await idle()
    await aiohttpsession.close()


if __name__ == "__main__":
    loop.run_until_complete(starter())
