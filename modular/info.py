################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

import os
from asyncio import sleep
from datetime import datetime
from traceback import format_exc

from hydrogram.enums import *
from hydrogram.errors import *
from hydrogram.raw.functions.channels import GetFullChannel
from hydrogram.raw.functions.users import GetFullUser
from team.nandev.class_log import LOGGER

from Mix import *
from Mix.core.sender_tools import extract_user

gban_db = GBan()

__modles__ = "Info"
__help__ = get_cgr("help_info")


async def count(c: user, chat):
    em = Emojik()
    em.initialize()
    try:
        administrator = []
        async for admin in c.get_chat_members(
            chat_id=chat, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            administrator.append(admin)
        total_admin = administrator
        bot = []
        async for tbot in c.get_chat_members(
            chat_id=chat, filter=ChatMembersFilter.BOTS
        ):
            bot.append(tbot)

        total_bot = bot
        bot_admin = 0
        ban = []
        async for banned in c.get_chat_members(chat, filter=ChatMembersFilter.BANNED):
            ban.append(banned)

        total_banned = ban
        for x in total_admin:
            for y in total_bot:
                if x == y:
                    bot_admin += 1
        total_admin = len(total_admin)
        total_bot = len(total_bot)
        total_banned = len(total_banned)
        return total_bot, total_admin, bot_admin, total_banned
    except Exception:
        total_bot = total_admin = bot_admin = total_banned = cgr("info_1").format(
            em.gagal
        )

    return total_bot, total_admin, bot_admin, total_banned


async def user_info(c, sus, already=False):
    em = Emojik()
    em.initialize()
    if not already:
        susu = await c.get_users(user_ids=sus)
    if not susu.first_name:
        return ["Deleted account", None]

    gbanned, reason_gban = gban_db.get_gban(susu.id)
    if gbanned:
        gban = True
        reason = reason_gban
    else:
        gban = False
        reason = cgr("glbl_7").format(em.warn)

    user_id = susu.id
    userrr = await c.resolve_peer(user_id)
    about = None
    try:
        ll = await c.invoke(GetFullUser(id=userrr))
        about = ll.full_user.about
    except Exception:
        pass
    username = susu.username
    first_name = susu.first_name
    last_name = susu.last_name
    mention = susu.mention(f"{first_name}")
    dc_id = susu.dc_id
    is_verified = susu.is_verified
    is_restricted = susu.is_restricted
    photo_id = susu.photo.big_file_id if susu.photo else None
    is_support = True if user_id in DEVS else False
    if user_id == bot.me.id:
        is_support = "Bot"
    omp = cgr("info_2")
    if is_support or bot.me.id:
        if user_id in DEVS:
            omp = cgr("info_2")
        elif user_id == bot.me.id:
            omp = "Bot"
        elif user_id == c.me.id:
            omp = cgr("info_4")
        if user_id in DEVS and user_id == c.me.id:
            omp = cgr("info_5")

    is_scam = susu.is_scam
    is_bot = susu.is_bot
    is_fake = susu.is_fake
    status = susu.status
    last_date = cgr("info_6")
    if is_bot is True:
        last_date = cgr("info_7")
    if status == UserStatus.RECENTLY:
        last_date = cgr("info_8")
    if status == UserStatus.LAST_WEEK:
        last_date = cgr("info_9")
    if status == UserStatus.LAST_MONTH:
        last_date = cgr("info_10")
    if status == UserStatus.LONG_AGO:
        last_date = cgr("info_11")
    if status == UserStatus.ONLINE:
        last_date = cgr("info_12")
    if status == UserStatus.OFFLINE:
        try:
            last_date = datetime.fromtimestamp(susu.status.date).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        except Exception:
            last_date = cgr("info_13")

    caption = cgr("info_14").format(
        user_id,
        user_id,
        mention,
        first_name,
        last_name,
        ("@" + username) if username else "NA",
        about,
        is_support,
        omp,
        gban,
        reason,
        dc_id,
        is_restricted,
        is_verified,
        is_fake,
        is_scam,
        is_bot,
        last_date,
    )

    return caption, photo_id


async def chat_info(c: user, chat, already=False):
    em = Emojik()
    em.initialize()
    u_name = False
    if not already:
        try:
            chat = await c.get_chat(chat)
            try:
                chat_r = await c.resolve_peer(chat.id)
                ll = await c.invoke(GetFullChannel(channel=chat_r))
                u_name = ll.chats[0].usernames
            except Exception:
                pass
        except Exception:
            try:
                chat_r = await c.resolve_peer(chat)
                chat = await c.get_chat(chat_r.channel_id)
                try:
                    ll = await c.invoke(GetFullChannel(channel=chat_r))
                    u_name = ll.chats[0].usernames
                except Exception:
                    pass
            except KeyError:
                caption = cgr("err").format(em.gagal, r)
                return caption, None
    chat_id = chat.id
    if u_name:
        username = " ".join([f"@{i}" for i in u_name])
    elif not u_name:
        username = chat.username
    total_bot, total_admin, total_bot_admin, total_banned = await count(c, chat.id)
    title = chat.title
    type_ = str(chat.type).split(".")[1]
    is_scam = chat.is_scam
    is_fake = chat.is_fake
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    can_save = chat.has_protected_content
    linked_chat = chat.linked_chat

    caption = cgr("info_15").format(
        chat_id,
        title,
        type_,
        dc_id,
        ("@" + username) if username else "NA",
        total_admin,
        total_bot,
        total_banned,
        total_bot_admin,
        is_scam,
        is_fake,
        is_restricted,
        description,
        members,
        can_save,
        linked_chat.id if linked_chat else "Not Linked",
    )

    return caption, photo_id


@ky.ubot("info|whois", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    if m.reply_to_message and m.reply_to_message.sender_chat:
        await m.reply_text(cgr("info_16").format(em.gagal))
        return
    sus, _, user_name = await extract_user(c, m)

    if not sus:
        await m.reply_text(cgr("glbl_2").format(em.gagal))

    m = await m.reply_text(cgr("proses").format(em.proses))

    try:
        info_caption, photo_id = await user_info(c, sus)

    except Exception as e:
        LOGGER.error(e)
        LOGGER.error(format_exc())
        return await m.edit(str(e))

    if not photo_id:
        await m.delete()
        await sleep(2)
        return await m.reply_text(info_caption, disable_web_page_preview=True)
    photo = await c.download_media(photo_id)

    await m.delete()
    await sleep(2)
    try:
        await m.reply_photo(photo, caption=info_caption)
    except MediaCaptionTooLong:
        x = await m.reply_photo(photo)
        try:
            await x.reply_text(info_caption)
        except EntityBoundsInvalid:
            await x.delete()
            await m.reply_text(info_caption)
        except RPCError as rpc:
            await m.reply_text(rpc)
    except Exception as e:
        await m.reply_text(text=e)
    os.remove(photo)
    return


@ky.ubot("cinfo|chatinfo", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    splited = m.text.split()
    if len(splited) == 1:
        if m.reply_to_message and m.reply_to_message.sender_chat:
            chat = m.reply_to_message.sender_chat.id
        else:
            chat = m.chat.id

    else:
        chat = splited[1]

    try:
        chat = int(chat)
    except (ValueError, Exception) as ef:
        if "invalid literal for int() with base 10:" in str(ef):
            chat = str(chat)
            if chat.startswith("https://"):
                chat = "@" + chat.split("/")[-1]
        else:
            return await m.reply_text(cgr("info_17").format(em.gagal, m.command))

    m = await m.reply_text(cgr("proses").format(em.proses))

    try:
        info_caption, photo_id = await chat_info(c, chat=chat)
        if info_caption.startswith("Failed to find the chat due"):
            await m.reply_text(info_caption)
            return
    except Exception as e:
        await m.delete()
        await sleep(0.5)
        return await m.reply_text(cgr("err").format(em.gagal, e))
    if not photo_id:
        await m.delete()
        await sleep(2)
        return await m.reply_text(info_caption, disable_web_page_preview=True)

    photo = await c.download_media(photo_id)
    await m.delete()
    await sleep(2)
    try:
        await m.reply_photo(photo, caption=info_caption)
    except MediaCaptionTooLong:
        x = await m.reply_photo(photo)
        try:
            await x.reply_text(info_caption)
        except EntityBoundsInvalid:
            await x.delete()
            await m.reply_text(info_caption)
        except RPCError as rpc:
            await m.reply_text(rpc)
    except Exception as e:
        await m.reply_text(text=e)
    os.remove(photo)
    return


@ky.ubot("me|userstats", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = await m.reply_text(f"{em.proses} <code>Collecting stats...</code>")
    start = datetime.now()
    zz = 0
    nanki = 0
    luci = 0
    tgr = 0
    ceger = 0
    kntl = 0
    xenn = await c.get_me()
    async for dialog in c.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            zz += 1
        elif dialog.chat.type == ChatType.BOT:
            ceger += 1
        elif dialog.chat.type == ChatType.GROUP:
            nanki += 1
        elif dialog.chat.type == ChatType.SUPERGROUP:
            luci += 1
            user_s = await dialog.chat.get_member(int(xenn.id))
            if user_s.status in (
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
            ):
                kntl += 1
        elif dialog.chat.type == ChatType.CHANNEL:
            tgr += 1

    end = datetime.now()
    ms = (end - start).seconds
    await Nan.edit_text(
        """**succesful extract your data in `{}` seconds
`{}` Private Messages.
`{}` Groups.
`{}` Super Groups.
`{}` Channels.
`Admin in {}` Chats.
`{}` Bots**""".format(
            ms, zz, nanki, luci, tgr, kntl, ceger
        )
    )
