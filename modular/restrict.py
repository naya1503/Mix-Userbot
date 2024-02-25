################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru || William Butcher
"""
################################################################

import asyncio
from time import time

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import DEVS, Emojik, ky, user
from Mix.core.parser import mention_html
from Mix.core.sender_tools import extract_user

__modles__ = "Group"
__help__ = """
Help Command Group 

• Perintah: <code>{0}purge</code> 
• Penjelasan: Untuk menghapus pesan keseluruhan dari pesan yg dibalas.

• Perintah: <code>{0}del</code> 
• Penjelasan: Untuk menghapus pesan.

• Perintah: <code>{0}report</code> 
• Penjelasan: Untuk melaporkan pengguna.

• Perintah: <code>{0}zombies</code>
• Penjelasan: Untuk mengeluarkan akun terhapus.

• Perintah: <code>{0}ban or delban</code>
• Penjelasan: Untuk memblokir pengguna.

• Perintah: <code>{0}kick or delkick</code>  
• Penjelasan: Untuk mengeluarkan pengguna.

• Perintah: <code>{0}mute or delmute</code> 
• Penjelasan: Untuk membisukan pengguna.

• Perintah: <code>{0}unmute</code>
• Penjelasan: Untuk menyuarakan pengguna.

• Perintah: <code>{0}unban</code>
• Penjelasan: Untuk melepas blokir pengguna.

• Perintah: <code>{0}promote</code>  
• Penjelasan: Untuk mengangkat admin.

• Perintah: <code>{0}fullpromote</code> 
• Penjelasan: Untuk mengangkat wakil pendiri.

• Perintah: <code>{0}demote</code>
• Penjelasan: Untuk menurunkan seorang admin.

• Perintah: <code>{0}title</code>
• Penjelasan: Untuk mengubah titel pengguna.

• Perintah: <code>{0}gctitle</code> 
• Penjelasan: Untuk mengubah nama grup.

• Perintah: <code>{0}gcdes</code>
• Penjelasan: Untuk mengubah deskripsi grup.

• Perintah: <code>{0}gcpic</code>
• Penjelasan: Untuk mengubah foto grup.

• Perintah: <code>{0}getlink or invitelink</code>
• Penjelasan: Untuk mengambil tautan grup.

