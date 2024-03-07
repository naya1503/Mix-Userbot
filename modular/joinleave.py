from pyrogram.types import *

from Mix import *

__modles__ = "Join"
__help__ = """
Help Command Join 

• Perintah: <code>{0}join</code>
• Penjelasan: Untuk join ke Group atau Channel.
"""


@ky.ubot("join|masuk", sudo=True)
@ky.devs("Cjoin")
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = m.command[1] if len(m.command) > 1 else m.chat.id
    ceger = await m.reply_text(f"{em.proses} <b>Processing...</b>")
    try:
        inpogc = await c.get_chat(Nan)
        namagece = inpogc.title

        await ceger.edit(
            f"{em.sukses} <b>Berhasil Bergabung ke</b> <code>{namagece}</code>"
        )
        await c.join_chat(Nan)
    except Exception as ex:
        await ceger.edit(f"{em.gagal} <b>ERROR: </b>\n\n<code>{str(ex)}</code>")


@ky.ubot("leave|kickme", sudo=True)
@ky.devs("Cleave")
async def _(c, m):
    em = Emojik()
    em.initialize()
    lus = m.command[1] if len(m.command) > 1 else m.chat.id
    ceger = await m.reply_text(f"{em.proses} <code>Processing...</code>")
    if m.chat.id in NO_GCAST:
        return await ceger.edit(
            f"{em.gagal} <b>Perintah ini Dilarang digunakan di Group ini</b>"
        )
    try:
        await ceger.edit_text(f"{em.sukses} {c.me.mention} <b>has left this group, bye!!</b>")
        await c.leave_chat(lus)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n<code>{str(ex)}</code>")
