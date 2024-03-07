from pyrogram.enums import *
from pyrogram.methods import *
from pyrogram.types import *

from Mix import *

__modles__ = "Getlink"
__help__ = """
Help Command Info 

• Perintah: <code>{0}getlink</code>
• Penjelasan: Untuk mendapatkan link invite chat.
"""


@ky.ubot("getlink|invitelink", sudo=True)
@ky.devs("getling")
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = await m.reply_text(f"{em.proses}<code>Processing...</code>")

    if m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        m.chat.title
        try:
            link = await c.export_chat_invite_link(m.chat.id)
            await Nan.edit(f"{em.sukses}Link Invite: {link}")
        except Exception:
            await Nan.edit(f"{em.gagal} You don't have Required permission")
    elif m.chat.type == ChatType.CHANNEL:
        try:
            link = await c.export_chat_invite_link(m.chat.id)
            await Nan.edit(f"{em.sukses}Link Invite: {link}")
        except Exception:
            await Nan.edit(f"{em.gagal} You don't have Required permission")
    else:
        await Nan.edit("This feature is only available for groups and channels.")
