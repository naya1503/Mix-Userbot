import os
from io import BytesIO

from pyrogram import *

from Mix import *

__modles__ = "Profile"
__help__ = get_cgr("help_prof")


@ky.ubot("unblock", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id = await c.extract_user(m)
    tex = await m.reply(f"{em.proses} Processing...")
    if not user_id:
        return await tex.edit(
            f"{em.gagal} Silahkan balas pesan pengguna atau berikan username."
        )
    if user_id == c.me.id:
        return await tex.edit(f"{em.gagal} Ya anda gile.")
    await c.unblock_user(user_id)
    umention = (await c.get_users(user_id)).mention
    await tex.edit(f"{em.sukses} Berhasil membuka blokir {umention}")
    return


@ky.ubot("block", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    user_id = await c.extract_user(m)
    tex = await m.reply(f"{em.proses} Processing...")
    if not user_id:
        return await tex.edit(
            f"{em.gagal} Silahkan balas pesan pengguna atau berikan username."
        )
    if user_id == c.me.id:
        return await tex.edit(f"{em.gagal} Ya anda gile.")
    await c.block_user(user_id)
    umention = (await c.get_users(user_id)).mention
    await tex.edit(f"{em.sukses} Berhasil memblokir {umention}")


@ky.ubot("setname", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    tex = await m.reply(f"{em.proses} Processing...")
    direp = m.reply_to_message
    if direp:
        name = direp.text
        await c.update_profile(first_name=name)
        await tex.edit(f"{em.sukses} Berhasil mengganti nama menjadi {name}.")
        return
    if len(m.command) == 2:
        name = m.text.split(None, 1)[1]
        await c.update_profile(first_name=name)
        await tex.edit(f"{em.sukses} Berhasil mengganti nama menjadi {name}.")
        return
    elif len(m.command) == 3:
        name = m.text.split(None, 2)[1]
        last = m.text.split(None, 2)[2]
        await c.update_profile(first_name=name, last_name=last)
        await tex.edit(
            f"{em.sukses} Berhasil mengganti nama depan `{name}` nama belakang `{last}."
        )
        return
    else:
        await tex.edit(f"{em.gagal} Silahkan berikan teks atau balas teks!")
        return


@ky.ubot("setbio", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    tex = await m.reply("Processing...")
    direp = m.reply_to_message
    if direp:
        bio = direp.text
    else:
        bio = m.text.split(None, 1)[1]
    try:
        await c.update_profile(bio=bio)
        await tex.edit(f"{em.sukses} Berhasil mengganti bio menjadi {bio}.")
        return
    except Exception as e:
        await tex.edit(f"{em.gagal} Error : `{e}`\n\nLaporke @KynanSupport!")
        return


@ky.ubot("meadmin", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    bacot = await m.reply(f"{em.proses} Processing...")
    a_chats = []
    me = await c.get_me()
    async for dialog in c.get_dialogs():
        if dialog.chat.type == enums.ChatType.SUPERGROUP:
            gua = await dialog.chat.get_member(int(me.id))
            if gua.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
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
        await bacot.edit_text(f"{em.gagal} Kamu tidak menjadi admin di grup manapun.")
    elif len(text) > 4096:
        with BytesIO(str.encode(text)) as out_file:
            out_file.name = "adminlist.text"
            await m.reply_document(
                document=out_file,
                disable_notification=True,
                quote=True,
            )
            await bacot.delete()
    else:
        await bacot.edit_text(
            f"{em.sukses} **Kamu admin di `{len(a_chats)}` group:\n\n{text}**",
            disable_web_page_preview=True,
        )


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
        await m.reply("**Foto Profil anda Berhasil Diubah.**")
        os.remove(pat)
    except Exception as e:
        return await m.reply(f"{em.gagal} Errror : `{e}`")


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
