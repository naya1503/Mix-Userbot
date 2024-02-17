import asyncio
import sys

from pyrogram import *
from pyrogram.errors import *

from Mix import *
from Mix.core import heroku

async def main():

    LOGGER.info(f"Connecting to {ndB.name}...")
    if ndB.ping():
        LOGGER.info(f"Connected to {ndB.name} Successfully!")
    try:
        LOGGER.info(f"Starting Telegram Client...")
        await user.start()
        await asyncio.sleep(1)
        await refresh_cache()
        await asyncio.sleep(1)
        await load_emo(user)
        await asyncio.sleep(1)
    except SessionExpired:
        LOGGER.info("Session Expired . Create New Session")
        sys.exit(1)
    except ApiIdInvalid:
        LOGGER.info("Api ID Not Valid.")
        sys.exit(1)
    if not udB.get_token(user.me.id):
        await autobot()
        await asyncio.sleep(1)
    try:
        await bot.start()
        await asyncio.sleep(1)
    except AccessTokenExpired:
        LOGGER.info("Token Expired.")
        udB.rem_token(user.me.id)
        sys.exit(1)
    except SessionRevoked:
        LOGGER.info("Token Revoked.")
        udB.rem_token(user.me.id)
        sys.exit(1)
    except AccessTokenInvalid:
        LOGGER.info("Token Invalid, Try again.")
        udB.rem_token(user.me.id)
        sys.exit(1)
    except UserDeactivated:
        LOGGER.info("Bot Deactive, Try again.")
        udB.rem_token(user.me.id)
        sys.exit(1)
    await check_logger()
    LOGGER.info(f"Check Finished.")
    await asyncio.sleep(1)
    await refresh_modules()
    LOGGER.info(f"Modules Imported...")
    await asyncio.sleep(1)
    LOGGER.info("Successfully Started Userbot.")
    await idle()


if __name__ == "__main__":
    # install()
    heroku()
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
