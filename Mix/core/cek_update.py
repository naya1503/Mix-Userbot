import os
import sys

async def cek_updater():
    os.system("git pull")
    os.execl(sys.executable, sys.executable, "-m", "Mix")