from pyrogram.types import *

from Mix import *

__modles__ = "Join"
__help__ = """
Help Command Join 

• Perintah: <code>{0}Join</code>
• Penjelasan: Untuk Join ke chat.
"""


@ky.ubot("join|masuk", sudo=True)
@ky.devs("Cjoin")
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = m.command[1] if len(m.command) > 1 else m.chat.id
    ceger = await m.reply_text(f"{em.proses} <code>Processing...</code>")
    try:
        await ceger.edit(f"{em.sukses} <b>Berhasil Bergabung ke Chat ID</b> {Nan}")
        await c.join_chat(Nan)
    except Exception as ex:
        await ceger.edit(f"ERROR: \n\n{str(ex)}")
