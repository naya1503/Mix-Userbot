

################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

__modles__ = "developer"
__help__ = """
 Help Command Developer

• Perintah : <code>{0}sh</code>
• Penjelasan : Execute code.

• Perintah : <code>{0}eval</code>
• Penjelasan : Execute code.

• Perintah : <code>{0}trash</code>
• Penjelasan : Dump message.

• Perintah : <code>{0}host</code>
• Penjelasan : System host.

• Perintah : <code>{0}host</code>
• Penjelasan : System host.

• Perintah : <code>{0}stats</code>
• Penjelasan : System stats.
"""

from Mix import *
import subprocess

@ky.ubot("update", sudo=True)
@ky.devs("diupdate")
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    xx = await m.reply(f"{emo.proses} Processing...")
    try:
        out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
        if "Already up to date." in str(out):
            return await xx.edit("Its already up-to date!")
        await xx.edit(f"`{out}`")
    except Exception as e:
        return await xx.edit(str(e))
    await c.restart()
    
    
@ky.ubot("restart", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    xx = await m.reply(f"{emo.proses} Processing...")
    await xx.edit(f"{emo.proses} Please Wait...")
    await xx.edit(f"{emo.sukses} Succesfully, wait for a minute.")
    await c.restart2()