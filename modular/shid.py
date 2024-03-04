################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

from pyrogram.enums import *
from pyrogram.errors import *

from Mix import *
from Mix.core.parser import mention_html
from Mix.core.sender_tools import extract_user

__modles__ = "ShowID"
__help__ = get_cgr("help_sid")


@ky.ubot("id", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id, _, _ = await extract_user(c, m)
    try:
        if user_id and len(m.text.split()) == 2:
            txt = f"{em.sukses} ID pengguna <code>{user_id}</code>"
            await m.reply_text(txt, parse_mode=ParseMode.HTML)
            return
        elif (
            m.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]
            and not m.reply_to_message
        ):
            await m.reply_text(
                text=f"{em.sukses} ID Group <code>{m.chat.id}</code>\n{em.profil} Your ID <code>{m.from_user.id}</code>"
            )
            return

        elif m.chat.type == ChatType.PRIVATE and not m.reply_to_message:
            await m.reply_text(text=f"{em.profil} Your ID is <code>{m.chat.id}</code>.")
            return
    except Exception as e:
        await m.reply_text(e)
        return
    if user_id:
        if m.reply_to_message and m.reply_to_message.forward_from:
            user1 = m.reply_to_message.from_user
            user2 = m.reply_to_message.forward_from
            orig_sender = await mention_html(user2.first_name, user2.id)
            orig_id = f"<code>{user2.id}</code>"
            fwd_sender = await mention_html(user1.first_name, user1.id)
            fwd_id = f"<code>{user1.id}</code>"
            await m.reply_text(
                text=f"""
{em.sukses} Original Sender - {orig_sender} <code>{orig_id}</code>
{em.warn} Forwarder - {fwd_sender} <code>{fwd_id}</code>
""",
                parse_mode=ParseMode.HTML,
            )
        else:
            try:
                user = await c.get_users(user_id)
            except PeerIdInvalid:
                await m.reply_text(
                    text=f"{em.gagal} Gagal mendapatkan ID pengguna.\nMungkin anda belum pernah berinteraksi!!"
                )
                return

            await m.reply_text(
                f"{em.sukses} {(await mention_html(user.first_name, user.id))} ID is <code>{user.id}</code>.",
                parse_mode=ParseMode.HTML,
            )
    elif m.chat.type == ChatType.PRIVATE:
        text = f"{em.sukses} Your ID is <code>{m.chat.id}</code>."
        if m.reply_to_message:
            if m.forward_from:
                text += f"{em.sukses} Forwarded from user ID <code>{m.forward_from.id}</code>."
            elif m.forward_from_chat:
                text += f"{em.sukses} Forwarded from user ID <code>{m.forward_from_chat.id}</code>."
        await m.reply_text(text)
    else:
        text = f"{em.sukses} Chat ID <code>{m.chat.id}</code>\n{em.profil} Your ID <code>{m.from_user.id}</code>"
        await m.reply_text(text)
    return


@ky.ubot("gifid", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if m.reply_to_message and m.reply_to_message.animation:
        await m.reply_text(
            f"{em.sukses} Gif ID:\n<code>{m.reply_to_message.animation.file_id}</code>",
            parse_mode=ParseMode.HTML,
        )
    else:
        await m.reply_text(text=f"{em.gagal} Silahkan balas ke gif.")
    return
