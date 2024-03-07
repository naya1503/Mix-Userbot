from pyrogram.enums import *
from pyrogram.errors import *
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
    mg = await m.reply_text(f"{em.proses} <code>Menambahkan Pengguna ...</code>")
    if len(m.command) < 2:
        await mg.edit(f"{em.gagal} Berikan ID/Nama Pengguna")
        return

    user_s_to_add = m.command[1]
    user_list = user_s_to_add.split(" ")

    if not user_list:
        await mg.edit(f"{em.gagal} Berikan ID/Nama Pengguna")
        return
    try:
        await c.add_chat_members(m.chat.id, user_list, forward_limit=100)
    except errors.BadRequest as e:
        await mg.edit(
            f"{em.gagal} Gagal menambahkan pengguna. Alasan: <code>{str(e)}</code>"
        )
        return
    mention = (await c.get_users(user_id)).mention
    await mg.edit(f"{em.sukses} Berhasil Menambahkan {mention} ke {m.chat.title}")


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
