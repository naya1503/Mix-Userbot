from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import *

from Mix import *

__modles__ = "Join"
__help__ = """
Help Command Join 

• Perintah: <code>{0}join</code> [username gc/ch atau id gc/ch atau link gc/ch]
• Penjelasan: Untuk Bergabung ke Group atau Channel.

• Perintah: <code>{0}leave</code> [username gc/ch atau id gc/ch atau link gc/ch]
• Penjelasan: Untuk Meninggalkan Group atau Channel.

• Perintah: <code>{0}leaveallgc</code>
• Penjelasan: Untuk Meninggalkan Semua Group Yang Ada Di Akun Anda.

• Perintah: <code>{0}leaveallch</code>
• Penjelasan: Untuk Meninggalkan Semua Channel Yang Ada Di Akun Anda.
"""


@ky.ubot("join", sudo=True)
@ky.devs("Cjoin")
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = m.command[1] if len(m.command) > 1 else m.chat.id
    ceger = await m.reply_text(f"{em.proses} <b>Processing...</b>")
    try:
        chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
        if chat_id.startswith("https://t.me/"):
            chat_id = chat_id.split("/")[-1]
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

    try:
        chat_id = m.chat.id

        if chat_id in NO_GCAST:
            return await m.reply(
                f"{em.gagal} <b>Tidak dapat menggunakan perintah itu di sini!</b>"
            )

        if str(chat_id).startswith("https://t.me/"):
            chat_id = chat_id.split("/")[-1]
            inpogc = await c.get_chat(chat_id)
            namagece = inpogc.title
            ceger = await m.reply(f"{em.proses} <code>Processing...</code>")
            if str(chat_id) in NO_GCAST or inpogc.id in NO_GCAST:
                await ceger.edit(
                    f"{em.gagal} <b>Tidak boleh menggunakan perintah itu di sini!</b>"
                )
            else:
                await c.leave_chat(chat_id)
                await ceger.edit(
                    f"{em.sukses} {c.me.mention} Berhasil keluar dari <code>{namagece}</code>"
                )
        else:
            await m.reply(f"{em.sukses} <b>Bye!</b>")
            await c.leave_chat(chat_id)

    except ChatAdminRequired:
        await m.reply(
            f"{em.gagal} <b>Saya tidak memiliki izin untuk meninggalkan obrolan ini!</b>"
        )
    except UserNotParticipant:
        await m.reply(
            f"{em.gagal} <b>Anda bukan anggota atau member di <code>{namagece}</code></b>"
        )
    except Exception as e:
        await m.reply(
            f"{em.gagal} <b>Terjadi kesalahan saat mencoba meninggalkan obrolan:</b> <code>{str(e)}</code>"
        )


@ky.ubot("leaveallgc|kickmeallgc", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    xenn = await m.reply_text(
        f"{em.proses} <code>Global Leave from group chats...</code>"
    )
    luci = 0
    nan = 0
    ceger = [-1001986858575, -1001876092598, -1001812143750]

    async for dialog in c.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                chat_info = await c.get_chat_member(chat, "me")
                user_status = chat_info.status
                if chat not in ceger and user_status not in (
                    ChatMemberStatus.OWNER,
                    ChatMemberStatus.ADMINISTRATOR,
                ):
                    nan += 1
                    await c.leave_chat(chat)
            except BaseException:
                luci += 1
    await xenn.edit(
        f"{em.sukses} <b>Successfully left {nan} Groups, Failed to leave {luci} Groups</b>"
    )


@ky.ubot("leaveallch|kickmeallch", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xenn = await m.reply_text(f"{em.proses} <code>Global Leave from Channels...</code>")
    luci = 0
    nan = 0
    ceger = [-1001713457115 - 1001818398503 - 1001697717236]

    async for dialog in c.iter_dialogs():
        if dialog.chat.type == ChatType.CHANNEL:
            chat = dialog.chat.id
            try:
                chat_info = await c.get_chat_member(chat, "me")
                user_status = chat_info.status
                if chat not in ceger and user_status not in (
                    ChatMemberStatus.OWNER,
                    ChatMemberStatus.ADMINISTRATOR,
                ):
                    nan += 1
                    await c.leave_chat(chat)
            except Exception:
                luci += 1

    await xenn.edit(
        f"{em.sukses} <b>Successfully left {nan} Channels, Failed to leave {luci} Channels</b>"
    )
