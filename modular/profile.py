import os
from io import BytesIO

from pyrogram import *
from pyrogram.enums import *

from Mix import *

__modles__ = "Profile"
__help__ = get_cgr("help_prof")


@ky.ubot("unblock", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id = await c.extract_user(m)
    tex = await m.reply(cgr("proses").format(em.proses))
    if not user_id:
        return await tex.edit(cgr("prof_1").format(em.gagal))
    if user_id == c.me.id:
        await tex.delete()
        return
    await c.unblock_user(user_id)
    (await c.get_users(user_id)).mention
    await tex.edit(cgr("prof_2").format(em.sukses, mention))
    return


@ky.ubot("block", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id = await c.extract_user(m)
    tex = await m.reply(cgr("proses").format(em.proses))
    if not user_id:
        return await tex.edit(cgr("prof_1").format(em.gagal))
    if user_id == c.me.id:
        await tex.delete()
        return
    await c.block_user(user_id)
    umention = (await c.get_users(user_id)).mention
    await tex.edit(cgr("prof_3").format(em.sukses, umention))
    return


@ky.ubot("setname", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    tex = await m.reply(cgr("proses").format(em.proses))
    direp = m.reply_to_message
    if direp:
        name = direp.text
        await c.update_profile(first_name=name)
        await tex.edit(cgr("prof_4").format(em.sukses, name))
        return
    if len(m.command) == 2:
        name = m.text.split(None, 1)[1]
        await c.update_profile(first_name=name)
        await tex.edit(cgr("prof_4").format(em.sukses, name))
        return
    elif len(m.command) == 3:
        name = m.text.split(None, 2)[1]
        last = m.text.split(None, 2)[2]
        await c.update_profile(first_name=name, last_name=last)
        await tex.edit(cgr("prof_5").format(em.sukses, name, last))
        return
    else:
        await tex.edit(cgr("gcs_1").format(em.gagal))
        return


@ky.ubot("setbio", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    tex = await m.reply(cgr("proses").format(em.proses))
    direp = m.reply_to_message
    if direp:
        bio = direp.text
    else:
        bio = m.text.split(None, 1)[1]
    try:
        await c.update_profile(bio=bio)
        await tex.edit(cgr("prof_6").format(em.sukses, bio))
        return
    except Exception as e:
        await tex.edit(cgr("err").format(em.gagal, e))
        return


@ky.ubot("meadmin", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    bacot = await m.reply(cgr("proses").format(em.proses))
    a_chats = []
    me = await c.get_me()
    async for dialog in c.get_dialogs():
        if dialog.chat.type == ChatType.SUPERGROUP:
            gua = await dialog.chat.get_member(int(me.id))
            if gua.status in (
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chats.append(dialog.chat)

    text = ""
    j = 0
    for chat in a_chats:
        try:
            title = chat.title
        except Exception:
            title = "Private Group"
        if chat.username:
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{chat.username})[`{chat.id}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{chat.id}`]\n"
        j += 1

    if not text:
        await bacot.edit_text(cgr("prof_7").format(em.gagal))
        return
    elif len(text) > 4096:
        with BytesIO(str.encode(text)) as out_file:
            out_file.name = "adminlist.text"
            await m.reply_document(document=out_file)
            await bacot.delete()
            return
    else:
        await bacot.edit_text(
            cgr("prof_8").format(em.sukses, len(a_chats), text),
            disable_web_page_preview=True,
        )
        return


@ky.ubot("setpp", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    replied = m.reply_to_message
    media = None
    try:
        if replied.photo:
            media = replied.photo.file_id
            pat = await c.download_media(media, file_name=f"{user.me.id}.jpg")
            await c.set_profile_photo(photo=pat)
        elif replied.video:
            media = replied.video.file_id
            pat = await c.download_media(media, file_name=f"{user.me.id}.mp4")
            await c.set_profile_photo(video=pat)
        await m.reply(cgr("prof_9").format(em.sukses))
        os.remove(pat)
    except Exception as e:
        return await m.reply(cgr("err").format(em.gagal, e))


@ky.ubot("purgeme", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if len(m.command) != 2:
        return await m.delete()
    n = m.reply_to_message if m.reply_to_message else m.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return
    n = int(n)
    if n < 1:
        return
    chat_id = m.chat.id
    message_ids = [
        m.id
        async for m in c.search_messages(
            chat_id,
            from_user=int(m.from_user.id),
            limit=n,
        )
    ]
    if not message_ids:
        return
    to_delete = [message_ids[i : i + 999] for i in range(0, len(message_ids), 999)]
    for hundred_messages_or_less in to_delete:
        await c.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
