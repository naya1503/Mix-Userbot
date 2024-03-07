from pyrogram.enums import *
from pyrogram.methods import *
from pyrogram.types import *

from Mix import *

__modles__ = "Invite"
__help__ = """
Help Command Invite 

• Perintah: <code>{0}invite</code>
• Penjelasan: Untuk mengundang seseorang ke group/channel.

• Perintah: <code>{0}getlink</code>
• Penjelasan: Untuk mendapatkan link invite chat.
"""


@ky.ubot("invite|undang", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    mg = await reply_text(f"{em.proses} <code>Adding Users!</code>")
    user_s_to_add = m.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(f"{em.gagal} Give me User's Id/Username")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await c.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"{em.gagal} Unable To Add Users! \nTraceBack : {e}")
        return
    await mg.edit(f"{em.sukses} Sucessfully Added {len(user_list)} To {mg.chat.title}")


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
