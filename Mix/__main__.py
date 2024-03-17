import asyncio
import importlib
import sys
from os import execvp
from sys import executable

from pyrogram import *
from pyrogram.errors import *
from uvloop import install

from Mix import *
from Mix.core.gclog import getFinish
from Mix.core.waktu import auto_clean
from modular import USER_MOD

lool = asyncio.get_event_loop()


async def start_user():
    LOGGER.info(f"Importing User Modules...")
    for modul in USER_MOD:
        imported_module = importlib.import_module(f"modular.{modul}")
        if hasattr(imported_module, "__modles__") and imported_module.__modles__:
              imported_module.__modles__ = imported_module.__modles__
              if hasattr(imported_module, "__help__") and imported_module.__help__:
                  CMD_HELP[imported_module.__modles__.replace(" ", "_").lower()] = (imported_module)
    LOGGER.info(f"Successfully Import User Modules...")
    LOGGER.info(f"Starting Telegram User Client...")
    try:
        await nlx.start()
    except (SessionExpired, ApiIdInvalid, UserDeactivatedBan):
        LOGGER.info("Check your session or api id!!")
        sys.exit(1)


async def start_bot():
    LOGGER.info(f"Importing Bot Modules...")
    for plus in BOT_PLUGINS:
        imported_module = importlib.import_module(f"assistant.{plus}")
        importlib.reload(imported_module)
    LOGGER.info(f"Successfully Import Bot Modules...")
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
    user_task = asyncio.create_task(start_user())
    bot_task = asyncio.create_task(start_bot())
    await user_task
    await bot_task
    # if TAG_LOG is None:
    # await check_logger()
    # await asyncio.gather(refresh_cache())
    LOGGER.info("Successfully Started Userbot.")
    await asyncio.gather(refresh_cache(), getFinish(), auto_clean(), isFinish(), idle())
    # await asyncio.gather(auto_clean(), isFinish(), idle())


if __name__ == "__main__":
    install()
    # loop = asyncio.get_event_loop_policy()
    # event_loop = loop.get_event_loop()
    # asyncio.set_event_loop(event_loop)
    # event_loop.run_until_complete(starter())
    lool.run_until_complete(starter())
