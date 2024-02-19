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

async def load_emo():
    from Mix import user
    eping = "🏓"
    ping_id = "<emoji id=5269563867305879894>🏓</emoji>"
    epong = "🥵"
    pong_id = "<emoji id=6183961455436498818>🥵</emoji>"
    eproses = "🔄"
    proses_id = "<emoji id=6113844439292054570>🔄</emoji>"
    egagal = "❌"
    gagal_id = "<emoji id=6113872536968104754>❌</emoji>"
    esukses = "✅"
    sukses_id = "<emoji id=6113647841459047673>✅</emoji>"
    eprofil = "👤"
    profil_id = "<emoji id=5373012449597335010>👤</emoji>"
    ealive = "⭐"
    alive_id = "<emoji id=6127272826341690178>⭐</emoji>"
    ewarn = "❗️"
    warn_id = "<emoji id=6172475875368373616>❗️</emoji>"
    eblock = "🚫"
    block_id = "<emoji id=5240241223632954241>🚫</emoji>"
    a = udB.get_var(user.me.id, "emo_ping")
    b = udB.get_var(user.me.id, "emo_pong")
    c = udB.get_var(user.me.id, "emo_proses")
    d = udB.get_var(user.me.id, "emo_gagal")
    e = udB.get_var(user.me.id, "emo_sukses")
    f = udB.get_var(user.me.id, "emo_profil")
    g = udB.get_var(user.me.id, "emo_alive")
    h = udB.get_var(user.me.id, "emo_warn")
    i = udB.get_var(user.me.id, "emo_block")
    uprem = user.me.is_premium
    if uprem == True:
        if (a, b, user.me.id, d, e, f, g, h, i) is not None:
            return
        else:
            udB.set_var(user.me.id, "emo_ping", ping_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_pong", pong_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_proses", proses_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_gagal", gagal_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_sukses", sukses_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_profil", profil_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_alive", alive_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_warn", warn_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_block", block_id)
    elif uprem == False:
        if (a, b, user.me.id, d, e, f, g, h, i) is not None:
            return
        else:
            udB.set_var(user.me.id, "emo_ping", eping)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_pong", epong)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_proses", eproses)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_gagal", egagal)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_sukses", esukses)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_profil", eprofil)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_alive", ealive)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_warn", ewarn)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_block", eblock)

