#
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

from config import *

from team.nandev.class_log import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(
        install_requirements()
    )


def git():
    REPO_LINK = upstream_repo
    if git_token:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        upstream_repo = (
            f"https://{GIT_USERNAME}:{git_token}@{TEMP_REPO}"
        )
    else:
        upstream_repo = upstream_repo
    try:
        repo = Repo()
        LOGGER.info(f"Git Client Found [VPS DEPLOYER]")
    except GitCommandError:
        LOGGER.info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", upstream_repo)
        origin.fetch()
        repo.create_head(
            upstream_branch,
            origin.refs[upstream_branch],
        )
        repo.heads[upstream_branch].set_tracking_branch(
            origin.refs[upstream_branch]
        )
        repo.heads[upstream_branch].checkout(True)
        try:
            repo.create_remote("origin", upstream_repo)
        except BaseException:
            pass
        nrs = repo.remote("origin")
        nrs.fetch(upstream_branch)
        try:
            nrs.pull(upstream_branch)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        install_req("pip3 install --no-cache-dir -r requirements.txt")
        LOGGER.info(f"Fetched Updates from: {REPO_LINK}")
