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

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.users import GetFullUser
from team.nandev.class_log import LOGGER

from Mix import *
from Mix.core.sender_tools import extract_user

gban_db = GBan()

__modles__ = "Info"
__help__ = """
Help Command Info 

• Perintah: <code>{0}info</code>
• Penjelasan: Untuk melihat pengguna.

• Perintah: <code>{0}cinfo</code>
• Penjelasan: Untuk melihat grup.
"""


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
        total_bot = total_admin = bot_admin = total_banned = (
            f"{em.gagal} Saya tidak berada digrup itu?"
        )

    return total_bot, total_admin, bot_admin, total_banned


async def user_info(c: user, sus, already=False):
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
        reason = f"{em.warn} Pengguna belum diGban!"

    user_id = susu.id
    userrr = await c.resolve_peer(user_id)
    about = "NA"
    try:
        ll = await c.invoke(GetFullUser(id=userrr))
        about = ll.full_susu.about
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
        is_support = "I'm Bot"
    omp = "Tidak Diketahui"
    if is_support or bot.me.id:
        if user_id in DEVS:
            omp = "Developer"
        elif user_id == bot.me.id:
            omp = "I'm Bot"
        elif user_id == c.me.id:
            omp = "Owner of the bot"
        if user_id in DEVS and user_id == c.me.id:
            omp = "Developer and Owner"

    is_scam = susu.is_scam
    is_bot = susu.is_bot
    is_fake = susu.is_fake
    status = susu.status
    last_date = "Unable to fetch"
    if is_bot is True:
        last_date = "Targeted user is a bot"
    if status == UserStatus.RECENTLY:
        last_date = "User was seen recently"
    if status == UserStatus.LAST_WEEK:
        last_date = "User was seen last week"
    if status == UserStatus.LAST_MONTH:
        last_date = "User was seen last month"
    if status == UserStatus.LONG_AGO:
        last_date = "User was seen long ago or may be I am blocked by the user  :("
    if status == UserStatus.ONLINE:
        last_date = "User is online"
    if status == UserStatus.OFFLINE:
        try:
            last_date = datetime.fromtimestamp(susu.status.date).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        except Exception:
            last_date = "User is offline"

    caption = f"""
<b>User Info</b>

<b>🆔 User ID</b>: <code>{user_id}</code>
<b>📎 Link To Profile</b>: <a href='tg://user?id={user_id}'>Click Here🚪</a>
<b>🫵 Mention</b>: {mention}
<b>🗣 First Name</b>: <code>{first_name}</code>
<b>🔅 Second Name</b>: <code>{last_name}</code>
<b>🔍 Username</b>: {("@" + username) if username else "NA"}
<b>✍️ Bio</b>: `{about}`
<b>🧑‍💻 Support</b>: {is_support}
<b>🥷 Support user type</b>: <code>{omp}</code>
<b>💣 Gbanned</b>: {gban}
<b>☠️ Gban reason</b>: <code>{reason}</code>
<b>🌐 DC ID</b>: {dc_id}
<b>✋ RESTRICTED</b>: {is_restricted}
<b>✅ VERIFIED</b>: {is_verified}
<b>❌ FAKE</b> : {is_fake}
<b>⚠️ SCAM</b> : {is_scam} 
<b>🤖 BOT</b>: {is_bot}
<b>👀 Last seen</b>: <code>{last_date}</code>
"""

    return caption, photo_id


async def chat_info(c: user, chat, already=False):
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
            except KeyError as e:
                caption = f"Failed to find the chat due to\n{e}"
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

    caption = f"""
<b>CHAT INFO</b>

<b>🆔 ID</b>: <code>{chat_id}</code>
<b>🚀 Chat Title</b>: {title}
<b>✨ Chat Type</b>: {type_}
<b>🌐 DataCentre ID</b>: {dc_id}
<b>🔍 Username</b>: {("@" + username) if username else "NA"}
<b>⚜️ Administrators</b>: {total_admin}
<b>🤖 Bots</b>: {total_bot}
<b>🚫 Banned</b>: {total_banned}
<b>⚜️ Admin 🤖 Bots</b>: {total_bot_admin}
<b>⁉️ Scam</b>: {is_scam}
<b>❌ Fake</b>: {is_fake}
<b>✋ Restricted</b>: {is_restricted}
<b>👨🏿‍💻 Description</b>: <code>{description}</code>
<b>👪 Total members</b>: {members}
<b>🚫 Has Protected Content</b>: {can_save}
<b>🔗 Linked Chat</b>: <code>{linked_chat.id if linked_chat else "Not Linked"}</code>

"""

    return caption, photo_id


@ky.ubot("info|whois", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if m.reply_to_message and m.reply_to_m.sender_chat:
        await m.reply_text(
            f"{em.gagal} Ini bukan pengguna, tetapi Grup! Silahkan gunakan <code>.cinfo</code>."
        )
        return
    sus, _, user_name = await extract_user(c, m)

    if not sus:
        await m.reply_text(f"{em.gagal} Saya tidak dapat menemukan pengguna!")

    m = await m.reply_text(
        f"{em.proses} Fetching {('@' + user_name) if user_name else 'user'} info..."
    )

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
        if m.reply_to_message and m.reply_to_m.sender_chat:
            chat = m.reply_to_m.sender_chat.id
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
            return await m.reply_text(
                f"{em.gagal} Silahkan gunakan : <code>.cinfo</code> @username/id grup."
            )

    m = await m.reply_text(f"{em.proses} Fetching chat info...")

    try:
        info_caption, photo_id = await chat_info(c, chat=chat)
        if info_caption.startswith("Failed to find the chat due"):
            await m.reply_text(info_caption)
            return
    except Exception as e:
        await m.delete()
        await sleep(0.5)
        return await m.reply_text(f"{em.gagal} Error Laporkan ke @kynansupport\n {e}")
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
