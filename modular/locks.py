################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

__modles__ = "Locks"
__help__ = """
Help Command Group 

• Perintah: <code>{0}locktypes</code> 
• Penjelasan: Untuk melihat argumen kunci.

• Perintah: <code>{0}lock</code> 
• Penjelasan: Untuk mengunci izin.

• Perintah: <code>{0}unlock</code> 
• Penjelasan: Untuk membuka izin.

• Perintah: <code>{0}locks</code> 
• Penjelasan: Untuk melihat semua izin.
"""

from asyncio import sleep

from pyrogram import filters
from pyrogram.enums import MessageEntityType as MET
from pyrogram.errors import ChatAdminRequired, ChatNotModified, RPCError
from pyrogram.types import ChatPermissions

from Mix import *

from .restrict import list_admins

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
- `anonchannel` = Send as chat will be locked
- `forwardall` = Forwarding from channel and user
- `forwardu` = Forwarding from user
- `forwardc` = Forwarding from channel
- `url` = Lock links"""


async def prevent_approved(m):
    ceksud = udB.get_list_from_var(user.me.id, "SUDO_USER", "ID_NYA")
    ms = m.from_user.id
    for ms in (DEVS, ceksud):
        try:
            await m.chat.unban_member(ms)
        except (ChatAdminRequired, ChatNotModified, RPCError):
            continue
        await sleep(0.1)
    return


async def is_approved_user(c: user, m):
    admins_group = await list_admins(m.chat.id)
    if m.forward_from:
        if (
            m.from_user.id in DEVS
            or m.from_user.id in admins_group
            or m.from_user.id == c.me.id
        ):
            return False
        # return True
    elif m.forward_from_chat:
        x_chat = (await c.get_chat(m.forward_from_chat.id)).linked_chat
        if (
            m.from_user.id in DEVS
            or m.from_user.id in admins_group
            or m.from_user.id == c.me.id
        ):
            return False
        if not x_chat:
            return False
        elif x_chat and x_chat.id == m.chat.id:
            return True
    elif m.from_user:
        if (
            m.from_user.id in DEVS
            or m.from_user.id in admins_group
            or m.from_user.id == c.me.id
        ):
            return False
        # return False


async def delete_messages(c: user, m):
    try:
        await c.delete_messages(m.chat.id, message_ids=m.id)
        return
    except RPCError as e:
        await m.reply(f"{e}")


@user.on_message(filters.forwarded & filters.group, group=69)
async def _(c: user, m):
    lock = LOCKS()
    all_chats = lock.get_lock_channel()
    if not all_chats:
        return
    if m.chat.id not in all_chats:
        return
    if m.sender_chat and not (m.forward_from_chat or m.forward_from):
        if m.sender_chat.id == m.chat.id:
            return
        await delete_messages(c, m)
        return
    is_approved = await is_approved_user(c, m)
    entity = m.entities if m.text else m.caption_entities
    if entity:
        for i in entity:
            if i.type in [MET.URL or MET.TEXT_LINK]:
                if not is_approved:
                    await delete_messages(c, m)
                    return
    elif m.forward_from or m.forward_from_chat:
        if not is_approved:
            if lock.is_particular_lock(m.chat.id, "anti_fwd"):
                await delete_messages(c, m)
                return
            elif (
                lock.is_particular_lock(m.chat.id, "anti_fwd_u")
                and not m.forward_from_chat
            ):
                await delete_messages(c, m)
                return
            elif (
                lock.is_particular_lock(m.chat.id, "anti_fwd_c") and m.forward_from_chat
            ):
                await delete_messages(c, m)
                return


@ky.ubot("locktypes", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    await m.reply_text(l_t)
    return


@ky.ubot("lock", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) < 2:
        await m.reply_text(f"{em.gagal} Gunakan format : `lock` type!")
        return
    lock_type = m.text.split(None, 1)[1]
    chat_id = m.chat.id

    if not lock_type:
        await m.reply_text(f"{em.gagal} Berikan argumen untuk dikunci!")
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
            await m.reply_text(
                f"{em.gagal} Sepertinya saya tidak mempunyai izin lebih!"
            )
        await m.reply_text(f"{em.sukses}" + "Terkunci <b>all</b> untuk grup ini!")
        ##await prevent_approved(m)
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
            await m.reply_text(f"{em.sukses} Sudah hidup!")
            return
        await m.reply_text(f"{em.sukses} Kirim link dikunci digrup ini!")
        return
    elif lock_type == "anonchannel":
        curr = lock.insert_lock_channel(m.chat.id, "anti_c_send")
        if not curr:
            await m.reply_text(f"{em.sukses} Sudah hidup!")
            return
        await m.reply_text(f"{em.sukses} Kirim sebagai channel dikunci digrup ini!")
        return
    elif lock_type == "forwardall":
        curr = lock.insert_lock_channel(m.chat.id, "anti_fwd")
        if not curr:
            await m.reply_text(f"{em.sukses} Sudah hidup!")
            return
        await m.reply_text(f"{em.sukses} Pesan terusan dikunci digrup ini!")
        return
    elif lock_type == "forwardu":
        curr = lock.insert_lock_channel(m.chat.id, "anti_fwd_u")
        if not curr:
            await m.reply_text(f"{em.sukses} Sudah hidup!")
            return
        await m.reply_text(f"{em.sukses} Pesan terusan pengguna dikunci digrup ini!")
        return
    elif lock_type == "forwardc":
        curr = lock.insert_lock_channel(m.chat.id, "anti_fwd_c")
        if not curr:
            await m.reply_text(f"{em.sukses} Sudah hidup!")
            return
        await m.reply_text(f"{em.sukses} Pesan terusan channel dikunci digrup ini!")
        return
    else:
        await m.reply_text(
            f"{em.gagal} Invalid Lock Tipe!\n\n{em.sukses} Silahkan ketik <code>locktypes</code> untuk melihat format lock!"
        )
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
        await m.reply_text(f"{em.gagal} Sepertinya saya tidak mempunyai izin lebih!")
    await m.reply_text(
        f"{em.sukses}" + f"Terkunci <b>{perm}</b> dalam grup ini.",
    )
    ##await prevent_approved(m)
    return


@ky.ubot("unlock", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) < 2:
        await m.reply_text(f"{em.gagal} Gunakan format : `lock` type!")
        return
    unlock_type = m.text.split(None, 1)[1]
    chat_id = m.chat.id

    if not unlock_type:
        await m.reply_text(f"{em.gagal} Berikan argumen untuk dibuka!")
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
            await m.reply_text(
                f"{em.gagal} Sepertinya saya tidak mempunyai izin lebih!"
            )
        await m.reply_text(f"{em.sukses}" + "Dibuka <b>all</b> untuk grup ini!")
        ##await prevent_approved(m)
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
            await m.reply_text(f"{em.sukses} Sudah dibuka!")
            return
        await m.reply_text(f"{em.sukses} Kirim sebagai channel dibuka digrup ini!")
        return
    elif unlock_type == "url":
        curr = lock.remove_lock_channel(m.chat.id, "anti_links")
        if curr:
            await m.reply_text(f"{em.sukses} Sudah dibuka!")
            return
        await m.reply_text(f"{em.sukses} Kirim link dibuka digrup ini!")
        return
    elif unlock_type == "forwardall":
        curr = lock.remove_lock_channel(m.chat.id, "anti_fwd")

        if not curr:
            await m.reply_text(f"{em.sukses} Sudah dibuka!")
            return
        await m.reply_text(f"{em.sukses} Semua pesan terusan dibuka digrup ini!")
        return

    elif unlock_type == "forwardu":
        curr = lock.remove_lock_channel(m.chat.id, "anti_fwd_u")

        if not curr:
            await m.reply_text(f"{em.sukses} Sudah dibuka!")
            return
        await m.reply_text(f"{em.sukses} Pesan terusan pengguna dibuka digrup ini!")
        return

    elif unlock_type == "forwardc":
        curr = lock.remove_lock_channel(m.chat.id, "anti_fwd_c")

        if not curr:
            await m.reply_text(f"{em.sukses} Sudah dibuka!")
            return
        await m.reply_text(f"{em.sukses} Pesan terusan channel dibuka digrup ini!")
        return

    else:
        await m.reply_text(
            f"{em.gagal} Invalid Unlock Tipe!\n\n{em.sukses} Silahkan ketik <code>locktypes</code> untuk melihat format lock!"
        )

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
        await m.reply_text(f"{em.gagal} Sepertinya saya tidak mempunyai izin lebih!")
    await m.reply_text(
        f"{em.sukses}" + f"Dibuka <b>{uperm}</b> dalam grup ini.",
    )
    ##await prevent_approved(m)
    return


@ky.ubot("locks", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    chkmsg = await m.reply_text(f"{em.proses} Processing...")
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
            await chkmsg.edit_text(f"{em.gagal} Terjadi kesalahan!")
            await m.reply_text(f"{em.gagal} Lapor ke @kynansupport :\n\n{e_f}")
    return
