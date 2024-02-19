################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import asyncio
import os
import socket
import subprocess
import sys

import heroku3
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from team.nandev.class_log import LOGGER

from config import *

from .misc import XCB

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def in_heroku():
    return "heroku" in socket.getfqdn()


async def cek_updater():
    if await in_heroku():
        if heroku_api and heroku_app_name:
            hehe = heroku3.from_key(heroku_api)
            hehe.app(heroku_app_name)
    try:
        repo = Repo()
    except GitCommandError:
        LOGGER.info("Kesalahan Perintah Git")
        return
    except InvalidGitRepositoryError:
        LOGGER.info("Repositori Git Tidak Valid")
        return
    to_exc = f"git fetch origin {upstream_branch} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{upstream_branch}"):
        verification = str(checks.count())
    if verification == "":
        LOGGER.info("Mix-Userbot is up-to-date!")
        return
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )

    os.system("git stash &> /dev/null && git pull")
    if await in_heroku():
        try:
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            LOGGER.info(
                f"Something went wrong while initiating reboot! Please try again later or check logs for more info.\n\n{err}"
            )
    else:
        process = subprocess.Popen(
            "git pull", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        if error:
            LOGGER.info(f"Error: {error.decode()}")
            return

        if "Already up to date." in output.decode():
            LOGGER.info("Mix-Userbot Already up to date.")
            return

        os.execl(sys.executable, sys.executable, "-m", "Mix")