• Perintah: <code>{0}pin or unpin</code>
• Penjelasan: Untuk menyematkan pesan atau melepas sematan grup.
"""


async def member_permissions(chat: int, org: int):
    perms = []
    member = (await user.get_chat_member(chat, org)).privileges
    if not member:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_video_chats:
        perms.append("can_manage_video_chats")
    return perms


admins_in_chat = {}


async def list_admins(chat: int):
    global admins_in_chat
    if chat in admins_in_chat:
        interval = time() - admins_in_chat[chat]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat]["data"]

    admins_in_chat[chat] = {
        "last_updated_at": time(),
        "data": [
            i.user.id
            async for i in user.get_chat_members(
                chat, filter=enums.ChatMembersFilter.ADMINISTRATORS
            )
        ],
    }
    return admins_in_chat[chat]["data"]


@ky.ubot("purge", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    repliedmsg = m.reply_to_message
    await m.delete()

    if not repliedmsg:
        return await m.reply_text(f"{em.gagal} Silahkan balas ke pesan untuk dihapus.")

    cmd = m.command
    if len(cmd) > 1 and cmd[1].isdigit():
        purge_to = repliedmsg.id + int(cmd[1])
        if purge_to > m.id:
            purge_to = m.id
    else:
        purge_to = m.id

    chat_id = m.chat.id
    message_ids = []

    for message_id in range(
        repliedmsg.id,
        purge_to,
    ):
        message_ids.append(message_id)

        if len(message_ids) == 100:
            await c.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            message_ids = []

    if len(message_ids) > 0:
        await c.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )


@ky.ubot("kick|delkick", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id, reason = await c.extract_user_and_reason(m)
    if not user_id:
        return await m.reply_text(f"{em.gagal} Saya tidak dapat menemukan pengguna.")
    if user_id == c.me.id:
        return await m.reply_text(f"{em.gagal} Oh anda ingin menendang diri sendiri ?")
    if user_id in DEVS:
        return await m.reply_text(
            f"{em.gagal} Oh anda ingin menendang Developer Mix-Userbot ?"
        )
    if user_id in (await list_admins(m.chat.id)):
        return await m.reply_text(f"{em.gagal} Tidak dapat menendang admin!")
    mention = (await c.get_users(user_id)).mention
    msg = f"""
{em.profil} **Kicked User:** {mention}
{em.warn} **Kicked By:** {m.from_user.mention if m.from_user else 'Anon'}
{em.block} **Reason:** {reason or 'No Reason Provided.'}"""
    if m.command[0][0] == "d":
        await m.reply_to_message.delete()
        await m.delete()
    await m.chat.ban_member(user_id)
    await m.reply_text(msg)
    await asyncio.sleep(1)
    await m.chat.unban_member(user_id)


@ky.ubot("ban|delban", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id, reason = await c.extract_user_and_reason(m)

    if not user_id:
        return await m.reply_text(f"{em.gagal} Saya tidak dapat menemukan pengguna.")
    if user_id == c.me.id:
        return await m.reply_text(f"{em.gagal} Oh anda ingin memblokir diri sendiri ?")
    if user_id in DEVS:
        return await m.reply_text(
            f"{em.gagal} Oh anda ingin memblokir Developer Mix-Userbot ?"
        )
    if user_id in (await list_admins(m.chat.id)):
        return await m.reply_text(f"{em.gagal} Tidak dapat memblokir admin!")
    try:
        mention = (await c.get_users(user_id)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    msg = (
        f"{em.profil} **Banned User:** {mention}\n"
        f"{em.block} **Banned By:** {m.from_user.mention if m.from_user else 'Anon'}\n"
    )
    if m.command[0][0] == "d":
        await m.reply_to_message.delete()
        await m.delete()
    if reason:
        msg += f"{em.warn} **Reason:** {reason}"
    await m.chat.ban_member(user_id)
    await m.reply_text(msg)
    # await msg.delete()


@ky.ubot("unban", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    reply = m.reply_to_message

    if reply and reply.sender_chat and reply.sender_chat != m.chat.id:
        return await m.reply_text(f"{em.gagal} Pengguna tidak diketahui!")
    if len(m.command) == 2:
        user = m.text.split(None, 1)[1]
    elif len(m.command) == 1 and reply:
        user = m.reply_to_message.from_user.id
    else:
        return await m.reply_text(f"{em.gagal} Berikan username atau userid pengguna!")
    await m.chat.unban_member(user)
    umention = (await c.get_users(user)).mention
    await m.reply_text(f"{em.sukses} Unbanned! {umention}")


@ky.ubot("del", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(f"{em.gagal} Silahkan balas ke pesan!")
    await m.reply_to_message.delete()
    await m.delete()


@ky.ubot("pin|unpin", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(f"{em.gagal} Silahkan balas ke pesan!")
    r = m.reply_to_message
    if m.command[0][0] == "u":
        await r.unpin()
        return await m.reply_text(
            f"{em.sukses} **Sematan dilepas [pesan]({r.link}).**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await m.reply(
        f"{em.sukses} **Berhasil disematkan [pesan]({r.link}) m.**",
        disable_web_page_preview=True,
    )


@ky.ubot("mute|delmute", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id, reason = await c.extract_user_and_reason(m)
    if not user_id:
        return await m.reply_text(f"{em.gagal} Saya tidak dapat menemukan pengguna.")
    if user_id == c.me.id:
        return await m.reply_text(f"{em.gagal} Oh anda ingin membisukan diri sendiri ?")
    if user_id in DEVS:
        return await m.reply_text(
            f"{em.gagal} Oh anda ingin membisukan Developer Mix-Userbot ?"
        )
    if user_id in (await list_admins(m.chat.id)):
        return await m.reply_text(f"{em.gagal} Tidak dapat membisukan admin!")
    mention = (await c.get_users(user_id)).mention
    msg = (
        f"{em.profil} **Muted User:** {mention}\n"
        f"{em.block} **Muted By:** {m.from_user.mention if m.from_user else 'Anon'}\n"
    )
    if m.command[0][0] == "d":
        await m.reply_to_message.delete()
        await m.delete()
    if reason:
        msg += f"{em.warn} **Reason:** {reason}"
    try:
        await m.chat.restrict_member(user_id, permissions=ChatPermissions())
        await m.reply_text(msg)
    except ChatAdminRequired:
        await m.reply_text(f"{em.gagal} Saya bukan admin!")
    except RightForbidden:
        await m.reply_text(f"{em.gagal} Saya tidak mempunyai izin!")
    except UserAdminInvalid:
        await m.reply_text(f"{em.gagal} Pengguna invalid!")
    except RPCError as e:
        await m.reply_text(
            f"{em.gagal} Pengguna tidak pernah berinteraksi dengan anda!\n\n Laporke @KynanSupport : {e}"
        )
    except Exception as e:
        await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
    return


@ky.ubot("unmute", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id = await c.extract_user(m)
    if not user_id:
        return await m.reply_text(f"{em.gagal} Saya tidak dapat menemukan pengguna.")
    try:
        await m.chat.unban_member(user_id)
        umention = (await c.get_users(user_id)).mention
        await m.reply_text(f"Unmuted! {umention}")
    except ChatAdminRequired:
        await m.reply_text(f"{em.gagal} Saya bukan admin!")
    except RightForbidden:
        await m.reply_text(f"{em.gagal} Saya tidak mempunyai izin!")
    except UserAdminInvalid:
        await m.reply_text(f"{em.gagal} Pengguna invalid!")
    except RPCError as e:
        await m.reply_text(
            f"{em.gagal} Pengguna tidak pernah berinteraksi dengan anda!\n\n Laporke @KynanSupport : {e}"
        )
    except Exception as e:
        await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
    return


@ky.ubot("zombies", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    chat_id = m.chat.id
    deleted_users = []
    banned_users = 0
    m = await m.reply(f"{em.proses} Mencari akun terhapus...")

    async for i in c.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                await m.chat.ban_member(deleted_user)
            except Exception:
                pass
            banned_users += 1
        await m.edit(
            f"{em.sukses} Berhasil mengeluarkan `{banned_users}` akun terhapus."
        )
    else:
        await m.edit(f"{em.gagal} Tidak ada akun terhapus disini!")


@ky.ubot("getlink|invitelink", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        link = (await c.get_chat(m.chat.id)).invite_link
        if not link:
            link = await c.export_chat_invite_link(m.chat.id)
        text = f"{em.sukses} **Ini adalah link invite grup :**\n\n{link}"
        if m.reply_to_message:
            await m.reply_to_message.reply_text(text, disable_web_page_preview=True)
        else:
            await m.reply_text(text, disable_web_page_preview=True)


@ky.ubot("report", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(
            f"{em.gagal} Silahkan balas ke pesan untuk dilaporkan ke admin!"
        )

    reply = m.reply_to_message
    reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
    user_id = m.from_user.id if m.from_user else m.sender_chat.id
    if reply_id == user_id:
        return await m.reply_text(f"{em.gagal} Kenapa harus melaporkan diri sendiri?")

    list_of_admins = await list_admins(m.chat.id)
    linked_chat = (await c.get_chat(m.chat.id)).linked_chat
    if linked_chat is not None:
        if (
            reply_id in list_of_admins
            or reply_id == m.chat.id
            or reply_id == linked_chat.id
        ):
            return await m.reply_text(f"{em.gagal} Dia adalah admin!")
    else:
        if reply_id in list_of_admins or reply_id == m.chat.id:
            return await m.reply_text(f"{em.gagal} Dia adalah admin!")

    user_mention = (
        reply.from_user.mention if reply.from_user else reply.sender_chat.title
    )
    text = f"{em.warn} **Dilaporkan {user_mention} ke admin!**"
    admin_data = [
        i
        async for i in c.get_chat_members(
            chat_id=m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
        )
    ]  # will it give floods ???
    for admin in admin_data:
        if admin.user.is_bot or admin.user.is_deleted:
            # return bots or deleted admins
            continue
        text += f"[\u2063](tg://user?id={admin.user.id})"

    await m.reply_to_message.reply_text(text)


@ky.ubot("fullpromote", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(f"{em.gagal} Berikan username atau userid pengguna!")
        return
    try:
        user_id, user_first_name, user_name = await extract_user(c, m)
    except Exception:
        return
    bot = await c.get_chat_member(m.chat.id, c.me.id)
    if user_id == c.me.id:
        await m.reply_text(f"{em.gagal} Anda sudah admin!")
        return
    if not bot.privileges.can_promote_members:
        await m.reply_text(f"{em.gagal} Saya tidak mempunyai izin!")
        return
    await c.get_chat_member(m.chat.id, m.from_user.id)
    try:
        admin_list = await list_admins(m.chat.id)
    except KeyError:
        return
    if user_id in admin_list:
        await m.reply_text(f"{em.gagal} Pengguna adalah admin!!")
        return
    try:
        await m.chat.promote_member(user_id=user_id, privileges=bot.privileges)
        title = ""
        if m.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            title = "Babu"  # Default fullpromote title
            if len(m.text.split()) == 3 and not m.reply_to_message:
                title = " ".join(m.text.split()[2:16])  # trim title to 16 characters
            elif len(m.text.split()) >= 2 and m.reply_to_message:
                title = " ".join(m.text.split()[1:16])  # trim title to 16 characters

            try:
                await c.set_administrator_title(m.chat.id, user_id, title)
            except RPCError as e:
                await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
            except Exception as e:
                await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
        await m.reply_text(
            "{e1} {promoter}\n{e2} Pengguna {promoted} berhasil diangkat menjadi fulladmin!"
        ).format(
            e1=em.profil,
            promoter=(await mention_html(m.from_user.first_name, m.from_user.id)),
            e2=em.warn,
            promoted=(await mention_html(user_first_name, user_id)),
        )
    except ChatAdminRequired:
        await m.reply_text(f"{em.gagal} Saya bukan admin!")
    except RightForbidden:
        await m.reply_text(f"{em.gagal} Saya tidak mempunyai izin!")
    except UserAdminInvalid:
        await m.reply_text(f"{em.gagal} Pengguna invalid!")
    except RPCError as e:
        await m.reply_text(
            f"{em.gagal} Pengguna tidak pernah berinteraksi dengan anda!\n\n Laporke @KynanSupport : {e}"
        )
    except Exception as e:
        await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
    return


@ky.ubot("promote", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(f"{em.gagal} Berikan username atau userid pengguna!")
        return
    try:
        user_id, user_first_name, user_name = await extract_user(c, m)
    except Exception:
        return
    bot = await c.get_chat_member(m.chat.id, c.me.id)
    if user_id == c.me.id:
        await m.reply_text(f"{em.gagal} Anda sudah admin!")
        return
    if not bot.privileges.can_promote_members:
        await m.reply_text(f"{em.gagal} Saya tidak mempunyai izin!")
        return
    try:
        admin_list = await list_admins(m.chat.id)
    except KeyError:

        return
    if user_id in admin_list:
        await m.reply_text(f"{em.gagal} Pengguna adalah admin!!")
        return
    try:
        await m.chat.promote_member(
            user_id=user_id,
            privileges=ChatPrivileges(
                can_invite_users=bot.privileges.can_invite_users,
                can_delete_messages=bot.privileges.can_delete_messages,
                can_restrict_members=bot.privileges.can_restrict_members,
                can_manage_chat=bot.privileges.can_manage_chat,
                can_manage_video_chats=bot.privileges.can_manage_video_chats,
            ),
        )
        title = ""
        if m.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            title = "Ini Babu"  # Deafult title
            if len(m.text.split()) >= 3 and not m.reply_to_message:
                title = " ".join(m.text.split()[2:16])  # trim title to 16 characters
            elif len(m.text.split()) >= 2 and m.reply_to_message:
                title = " ".join(m.text.split()[1:16])  # trim title to 16 characters
            try:
                await c.set_administrator_title(m.chat.id, user_id, title)
            except RPCError as e:
                await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
            except Exception as e:
                await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
        promoter = (await mention_html(m.from_user.first_name, m.from_user.id))
        promoted = (await mention_html(user_first_name, user_id))
        await m.reply_text(
            f"{em.profil} {promoter}\n{em.warn} Pengguna {promoted} berhasil diangkat menjadi admin!"
        )
    except ChatAdminRequired:
        await m.reply_text(f"{em.gagal} Saya bukan admin!")
    except RightForbidden:
        await m.reply_text(f"{em.gagal} Saya tidak mempunyai izin!")
    except UserAdminInvalid:
        await m.reply_text(f"{em.gagal} Pengguna invalid!")
    except RPCError as e:
        await m.reply_text(
            f"{em.gagal} Pengguna tidak pernah berinteraksi dengan anda!\n\n Laporke @KynanSupport : {e}"
        )
    except Exception as e:
        await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
    return


@ky.ubot("demote", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(f"{em.gagal} Berikan username atau userid pengguna!")
        return
    try:
        user_id, user_first_name, _ = await extract_user(c, m)
    except Exception:
        return
    if user_id == c.me.id:
        await m.reply_text(f"{em.gagal} Cari pendiri grup dan turunkan anda.")
        return
    botol = await member_permissions(m.chat.id, user_id)
    if not botol:
        await m.reply_text(f"{em.gagal} Pengguna bukan admin!")
        return
    try:
        await m.chat.promote_member(
            user_id=user_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
            ),
        )
        demoter = (await mention_html(m.from_user.first_name, m.from_user.id))
        demoted = (await mention_html(user_first_name, user_id))
        await m.reply_text(
            f"{em.profil} {demoter}\n{em.warn} Pengguna {demoted} berhasil diturunkan admin!")
    except BotChannelsNa:
        await m.reply_text(f"{em.gagal} Pengguna tidak diangkat oleh saya!")
    except ChatAdminRequired:
        await m.reply_text(f"{em.gagal} Saya bukan admin!")
    except RightForbidden:
        await m.reply_text(f"{em.gagal} Saya tidak mempunyai izin!")
    except UserAdminInvalid:
        await m.reply_text(f"{em.gagal} Pengguna invalid!")
    except RPCError as e:
        await m.reply_text(
            f"{em.gagal} Pengguna tidak pernah berinteraksi dengan anda!\n\n Laporke @KynanSupport : {e}"
        )
    except Exception as e:
        await m.reply_text(f"{em.gagal} Laporke @KynanSupport : {e}")
    return


@ky.ubot("gctitle", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(f"{em.gagal} Berikan teks atau balas pesan!")
        return
    if m.reply_to_message:
        gtit = m.reply_to_message.text
    else:
        gtit = m.text.split(None, 1)[1]
    try:
        await m.chat.set_title(gtit)
    except Exception as e:
        return await m.reply_text(f"{em.gagal} Error: {e}")
    return await m.reply_text(
        f"{em.sukses} Berhasil mengubah nama Grup {m.chat.title} menjadi {gtit}",
    )


@ky.ubot("gcdes", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(f"{em.gagal} Berikan teks atau balas pesan!")
        return
    if m.reply_to_message:
        desp = m.reply_to_message.text
    else:
        desp = m.text.split(None, 1)[1]
    try:
        await m.chat.set_description(desp)
    except Exception as e:
        return await m.reply_text(f"{em.gagal} Error: {e}")
    return await m.reply_text(
        f"{em.sukses} Berhasil mengubah deskripsi grup {m.chat.description} menjadi {desp}!",
    )


@ky.ubot("title", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        return await m.reply_text(
            f"{em.gagal} Balas pengguna atau berikan username pengguna!"
        )
    if m.reply_to_message:
        if len(m.text.split()) >= 2:
            reason = m.text.split(None, 1)[1]
    else:
        if len(m.text.split()) >= 3:
            reason = m.text.split(None, 2)[2]
    try:
        user_id, _, _ = await extract_user(c, m)
    except Exception:
        return
    if not user_id:
        return await m.reply_text(f"{em.gagal} Tidak dapat menemukan pengguna!")
    if user_id == c.me.id:
        return await m.reply_text(f"{em.gagal} Kenapa harus saya?")
    if not reason:
        return await m.reply_text(f"{em.gagal} Berikan title untuk pengguna!")
    from_user = await c.get_users(user_id)
    title = reason
    try:
        await c.set_administrator_title(m.chat.id, from_user.id, title)
    except Exception as e:
        return await m.reply_text(f"{em.gagal} Error: {e}")
    except UserCreator:
        return await m.reply_text(f"{em.gagal} Dia adalah pemilik grup ini!")
    return await m.reply_text(
        f"{em.sukses} Berhasil mengubah title pengguna {from_user.mention} menjadi {title}",
    )


@ky.ubot("gcpic", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(f"{em.gagal} Balas ke media!")
    if (
        not m.reply_to_message.photo
        and not m.reply_to_message.document
        and not m.reply_to_message.video
    ):
        return await m.reply_text(f"{em.gaga} Balas ke media!")

    if m.reply_to_message:
        if m.reply_to_message.photo:
            await c.set_chat_photo(m.chat.id, photo=m.reply_to_message.photo.file_id)
            await m.reply_text(f"{em.sukses} Foto grup berhasil diubah!")
        if m.reply_to_message.document:
            await c.set_chat_photo(m.chat.id, photo=m.reply_to_message.document.file_id)
            await m.reply_text(
                f"{em.sukses} Berhasil mengubah dokumen menjadi foto grup!"
            )
        elif m.reply_to_message.video:
            await c.set_chat_photo(m.chat.id, video=m.reply_to_message.video.file_id)
            await m.reply_text(
                f"{em.sukses} Berhasil mengubah video menjadi foto grup!"
            )
    else:
        return await m.reply_text(f"{em.gaga} Balas ke media!")
