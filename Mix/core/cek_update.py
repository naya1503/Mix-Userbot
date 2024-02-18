import os
import sys
import subprocess
from team.nandev.class_log import LOGGER

async def cek_updater():
    process = subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        LOGGER.info(f"Error: {error.decode()}")
        sys.exit(1)
    
    if "Already up to date." in output.decode():
        LOGGER.info("Mix-Userbot Already up to date.")
        return
    
    os.execl(sys.executable, sys.executable, "-m", "Mix")
