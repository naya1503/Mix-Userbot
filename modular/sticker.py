################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty || William || Gojo_Satoru
"""
################################################################

__modles__ = "Sticker"
__help__ = """
Help Command Sticker

• Perintah: <code>{0}gstik</code> [reply sticker]
• Penjelasan: Untuk mengambil info sticker.
"""

import os

from pyrogram import enums
from pyrogram.errors import BadRequest, PeerIdInvalid, StickersetInvalid
from pyrogram.raw.functions.messages import GetStickerSet, SendMedia
from pyrogram.raw.functions.stickers import AddStickerToSet, CreateStickerSet
from pyrogram.raw.types import (DocumentAttributeFilename, InputDocument,
                                InputMediaUploadedDocument,
                                InputStickerSetItem, InputStickerSetShortName)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Mix import Emojik, bot, ky, ndB, user
from Mix.core.http import http
from Mix.core.stick_tools import EMOJI_PATTERN, convert_video, resize_image

LOG_ME = ndB.get_key("TAG_LOG")


@ky.ubot("gstik|getstiker|getsticker", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    stick = rep.sticker
    if not rep:
        await m.reply(f"{em.gagal} Silahkan balas ke sticker!")
        return
    else:
        if stick.is_video == True:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.mp4")
            await m.reply_to_message.reply_document(
                document=pat,
                caption=f"<b>Emoji:</b> {stick.emoji}\n"
                f"<b>Sticker ID:</b> <code>{stick.file_id}</code>",
            )
        elif stick.is_animated == True:
            await m.reply(f"{em.gagal} Silahkan balas ke sticker non animasi!")
            return

        else:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.png")
            await m.reply_to_message.reply_document(
                document=pat,
                caption=f"<b>Emoji:</b> {stick.emoji}\n"
                f"<b>Sticker ID:</b> <code>{stick.file_id}</code>",
            )
        return
    os.remove(pat)


#@ky.ubot("kang", sudo=False)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(f"{em.proses} Processing kang stickers...")
    sticker_emoji = "🤔"
    await user.unblock_user(bot.me.username)
    await user.send_message(bot.me.username, "/start")
    x = await user.forward_messages(bot.me.username, m.chat.id, m.reply_to_message.id)
    await user.send_message(bot.me.username, "/kang", reply_to_message_id=x.id)
    if await cek_res(m) == "Stiker berhasil dikang":
        pros.edit(
            f"{em.sukses} <b>Stiker berhasil dikang !</b>\n<b>Emoji:</b> {sticker_emoji}\n\n<a href=https://t.me/{bot.me.username}>👀 Klik Disini</a>"
        )
        return


@ky.ubot("kang", sudo=False)
async def _(self: bot, message):
    prog_msg = await message.reply("Mencoba mencuri stiker Anda...")
    sticker_emoji = "🤔"
    packnum = 0
    packname_found = False
    resize = False
    animated = False
    videos = False
    convert = False
    reply = message.reply_to_message
    org = await self.resolve_peer(message.from_user.username or message.from_user.id)

    if reply and reply.media:
        if reply.photo:
            resize = True
        elif reply.animation:
            videos = True
            convert = True
        elif reply.video:
            convert = True
            videos = True
        elif reply.document:
            if "image" in reply.document.mime_type:
                # mime_type: image/webp
                resize = True
            elif reply.document.mime_type in (
                enums.MessageMediaType.VIDEO,
                enums.MessageMediaType.ANIMATION,
            ):
                # mime_type: application/video
                videos = True
                convert = True
            elif "tgsticker" in reply.document.mime_type:
                # mime_type: application/x-tgsticker
                animated = True
        elif reply.sticker:
            if not reply.sticker.file_name:
                return await prog_msg.edit_text("Stiker tidak memiliki nama.")
            if reply.sticker.emoji:
                sticker_emoji = reply.sticker.emoji
            animated = reply.sticker.is_animated
            videos = reply.sticker.is_video
            if videos:
                convert = False
            elif not reply.sticker.file_name.endswith(".tgs"):
                resize = True
        else:
            return await prog_msg.edit_text()

        pack_prefix = "anim" if animated else "vid" if videos else "a"
        packname = f"{pack_prefix}_{message.from_user.id}_by_{self.me.username}"

        if (
            len(message.command) > 1
            and message.command[1].isdigit()
            and int(message.command[1]) > 0
        ):
            # provide pack number to kang in desired pack
            packnum = message.command.pop(1)
            packname = (
                f"{pack_prefix}{packnum}_{message.from_user.id}_by_{self.me.username}"
            )
        if len(message.command) > 1:
            # matches all valid emojis in input
            sticker_emoji = (
                "".join(set(EMOJI_PATTERN.findall("".join(message.command[1:]))))
                or sticker_emoji
            )
        filename = await self.download_media(message.reply_to_message)
        if not filename:
            # Failed to download
            await prog_msg.delete()
            return
    elif message.entities and len(message.entities) > 1:
        pack_prefix = "a"
        filename = "sticker.png"
        packname = f"c{message.from_user.id}_by_{self.me.username}"
        img_url = next(
            (
                message.text[y.offset : (y.offset + y.length)]
                for y in message.entities
                if y.type == "url"
            ),
            None,
        )

        if not img_url:
            await prog_msg.delete()
            return
        try:
            r = await http.get(img_url)
            if r.status_code == 200:
                with open(filename, mode="wb") as f:
                    f.write(r.read())
        except Exception as r_e:
            return await prog_msg.edit_text(f"{r_e.__class__.__name__} : {r_e}")
        if len(message.command) > 2:
            # m.command[1] is image_url
            if message.command[2].isdigit() and int(message.command[2]) > 0:
                packnum = message.command.pop(2)
                packname = f"a{packnum}_{message.from_user.id}_by_{self.me.username}"
            if len(message.command) > 2:
                sticker_emoji = (
                    "".join(set(EMOJI_PATTERN.findall("".join(message.command[2:]))))
                    or sticker_emoji
                )
            resize = True
    else:
        return await prog_msg.edit_text(
            "Ingin saya menebak stikernya? Harap tandai stiker."
        )
    try:
        if resize:
            filename = resize_image(filename)
        elif convert:
            filename = await convert_video(filename)
            if filename is False:
                return await prog_msg.edit_text("Error")
        max_stickers = 50 if animated else 120
        while not packname_found:
            try:
                stickerset = await self.invoke(
                    GetStickerSet(
                        stickerset=InputStickerSetShortName(short_name=packname),
                        hash=0,
                    )
                )
                if stickerset.set.count >= max_stickers:
                    packnum += 1
                    packname = f"{pack_prefix}_{packnum}_{message.from_user.id}_by_{self.me.username}"
                else:
                    packname_found = True
            except StickersetInvalid:
                break
        file = await self.save_file(filename)
        media = await self.invoke(
            SendMedia(
                peer=(await self.resolve_peer(LOG_ME)),
                media=InputMediaUploadedDocument(
                    file=file,
                    mime_type=self.guess_mime_type(filename),
                    attributes=[DocumentAttributeFilename(file_name=filename)],
                ),
                message=f"#Sticker kang by UserID -> {message.from_user.id}",
                random_id=self.rnd_id(),
            ),
        )
        msg_ = media.updates[-1].message
        stkr_file = msg_.media.document
        if packname_found:
            await prog_msg.edit_text(
                "<code>Menggunakan paket stiker yang ada...</code>"
            )
            await self.invoke(
                AddStickerToSet(
                    stickerset=InputStickerSetShortName(short_name=packname),
                    sticker=InputStickerSetItem(
                        document=InputDocument(
                            id=stkr_file.id,
                            access_hash=stkr_file.access_hash,
                            file_reference=stkr_file.file_reference,
                        ),
                        emoji=sticker_emoji,
                    ),
                )
            )
        else:
            await prog_msg.edit_text("<b>Membuat paket stiker baru...</b>")
            stkr_title = f"{message.from_user.first_name}'s"
            if animated:
                stkr_title += "AnimPack"
            elif videos:
                stkr_title += "VidPack"
            if packnum != 0:
                stkr_title += f" v{packnum}"
            try:
                await self.invoke(
                    CreateStickerSet(
                        user_id=org,
                        title=stkr_title,
                        short_name=packname,
                        stickers=[
                            InputStickerSetItem(
                                document=InputDocument(
                                    id=stkr_file.id,
                                    access_hash=stkr_file.access_hash,
                                    file_reference=stkr_file.file_reference,
                                ),
                                emoji=sticker_emoji,
                            )
                        ],
                        animated=animated,
                        videos=videos,
                    )
                )
            except PeerIdInvalid:
                return (
                    await prog_msg.edit_text(
                        "Tampaknya Anda belum pernah berinteraksi dengan saya dalam obrolan pribadi, Anda harus melakukannya dulu.."
                    ),
                )
    except BadRequest:
        return await prog_msg.edit_text(
            "Paket Stiker Anda penuh jika paket Anda tidak dalam Tipe v1 /kang 1, jika tidak dalam Tipe v2 /kang 2 dan seterusnya."
        )
    except Exception as all_e:
        await prog_msg.edit_text(f"{all_e.__class__.__name__} : {all_e}")
    else:
        
        await prog_msg.edit_text(
            f"<b>Stiker berhasil dikang!</b>\n<b>Emoji:</b> {sticker_emoji}\n\n<a href=https://t.me/addstickers/{packname}>👀 Lihat Paket</a>",
        )
        # Cleanup
        await self.delete_messages(chat_id=LOG_ME, message_ids=msg_.id, revoke=True)
        try:
            os.remove(filename)
        except OSError:
            pass


async def cek_res(m):
    return [x async for x in user.get_chat_history(bot.me.username, limit=1)][0].text
