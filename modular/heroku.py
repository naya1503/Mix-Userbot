################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
################################################################


import asyncio
import importlib
import math
import os
import sys
from datetime import datetime
from importlib import import_module

import dotenv
import heroku3
import requests
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from team.nandev.class_log import LOGGER

from config import *
from Mix import XCB, Emojik, in_heroku, ky, on_heroku, paste, user

from . import import_modular

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__modles__ = "Heroku"
__help__ = get_cgr("help_heroku")

@ky.ubot("getlog", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    try:
        if on_heroku():
            if heroku_api and heroku_app_name:
                Heroku = heroku3.from_key(heroku_api)
                haha = Heroku.app(heroku_app_name)
            data = haha.get_log()
            link = await paste(data)
            return await m.reply_text(link)
        else:
            if os.path.exists("logs.txt"):
                log = open("logs.txt")
                lines = log.readlines()
                data = ""
                try:
                    NUMB = int(m.text.split(None, 1)[1])
                except:
                    NUMB = 100
                for x in lines[-NUMB:]:
                    data += x
                link = await paste(data)
                return await m.reply_text(link)
            else:
                return await m.reply_text(
                    f"{em.gagal} Anda hanya bisa mendapatkan log dari Heroku."
                )
    except Exception as e:
        print(e)
        await m.reply_text(f"{em.gagal} Anda hanya bisa mendapatkan log dari Heroku")


@ky.ubot("getvar", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    usage = f"{em.gagal} Usage command : `getvar variabel`."
    if len(m.command) != 2:
        return await m.reply_text(usage)
    check_var = m.text.split(None, 2)[1]
    if on_heroku():
        if heroku_api and heroku_app_name:
            Heroku = heroku3.from_key(heroku_api)
            haha = Heroku.app(heroku_app_name)
        heroku_config = haha.config()
        if check_var in heroku_config:
            return await m.reply_text(
                f"{em.sukses} **{check_var}:** `{heroku_config[check_var]}`"
            )
        else:
            return await m.reply_text(
                f"{em.gagal} Tidak dapat menemukan var seperti itu."
            )
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await m.reply_text(f"{em.gagal} env file tidak ditemukan.")
        output = dotenv.get_key(path, check_var)
        if not output:
            await m.reply_text(f"{em.gagal} Tidak dapat menemukan var seperti itu.")
        else:
            return await m.reply_text(f"{em.sukses} **{check_var}:** `{str(output)}`")


@ky.ubot("delvar", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    usage = f"{em.gagal} Usage command : `delvar` [variabel]."
    if len(m.command) != 2:
        return await m.reply_text(usage)
    check_var = m.text.split(None, 2)[1]
    if on_heroku():
        if heroku_api and heroku_app_name:
            Heroku = heroku3.from_key(heroku_api)
            haha = Heroku.app(heroku_app_name)
        heroku_config = haha.config()
        if check_var in heroku_config:
            await m.reply_text(f"{em.sukses} {check_var} Dihapus.")
            del heroku_config[check_var]
        else:
            return await m.reply_text(
                f"{em.gagal} Tidak dapat menemukan var seperti itu."
            )
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await m.reply_text(f"{em.gagal} env file tidak ditemukan.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            await m.reply_text(f"{em.gagal} Tidak dapat menemukan var seperti itu.")
        else:
            await m.reply_text(f"{em.sukses} {check_var} Dihapus.")
            os.execl(sys.executable, sys.executable, "-m", "Mix")


@ky.ubot("setvar", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    usage = f"{em.gagal} **Penggunaan:**\n`setvar` [variabel] [value]"
    if len(m.command) < 3:
        return await m.reply_text(usage)
    to_set = m.text.split(None, 2)[1].strip()
    value = m.text.split(None, 2)[2].strip()
    if on_heroku():
        if heroku_api and heroku_app_name:
            Heroku = heroku3.from_key(heroku_api)
            haha = Heroku.app(heroku_app_name)
        heroku_config = haha.config()
        if to_set in heroku_config:
            await m.reply_text(f"{em.sukses} {to_set} telah berhasil diperbarui")
        else:
            await m.reply_text(f"{em.sukses} {to_set} telah berhasil ditambahkan")
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await m.reply_text(f"{em.gagal} env file tidak ditemukan.")
        dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            await m.reply_text(f"{em.sukses} {to_set} telah berhasil diperbarui")
        else:
            await m.reply_text(f"{em.sukses} {to_set} telah berhasil ditambahkan")
        os.execl(sys.executable, sys.executable, "-m", "Mix")


@ky.ubot("usage", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    ### Credits CatUserbot
    if on_heroku():
        if heroku_api and heroku_app_name:
            hehe = heroku3.from_key(heroku_api)
            hehe.app(heroku_app_name)
    else:
        return await m.reply_text(f"{em.gagal} Hanya untuk Heroku.")
    dyno = await m.reply_text(
        f"{em.proses} Memeriksa Penggunaan Heroku. Mohon Tunggu.."
    )
    Heroku = heroku3.from_key(heroku_api)
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {heroku_api}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
{em.sukses} **DYNO USAGE**

{em.sukses} <u>Usage:</u>
**Total Used: `{AppHours}h`  `{AppMinutes}m` [`{AppPercentage}%`**]

{em.sukses} <u>Remaining Quota:</u>
**Total Left: `{hours}h`  `{minutes}m`  [`{percentage}%`**]"""
    return await dyno.edit(text)


@ky.ubot("update", sudo=True)
@ky.devs("diupdate")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if await in_heroku():
        if heroku_api and heroku_app_name:
            hehe = heroku3.from_key(heroku_api)
            hehe.app(heroku_app_name)
    jj = await m.reply_text(f"{em.proses} Memeriksa pembaruan yang tersedia...")
    try:
        repo = Repo()
    except GitCommandError:
        return await jj.edit(f"{em.gagal} Kesalahan Perintah Git")
    except InvalidGitRepositoryError:
        return await jj.edit(f"{em.gagal} Repositori Git Tidak Valid")
    to_exc = f"git fetch origin {upstream_branch} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{upstream_branch}"):
        verification = str(checks.count())
    if verification == "":
        return await jj.edit(f"{em.alive} Mix-Userbot is up-to-date!")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{upstream_branch}"):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ Commited on:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>A new update is available for the Mix-Userbot !</b>\n\n<code>➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await paste(updates)
        nrs = await jj.edit(
            f"<b>A new update is available for the Mix-Userbot!</b>\n\n<code>➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n[Click Here to checkout Updates]({url})",
            disable_web_page_preview=True,
        )
    else:
        nrs = await jj.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")
    if await in_heroku():
        try:
            await jj.edit(
                f"<b>{nrs.text}\n\nMix-Userbot was updated successfully! Now, wait for 2 - 3 mins until the bot restarts!</b>"
            )
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            os.execl(sys.executable, sys.executable, "-m", "Mix")
        except Exception as err:
            await jj.edit(
                f"{nrs.text}\n\nSomething went wrong while initiating reboot! Please try again later or check logs for more info."
            )
            return await bot.send_message(
                udB.get_logger(c.me.id),
                f"AN EXCEPTION OCCURRED AT #UPDATER DUE TO: <code>{err}</code>\n\nLaporkan Ke @KynanSupport.",
            )
    else:

        await jj.edit(
            f"<b>{nrs.text}\n\nMix-Userbot was updated successfully! Now, wait for 2 - 3 mins until the bot restarts!</b>"
        )
        os.system("git pull")
        os.system("pip3 install -r requirements.txt")
        os.execl(sys.executable, sys.executable, "-m", "Mix")


@ky.ubot("reboot", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    jj = await m.reply_text(f"{em.proses} Restarting....")
    await jj.edit(
        f"{em.sukses} Reboot has been initiated successfully! Wait for 1 - 2 minutes until the bot restarts."
    )
    os.system("git pull")
    os.execl(sys.executable, sys.executable, "-m", "Mix")


async def reload_user():
    # await user.start()
    try:
        modxx = import_modular()
        for modx in modxx:
            imported_module = import_module(f"modular.{modx}")
            importlib.reload(imported_module)
    except Exception as er:
        LOGGER.error(f"{er}")


@ky.ubot("restart", sudo=True)
async def _(c: user, m):
    try:
        await reload_user()
    except Exception as er:
        await m.reply(f"Error {er}")
