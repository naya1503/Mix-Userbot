#
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import socket
from os import execvp
from sys import executable
from sys import version as pyver

import heroku3
import wget
from aiohttp import ClientSession
from pyrogram import *
from pyrogram import __version__ as pyrover
from pyrogram.errors import *
from pyrogram.types import ChatPrivileges
from pytgcalls import __version__ as pytgver
from team.nandev.class_handler import TAG_LOG
from team.nandev.class_log import LOGGER
from team.nandev.database import ndB

from config import *

HAPP = None

aiohttpsession = ClientSession()


def on_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(heroku_api),
    "https",
    str(heroku_app_name),
    "HEAD",
    "dev",
]


def heroku():
    global HAPP
    if on_heroku:
        if heroku_api and heroku_app_name:
            try:
                Heroku = heroku3.from_key(heroku_api)
                HAPP = Heroku.app(heroku_app_name)
                LOGGER.info(f"Heroku App Configured")
            except BaseException:
                LOGGER.warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )