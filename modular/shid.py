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
            txt = cgr("shid_1").format(em.sukses, user_id)
            await m.reply_text(txt, parse_mode=ParseMode.HTML)
            return
        elif (
            m.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]
            and not m.reply_to_message
        ):
            await m.reply_text(
                cgr("shid_2").format(em.sukses, m.chat.id, em.profil, m.from_user.id)
            )
            return

        elif m.chat.type == ChatType.PRIVATE and not m.reply_to_message:
            await m.reply_text(cgr("shid_3").format(em.profil, m.chat.id))
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
                cgr("shid_4").format(
                    em.sukses, orig_sender, orig_id, em.warn, fwd_sender, fwd_id
                ),
                parse_mode=ParseMode.HTML,
            )
        else:
            try:
                user = await c.get_users(user_id)
            except PeerIdInvalid:
                await m.reply_text(cgr("shid_5").format(em.gagal))
                return

            await m.reply_text(
                cgr("shid_7").format(
                    em.sukses, (await mention_html(user.first_name, user.id)), user.id
                ),
                parse_mode=ParseMode.HTML,
            )
    elif m.chat.type == ChatType.PRIVATE:
        text = cgr("shid_3").format(em.sukses, m.chat.id)
        if m.reply_to_message:
            if m.forward_from:
                text += cgr("shid_8").format(em.sukses, m.forward_from.id)
            elif m.forward_from_chat:
                text += cgr("shid_8").format(em.sukses, m.forward_from_chat.id)
        await m.reply_text(text)
    else:
        text = cgr("shid_8").format(em.sukses, m.chat.id, em.profil, m.from_user.id)
        await m.reply_text(text)
    return


@ky.ubot("gifid", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if m.reply_to_message and m.reply_to_message.animation:
        await m.reply_text(
            cgr("shid_9").format(em.sukses, m.reply_to_message.animation.file_id),
            parse_mode=ParseMode.HTML,
        )
    else:
        await m.reply_text(cgr("shid_10").format(em.gagal))
    return
