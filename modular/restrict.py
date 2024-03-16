################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru || William Butcher
"""
################################################################

import asyncio
from time import time

from hydrogram import *
from hydrogram.enums import *
from hydrogram.errors import *
from hydrogram.types import *

from Mix import DEVS, Emojik, cgr, get_cgr, ky, nlx
from Mix.core.parser import mention_html
from Mix.core.sender_tools import extract_nlx

__modles__ = "Restrict"
__help__ = get_cgr("help_rest")


async def member_permissions(chat: int, org: int):
    perms = []
    member = (await nlx.get_chat_member(chat, org)).privileges
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
    if member.can_invite_nlxs:
        perms.append("can_invite_nlxs")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_video_chats:
        perms.append("can_manage_video_chats")
    return perms


admins_in_chat = {}


async def list_admins(m):
    global admins_in_chat
    if m.chat.id in admins_in_chat:
        interval = time() - admins_in_chat[m.chat.id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[m.chat.id]["data"]

    admins_in_chat[m.chat.id] = {
        "last_updated_at": time(),
        "data": [
            mek.nlx.id
            async for mek in nlx.get_chat_members(
                m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
            )
        ],
    }
    return admins_in_chat[m.chat.id]["data"]


@ky.ubot("purge", sudo=True)
async def _(c: nlx, m):
    await m.delete()
    if not m.reply_to_message:
        return
    chat_id = m.chat.id
    message_ids = []
    for message_id in range(
        m.reply_to_message.id,
        m.id,
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
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nlx_id, reason = await c.extract_nlx_and_reason(m)
    if not nlx_id:
        return await m.reply_text(cgr("glbl_2").format(em.gagal))
    if nlx_id == c.me.id:
        return await m.reply_text(cgr("res_1").format(em.gagal))
    if nlx_id in DEVS:
        return await m.reply_text(cgr("glbl_3").format(em.gagal))
    mention = (await c.get_nlxs(nlx_id)).mention
    msg = cgr("res_2").format(
        em.profil,
        mention,
        em.warn,
        m.from_nlx.mention if m.from_nlx else "Anon",
        em.block,
        reason or "No Reason Provided.",
    )
    if m.command[0][0] == "d":
        await m.reply_to_message.delete()
        await m.delete()
    try:
        await m.chat.ban_member(nlx_id)
    except UserAdminInvalid:
        return await m.reply_text(cgr("res_3").format(em.gagal))
    await m.reply_text(msg)
    await asyncio.sleep(1)
    await m.chat.unban_member(nlx_id)
    return


@ky.ubot("ban|delban", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nlx_id, reason = await c.extract_nlx_and_reason(m)

    if not nlx_id:
        return await m.reply_text(cgr("glbl_2").format(em.gagal))
    if nlx_id == c.me.id:
        return await m.reply_text(cgr("res_4").format(em.gagal))
    if nlx_id in DEVS:
        return await m.reply_text(cgr("glbl_3").format(em.gagal))
    try:
        mention = (await c.get_nlxs(nlx_id)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    msg = cgr("res_5").format(
        em.profil,
        mention,
        em.warn,
        m.from_nlx.mention if m.from_nlx else "Anon",
        em.block,
        reason or "No Reason Provided.",
    )
    if m.command[0][0] == "d":
        await m.reply_to_message.delete()
        await m.delete()
    try:
        await m.chat.ban_member(nlx_id)
    except UserAdminInvalid:
        return await m.reply_text(cgr("res_3").format(em.gagal))
    await m.reply_text(msg)
    return


@ky.ubot("unban", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    reply = m.reply_to_message

    if reply and reply.sender_chat and reply.sender_chat != m.chat.id:
        return await m.reply_text(cgr("res_3").format(em.gagal))
    if len(m.command) == 2:
        nlx = m.text.split(None, 1)[1]
    elif len(m.command) == 1 and reply:
        nlx = m.reply_to_message.from_nlx.id
    else:
        return await m.reply_text(cgr("prof_1").format(em.gagal))
    await m.chat.unban_member(nlx)
    umention = (await c.get_nlxs(nlx)).mention
    await m.reply_text(cgr("res_6").format(em.sukses, umention))
    return


async def delete_reply(c, message):
    if message:
        await message.delete()


@ky.ubot("del", sudo=True)
async def _(c: nlx, m):
    if m.reply_to_message:
        await delete_reply(c, m.reply_to_message)
        await m.delete()
    else:
        await m.delete()


@ky.ubot("pin|unpin", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(cgr("res_7").format(em.gagal))
    r = m.reply_to_message
    if m.command[0][0] == "u":
        await r.unpin()
        return await m.reply_text(
            cgr("res_8").format(em.sukses, r.link), disable_web_page_preview=True
        )
    await r.pin(disable_notification=True)
    await m.reply(cgr("res_9").format(em.sukses, r.link), disable_web_page_preview=True)


@ky.ubot("mute|delmute", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nlx_id, reason = await c.extract_nlx_and_reason(m)
    if not nlx_id:
        return await m.reply_text(cgr("glbl_2").format(em.gagal))
    if nlx_id == c.me.id:
        return await m.reply_text(cgr("res_10").format(em.gagal))
    if nlx_id in DEVS:
        return await m.reply_text(cgr("glbl_3").format(em.gagal))
    mention = (await c.get_nlxs(nlx_id)).mention
    msg = cgr("res_11").format(
        em.profil,
        mention,
        em.warn,
        m.from_nlx.mention if m.from_nlx else "Anon",
        em.block,
        reason or "No Reason Provided.",
    )
    if m.command[0][0] == "d":
        await m.reply_to_message.delete()
        await m.delete()
    try:
        await m.chat.restrict_member(nlx_id, permissions=ChatPermissions())
        await m.reply_text(msg)
    except ChatAdminRequired:
        await m.reply_text(cgr("res_12").format(em.gagal))
    except RightForbidden:
        await m.reply_text(cgr("res_13").format(em.gagal))
    except UserAdminInvalid:
        return await m.reply_text(cgr("res_3").format(em.gagal))
    except RPCError:
        pass
    except Exception as e:
        await m.reply_text(cgr("err").format(em.gagal, e))
    return


@ky.ubot("unmute", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nlx_id = await c.extract_nlx(m)
    if not nlx_id:
        return await m.reply_text(cgr("glbl_2").format(em.gagal))
    try:
        await m.chat.unban_member(nlx_id)
        umention = (await c.get_nlxs(nlx_id)).mention
        await m.reply_text(cgr("res_14").format(em.sukses, umention))
    except ChatAdminRequired:
        await m.reply_text(cgr("res_12").format(em.gagal))
    except RightForbidden:
        await m.reply_text(cgr("res_13").format(em.gagal))
    except UserAdminInvalid:
        return await m.reply_text(cgr("res_3").format(em.gagal))
    except RPCError:
        pass
    except Exception as e:
        await m.reply_text(cgr("err").format(em.gagal, e))
    return


@ky.ubot("zombies", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    chat_id = m.chat.id
    deleted_nlxs = []
    banned_nlxs = 0
    m = await m.reply(cgr("proses").format(em.proses))

    async for i in c.get_chat_members(chat_id):
        if i.nlx.is_deleted:
            deleted_nlxs.append(i.nlx.id)
    if len(deleted_nlxs) > 0:
        for deleted_nlx in deleted_nlxs:
            try:
                await m.chat.ban_member(deleted_nlx)
            except Exception:
                pass
            banned_nlxs += 1
        await m.edit(cgr("res_15").format(em.sukses, banned_nlxs))
        return
    else:
        await m.edit(cgr("res_16").format(em.gagal))
        return


@ky.ubot("getlink|invitelink", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        link = (await c.get_chat(m.chat.id)).invite_link
        if not link:
            link = await c.export_chat_invite_link(m.chat.id)
        text = cgr("res_17").format(em.sukses, link)
        if m.reply_to_message:
            await m.reply_to_message.reply_text(text, disable_web_page_preview=True)
        else:
            await m.reply_text(text, disable_web_page_preview=True)


@ky.ubot("report", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(cgr("res_18").format(em.gagal))

    reply = m.reply_to_message
    reply_id = reply.from_nlx.id if reply.from_nlx else reply.sender_chat.id
    nlx_id = m.from_nlx.id if m.from_nlx else m.sender_chat.id
    if reply_id == nlx_id:
        return await m.reply_text(cgr("res_19").format(em.gagal))

    list_of_admins = await member_permissions(m.chat.id, nlx_id)
    linked_chat = (await c.get_chat(m.chat.id)).linked_chat
    if linked_chat is not None:
        if list_of_admins or reply_id == m.chat.id or reply_id == linked_chat.id:
            return await m.reply_text(cgr("res_20").format(em.gagal))
    else:
        if list_of_admins or reply_id == m.chat.id:
            return await m.reply_text(cgr("res_20").format(em.gagal))

    nlx_mention = reply.from_nlx.mention if reply.from_nlx else reply.sender_chat.title
    text = cgr("res_21").format(em.warn, nlx_mention)
    admin_data = [
        i
        async for i in c.get_chat_members(
            chat_id=m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
        )
    ]  # will it give floods ???
    for admin in admin_data:
        if admin.nlx.is_bot or admin.nlx.is_deleted:
            # return bots or deleted admins
            continue
        text += f"[\u2063](tg://nlx?id={admin.nlx.id})"

    await m.reply_to_message.reply_text(text)


@ky.ubot("fullpromote", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(cgr("prof_1").format(em.gagal))
        return
    try:
        nlx_id, nlx_first_name, nlx_name = await extract_nlx(c, m)
    except Exception:
        return
    bot = await c.get_chat_member(m.chat.id, c.me.id)
    if nlx_id == c.me.id:
        await m.reply_text(cgr("res_22").format(em.gagal))
        return
    if not bot.privileges.can_promote_members:
        await m.reply_text(cgr("res_13").format(em.gagal))
        return
    try:
        await m.chat.promote_member(nlx_id=nlx_id, privileges=bot.privileges)
        title = ""
        if m.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            title = "Babu"  # Default fullpromote title
            if len(m.text.split()) == 3 and not m.reply_to_message:
                title = " ".join(m.text.split()[2:16])  # trim title to 16 characters
            elif len(m.text.split()) >= 2 and m.reply_to_message:
                title = " ".join(m.text.split()[1:16])  # trim title to 16 characters

            await c.set_administrator_title(m.chat.id, nlx_id, title)
        promoter = await mention_html(m.from_nlx.first_name, m.from_nlx.id)
        promoted = await mention_html(nlx_first_name, nlx_id)
        await m.reply_text(cgr("res_23").format(em.profil, promoter, em.warn, promoted))

    except ChatAdminRequired:
        await m.reply_text(cgr("res_12").format(em.gagal))
    except UserAdminInvalid:
        await m.reply_text(cgr("res_3").format(em.gagal))
    except RPCError:
        pass
    except Exception as e:
        await m.reply_text(cgr("err").format(em.gagal), e)
    return


@ky.ubot("promote", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(cgr("prof_1").format(em.gagal))
        return
    try:
        nlx_id, nlx_first_name, nlx_name = await extract_nlx(c, m)
    except Exception:
        return
    bot = await c.get_chat_member(m.chat.id, c.me.id)
    if nlx_id == c.me.id:
        await m.reply_text(cgr("res_22").format(em.gagal))
        return
    if not bot.privileges.can_promote_members:
        await m.reply_text(cgr("res_13").format(em.gagal))
        return
    try:
        await m.chat.promote_member(
            nlx_id=nlx_id,
            privileges=ChatPrivileges(
                can_invite_nlxs=bot.privileges.can_invite_nlxs,
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
            await c.set_administrator_title(m.chat.id, nlx_id, title)
        promoter = await mention_html(m.from_nlx.first_name, m.from_nlx.id)
        promoted = await mention_html(nlx_first_name, nlx_id)
        await m.reply_text(cgr("res_24").format(em.profil, promoter, em.warn, promoted))

    except ChatAdminRequired:
        await m.reply_text(cgr("res_12").format(em.gagal))
    except UserAdminInvalid:
        await m.reply_text(cgr("res_3").format(em.gagal))
    except RPCError:
        pass
    except Exception as e:
        await m.reply_text(cgr("err").format(em.gagal), e)
    return


@ky.ubot("demote", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(cgr("prof_1").format(em.gagal))
        return
    try:
        nlx_id, nlx_first_name, _ = await extract_nlx(c, m)
    except Exception:
        return
    if nlx_id == c.me.id:
        await m.reply_text(cgr("res_19").format(em.gagal))
        return
    botol = await member_permissions(m.chat.id, nlx_id)
    if not botol:
        await m.reply_text(cgr("res_25").format(em.gagal))
        return
    try:
        await m.chat.promote_member(
            nlx_id=nlx_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_nlxs=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
            ),
        )
        demoter = await mention_html(m.from_nlx.first_name, m.from_nlx.id)
        demoted = await mention_html(nlx_first_name, nlx_id)
        await m.reply_text(cgr("res_26").format(em.profil, demoter, em.warn, demoted))
    except BotChannelsNa:
        await m.reply_text(cgr("res_27").format(em.gagal))
    except ChatAdminRequired:
        await m.reply_text(cgr("res_12").format(em.gagal))
    except UserAdminInvalid:
        await m.reply_text(cgr("res_3").format(em.gagal))
    except RPCError:
        pass
    except Exception as e:
        await m.reply_text(cgr("err").format(em.gagal, e))
    return


@ky.ubot("gctitle", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(cgr("gcs_1").format(em.gagal))
        return
    if m.reply_to_message:
        gtit = m.reply_to_message.text
    else:
        gtit = m.text.split(None, 1)[1]
    try:
        await m.chat.set_title(gtit)
    except Exception as e:
        return await m.reply_text(cgr("err").format(em.gagal), e)
    return await m.reply_text(cgr("res_28").format(em.sukses, m.chat.title, gtit))


@ky.ubot("gcdes", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text(cgr("gcs_1").format(em.gagal))
        return
    if m.reply_to_message:
        desp = m.reply_to_message.text
    else:
        desp = m.text.split(None, 1)[1]
    try:
        await m.chat.set_description(desp)
    except Exception as e:
        return await m.reply_text(cgr("err").format(em.gagal), e)
    return await m.reply_text(cgr("res_29").format(em.sukses, m.chat.description, desp))


@ky.ubot("title", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        return await m.reply_text(cgr("prof_1").format(em.gagal))
    if m.reply_to_message:
        if len(m.text.split()) >= 2:
            reason = m.text.split(None, 1)[1]
    else:
        if len(m.text.split()) >= 3:
            reason = m.text.split(None, 2)[2]
    try:
        nlx_id, _, _ = await extract_nlx(c, m)
    except Exception:
        return
    if not nlx_id:
        return await m.reply_text(cgr("glbl_2").format(em.gagal))
    if nlx_id == c.me.id:
        return await m.reply_text(cgr("res_19").format(em.gagal))
    if not reason:
        return await m.reply_text(cgr("res_30").format(em.gagal))
    from_nlx = await c.get_nlxs(nlx_id)
    title = reason
    try:
        await c.set_administrator_title(m.chat.id, from_nlx.id, title)
    except Exception as e:
        return await m.reply_text(cgr("err").format(em.gagal), e)
    except UserCreator:
        return await m.reply_text(cgr("res_31").format(em.gagal))
    return await m.reply_text(cgr("res_32").format(em.sukses, from_nlx.mention, title))


@ky.ubot("gcpic", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(cgr("res_33").format(em.gagal))
    if (
        not m.reply_to_message.photo
        and not m.reply_to_message.document
        and not m.reply_to_message.video
    ):
        return await m.reply_text(cgr("res_33").format(em.gagal))

    if m.reply_to_message:
        if m.reply_to_message.photo:
            await c.set_chat_photo(m.chat.id, photo=m.reply_to_message.photo.file_id)
            await m.reply_text(cgr("res_34").format(em.sukses))
        if m.reply_to_message.document:
            await c.set_chat_photo(m.chat.id, photo=m.reply_to_message.document.file_id)
            await m.reply_text(cgr("res_35").format(em.sukses))
        elif m.reply_to_message.video:
            await c.set_chat_photo(m.chat.id, video=m.reply_to_message.video.file_id)
            await m.reply_text(cgr("res_36").format(em.sukses))
    else:
        return await m.reply_text(cgr("res_33").format(em.gagal))
