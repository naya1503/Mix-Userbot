import asyncio
from os import execvp
from sys import executable
import importlib
from pyrogram import *
from pyrogram.errors import *
from uvloop import install
from assistant import BOT_PLUGINS
from beban import dasar_laknat, autor_gc, autor_ch, autor_us, autor_bot, autor_all
from Mix import *
from Mix.core.gclog import check_logger, getFinish
from Mix.core.waktu import auto_clean

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
        LOGGER.info(f"Importing Bot Modules...")
        for plus in BOT_PLUGINS:
            imported_module = importlib.import_module("assistant." + plus)
            importlib.reload(imported_module)
        LOGGER.info(f"Successfully Import Bot Modules...")
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

async def main():
    await starter()
    await asyncio.gather(refresh_cache(), getFinish())
    LOGGER.info("Successfully Started Userbot.")
    task_afk = asyncio.create_task(auto_clean())
    task_gc = asyncio.create_task(autor_gc())
    task_ch = asyncio.create_task(autor_ch())
    task_us = asyncio.create_task(autor_us())
    task_bot = asyncio.create_task(autor_bot())
    task_all = asyncio.create_task(autor_all())
    await asyncio.gather(task_afk, task_gc, task_ch, task_us, task_bot, task_all, isFinish(), idle())

if __name__ == "__main__":
    install()
    # loop = asyncio.get_event_loop_policy()
    # event_loop = loop.get_event_loop()
    # asyncio.set_event_loop(event_loop)
    # event_loop.run_until_complete(starter())
    lool.run_until_complete(main())
