################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################


from pyrogram.errors import ChatAdminRequired, ChatNotModified, RPCError
from pyrogram.types import ChatPermissions

from Mix import *

__modles__ = "Locks"
__help__ = get_cgr("help_lokk")

l_t = """
**Lock Types:**
- `all` = Everything
- `msg` = Messages
- `media` = Media, such as Photo and Video.
- `polls` = Polls
- `invite` = Add users to Group
- `pin` = Pin Messages
- `info` = Change Group Info
- `webprev` = Web Page Previews
- `inline` = Inline bots
- `animations` = Animations
- `games` = Game Bots
- `stickers` = Stickers
- `url` = Lock links"""


@ky.ubot("locktypes", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    await m.reply_text(l_t)
    return


@ky.ubot("lock", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) < 2:
        await m.reply_text(cgr("lck_1").format(em.gagal, m.command))
        return
    lock_type = m.text.split(None, 1)[1]
    chat_id = m.chat.id

    if not lock_type:
        await m.reply_text(cgr("lck_2").format(em.gagal))
        return

    get_perm = m.chat.permissions

    msg = get_perm.can_send_messages
    media = get_perm.can_send_media_messages
    webprev = get_perm.can_add_web_page_previews
    polls = get_perm.can_send_polls
    info = get_perm.can_change_info
    invite = get_perm.can_invite_users
    pin = get_perm.can_pin_messages
    stickers = animations = games = inlinebots = None

    if lock_type == "all":
        try:
            await c.set_chat_permissions(chat_id, ChatPermissions())
        except ChatNotModified:
            pass
        except ChatAdminRequired:
            await m.reply_text(cgr("lck_3").format(em.gagal))
        await m.reply_text(cgr("lck_4").format(em.sukses))
        return

    lock = LOCKS()

    if lock_type == "msg":
        msg = False
        perm = "messages"

    elif lock_type == "media":
        media = False
        perm = "audios, documents, photos, videos, video notes, voice notes"

    elif lock_type == "stickers":
        stickers = False
        perm = "stickers"

    elif lock_type == "animations":
        animations = False
        perm = "animations"

    elif lock_type == "games":
        games = False
        perm = "games"

    elif lock_type in ("inlinebots", "inline"):
        inlinebots = False
        perm = "inline bots"

    elif lock_type == "webprev":
        webprev = False
        perm = "web page previews"

    elif lock_type == "polls":
        polls = False
        perm = "polls"

    elif lock_type == "info":
        info = False
        perm = "info"

    elif lock_type == "invite":
        invite = False
        perm = "invite"

    elif lock_type == "pin":
        pin = False
        perm = "pin"

    elif lock_type == "url":
        curr = lock.insert_lock_channel(m.chat.id, "anti_links")
        if not curr:
            await m.reply_text(cgr("lck_5").format(em.sukses))
            return
        await m.reply_text(cgr("lck_6").format(em.sukses))
        return
    elif lock_type == "anonchannel":
        curr = lock.insert_lock_channel(m.chat.id, "anti_c_send")
        if not curr:
            await m.reply_text(cgr("lck_5").format(em.sukses))
            return
        await m.reply_text(cgr("lck_8").format(em.sukses))
        return
    elif lock_type == "forwardall":
        curr = lock.insert_lock_channel(m.chat.id, "anti_fwd")
        if not curr:
            await m.reply_text(cgr("lck_5").format(em.sukses))
            return
        await m.reply_text(cgr("lck_9").format(em.sukses))
        return
    elif lock_type == "forwardu":
        curr = lock.insert_lock_channel(m.chat.id, "anti_fwd_u")
        if not curr:
            await m.reply_text(cgr("lck_5").format(em.sukses))
            return
        await m.reply_text(cgr("lck_10").format(em.sukses))
        return
    elif lock_type == "forwardc":
        curr = lock.insert_lock_channel(m.chat.id, "anti_fwd_c")
        if not curr:
            await m.reply_text(cgr("lck_5").format(em.sukses))
            return
        await m.reply_text(cgr("lck_11").format(em.sukses))
        return
    else:
        await m.reply_text(cgr("lck_12").format(em.gagal))
        return

    try:
        await c.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=msg,
                can_send_media_messages=media,
                can_send_other_messages=any([stickers, animations, games, inlinebots]),
                can_add_web_page_previews=webprev,
                can_send_polls=polls,
                can_change_info=info,
                can_invite_users=invite,
                can_pin_messages=pin,
            ),
        )
    except ChatNotModified:
        pass
    except ChatAdminRequired:
        await m.reply_text(cgr("lck_13").format(em.gagal))
    await m.reply_text(cgr("lck_14").format(em.sukses, perm))
    return


