import os
import sys
import subprocess

async def cek_updater():
    process = subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        LOGGER(f"Error: {error.decode()}")
        sys.exit(1)
    
    if "Already up to date." in output.decode():
        LOGGER("Mix-Userbot Already up to date.")
        return
    
    os.execl(sys.executable, sys.executable, "-m", "Mix")