@ky.ubot("unlock", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) < 2:
        await m.reply_text(cgr("lck_1").format(em.gagal, m.command))
        return
    unlock_type = m.text.split(None, 1)[1]
    chat_id = m.chat.id

    if not unlock_type:
        await m.reply_text(cgr("lck_16").format(em.gagal))
        return

    if unlock_type == "all":
        try:
            await c.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                ),
            )
        except ChatNotModified:
            pass
        except ChatAdminRequired:
            await m.reply_text(cgr("lck_13").format(em.gagal))
        await m.reply_text(cgr("lck_18").format(em.sukses))
        return

    get_uperm = m.chat.permissions

    umsg = get_uperm.can_send_messages
    umedia = get_uperm.can_send_media_messages
    uwebprev = get_uperm.can_add_web_page_previews
    upolls = get_uperm.can_send_polls
    uinfo = get_uperm.can_change_info
    uinvite = get_uperm.can_invite_users
    upin = get_uperm.can_pin_messages
    ustickers = uanimations = ugames = uinlinebots = None

    lock = LOCKS()

    if unlock_type == "msg":
        umsg = True
        uperm = "messages"

    elif unlock_type == "media":
        umedia = True
        uperm = "audios, documents, photos, videos, video notes, voice notes"

    elif unlock_type == "stickers":
        ustickers = True
        uperm = "stickers"

    elif unlock_type == "animations":
        uanimations = True
        uperm = "animations"

    elif unlock_type == "games":
        ugames = True
        uperm = "games"

    elif unlock_type in ("inlinebots", "inline"):
        uinlinebots = True
        uperm = "inline bots"

    elif unlock_type == "webprev":
        uwebprev = True
        uperm = "web page previews"

    elif unlock_type == "polls":
        upolls = True
        uperm = "polls"

    elif unlock_type == "info":
        uinfo = True
        uperm = "info"

    elif unlock_type == "invite":
        uinvite = True
        uperm = "invite"

    elif unlock_type == "pin":
        upin = True
        uperm = "pin"
    elif unlock_type == "anonchannel":
        curr = lock.remove_lock_channel(m.chat.id, "anti_c_send")

        if not curr:
            await m.reply_text(cgr("lck_19").format(em.sukses))
            return
        await m.reply_text(cgr("lck_20").format(em.sukses))
        return
    elif unlock_type == "url":
        curr = lock.remove_lock_channel(m.chat.id, "anti_links")
        if curr:
            await m.reply_text(cgr("lck_19").format(em.sukses))
            return
        await m.reply_text(cgr("lck_21").format(em.sukses))
        return
    elif unlock_type == "forwardall":
        curr = lock.remove_lock_channel(m.chat.id, "anti_fwd")

        if not curr:
            await m.reply_text(cgr("lck_19").format(em.sukses))
            return
        await m.reply_text(cgr("lck_22").format(em.sukses))
        return

    elif unlock_type == "forwardu":
        curr = lock.remove_lock_channel(m.chat.id, "anti_fwd_u")

        if not curr:
            await m.reply_text(cgr("lck_19").format(em.sukses))
            return
        await m.reply_text(cgr("lck_23").format(em.sukses))
        return

    elif unlock_type == "forwardc":
        curr = lock.remove_lock_channel(m.chat.id, "anti_fwd_c")

        if not curr:
            await m.reply_text(cgr("lck_19").format(em.sukses))
            return
        await m.reply_text(cgr("lck_24").format(em.sukses))
        return

    else:
        await m.reply_text(cgr("lck_25").format(em.gagal))

    try:

        await c.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=umsg,
                can_send_media_messages=umedia,
                can_send_other_messages=any(
                    [ustickers, uanimations, ugames, uinlinebots],
                ),
                can_add_web_page_previews=uwebprev,
                can_send_polls=upolls,
                can_change_info=uinfo,
                can_invite_users=uinvite,
                can_pin_messages=upin,
            ),
        )
    except ChatNotModified:
        pass
    except ChatAdminRequired:
        await m.reply_text(cgr("lck_13").format(em.gagal))
    await m.reply_text(cgr("lck_27").format(em.sukses, uperm))

    return


@ky.ubot("locks", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    chkmsg = await m.reply_text(cgr("proses").format(em.proses))
    v_perm = m.chat.permissions

    async def convert_to_emoji(val: bool):
        if val:
            return f"{em.sukses}"
        return f"{em.gagal}"

    lock = LOCKS()
    anti_c_send = lock.get_lock_channel("anti_c_send")
    anti_forward = lock.get_lock_channel("anti_fwd")
    anti_forward_u = lock.get_lock_channel("anti_fwd_u")
    anti_forward_c = lock.get_lock_channel("anti_fwd_c")
    anti_links = lock.get_lock_channel("anti_links")
    anon = False
    if m.chat.id in anti_c_send:
        anon = True
    anti_f = False
    anti_f_u = False
    anti_f_c = False
    if m.chat.id in anti_forward:
        anti_f = True
    if m.chat.id in anti_forward_u:
        anti_f_u = True
    if m.chat.id in anti_forward_c:
        anti_f_c = True
    antil = False
    if m.chat.id in anti_links:
        antil = True
    vmsg = await convert_to_emoji(v_perm.can_send_messages)
    vmedia = await convert_to_emoji(v_perm.can_send_media_messages)
    vother = await convert_to_emoji(v_perm.can_send_other_messages)
    vwebprev = await convert_to_emoji(v_perm.can_add_web_page_previews)
    vpolls = await convert_to_emoji(v_perm.can_send_polls)
    vinfo = await convert_to_emoji(v_perm.can_change_info)
    vinvite = await convert_to_emoji(v_perm.can_invite_users)
    vpin = await convert_to_emoji(v_perm.can_pin_messages)
    vanon = await convert_to_emoji(anon)
    vanti = await convert_to_emoji(anti_f)
    vantiu = await convert_to_emoji(anti_f_u)
    vantic = await convert_to_emoji(anti_f_c)
    await convert_to_emoji(antil)

    if v_perm is not None:
        try:
            permission_view_str = f"""
<b>{em.warn} Chat Permissions:</b>

      <b>Send Messages:</b> {vmsg}
      <b>Send Media:</b> {vmedia}
      <b>Send Stickers:</b> {vother}
      <b>Send Animations:</b> {vother}
      <b>Can Play Games:</b> {vother}
      <b>Can Use Inline Bots:</b> {vother}
      <b>Webpage Preview:</b> {vwebprev}
      <b>Send Polls:</b> {vpolls}
      <b>Change Info:</b> {vinfo}
      <b>Invite Users:</b> {vinvite}
      <b>Pin Messages:</b> {vpin}
      <b>Send as chat:</b> {vanon}
      <b>Can forward:</b> {vanti}
      <b>Can forward from user:</b> {vantiu}
      <b>Can forward from channel and chats:</b> {vantic}
      <b>Can send links:</b> {antil}
      """
            await chkmsg.edit_text(permission_view_str)

        except RPCError as e_f:
            await chkmsg.edit_text(cgr("lck_28").format(em.gagal))
            await m.reply_text(cgr("err").format(em.gagal, e_f))
    return
