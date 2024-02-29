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

• Perintah: <code>{0}kang</code> [reply sticker]
• Penjelasan: Untuk mencuri atau membuat stickerpack sendiri.

• Perintah: <code>{0}unkang</code> [reply sticker]
• Penjelasan: Untuk menghapus sticker/stickerpack yang sudah ada.
"""

import os

from pyrogram import enums
from pyrogram.errors import BadRequest, PeerIdInvalid, StickersetInvalid
from pyrogram.file_id import FileId
from pyrogram.raw.functions.messages import GetStickerSet, SendMedia
from pyrogram.raw.functions.stickers import (AddStickerToSet, CreateStickerSet,
                                             RemoveStickerFromSet)
from pyrogram.raw.types import (DocumentAttributeFilename, InputDocument,
                                InputMediaUploadedDocument,
                                InputStickerSetItem, InputStickerSetShortName)

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
            await rep.reply_document(
                document=pat,
                caption=f"<b>Emoji:</b> {stick.emoji}\n"
                f"<b>Sticker ID:</b> <code>{stick.file_id}</code>",
            )
        elif stick.is_animated == True:
            await m.reply(f"{em.gagal} Silahkan balas ke sticker non animasi!")
            return

        else:
            pat = await c.download_media(stick, file_name=f"{stick.set_name}.png")
            await rep.reply_document(
                document=pat,
                caption=f"<b>Emoji:</b> {stick.emoji}\n"
                f"<b>Sticker ID:</b> <code>{stick.file_id}</code>",
            )
        return
    os.remove(pat)


@ky.ubot("kang", sudo=False)
async def _(self: bot, m):
    em = Emojik()
    em.initialize()
    prog_msg = await m.reply(f"{em.proses} Processing kang stickers...")
    sticker_emoji = "🤔"
    packnum = 0
    packname_found = False
    resize = False
    animated = False
    videos = False
    convert = False
    reply = m.reply_to_message
    org = await self.resolve_peer(m.from_user.username or m.from_user.id)

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
                enums.mMediaType.VIDEO,
                enums.mMediaType.ANIMATION,
            ):
                # mime_type: application/video
                videos = True
                convert = True
            elif "tgsticker" in reply.document.mime_type:
                # mime_type: application/x-tgsticker
                animated = True
        elif reply.sticker:
            if not reply.sticker.file_name:
                return await prog_msg.edit("Stiker tidak memiliki nama.")
            if reply.sticker.emoji:
                sticker_emoji = reply.sticker.emoji
            animated = reply.sticker.is_animated
            videos = reply.sticker.is_video
            if videos:
                convert = False
            elif not reply.sticker.file_name.endswith(".tgs"):
                resize = True
        else:
            return await prog_msg.delete()

        pack_prefix = "anim" if animated else "vid" if videos else "a"
        packname = f"{pack_prefix}_{m.from_user.id}_by_{self.me.username}"

        if len(m.command) > 1 and m.command[1].isdigit() and int(m.command[1]) > 0:
            # provide pack number to kang in desired pack
            packnum = m.command.pop(1)
            packname = f"{pack_prefix}{packnum}_{m.from_user.id}_by_{self.me.username}"
        if len(m.command) > 1:
            # matches all valid emojis in input
            sticker_emoji = (
                "".join(set(EMOJI_PATTERN.findall("".join(m.command[1:]))))
                or sticker_emoji
            )
        filename = await self.download_media(reply)
        if not filename:
            # Failed to download
            await prog_msg.delete()
            return
    elif m.entities and len(m.entities) > 1:
        pack_prefix = "a"
        filename = "sticker.png"
        packname = f"c{m.from_user.id}_by_{self.me.username}"
        img_url = next(
            (
                m.text[y.offset : (y.offset + y.length)]
                for y in m.entities
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
            return await prog_msg.edit(f"{em.gagal} Error : {r_e}")
        if len(m.command) > 2:
            # m.command[1] is image_url
            if m.command[2].isdigit() and int(m.command[2]) > 0:
                packnum = m.command.pop(2)
                packname = f"a{packnum}_{m.from_user.id}_by_{self.me.username}"
            if len(m.command) > 2:
                sticker_emoji = (
                    "".join(set(EMOJI_PATTERN.findall("".join(m.command[2:]))))
                    or sticker_emoji
                )
            resize = True
    else:
        return await prog_msg.edit(f"{em.gagal} Tidak valid!")
    try:
        if resize:
            filename = resize_image(filename)
        elif convert:
            filename = await convert_video(filename)
            if filename is False:
                return await prog_msg.edit("Error")
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
                    packname = f"{pack_prefix}_{packnum}_{m.from_user.id}_by_{self.me.username}"
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
                message=f"#Sticker kang by UserID -> {m.from_user.id}",
                random_id=self.rnd_id(),
            ),
        )
        msg_ = media.updates[-1].message
        stkr_file = msg_.media.document
        if packname_found:
            await prog_msg.edit(f"{em.proses} Menggunakan paket stiker yang ada...")
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
            await prog_msg.edit(f"{em.proses} Membuat paket stiker baru...")
            stkr_title = f"{m.from_user.first_name}"
            if animated:
                stkr_title += " Animation Pack"
            elif videos:
                stkr_title += " Video Pack"
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
                await prog_msg.edit(
                    "Tampaknya Anda belum pernah berinteraksi dengan saya dalam obrolan pribadi, Anda harus melakukannya dulu.."
                )
                return
    except BadRequest:
        return await prog_msg.edit(
            "Paket Stiker Anda penuh jika paket Anda tidak dalam Tipe v1 /kang 1, jika tidak dalam Tipe v2 /kang 2 dan seterusnya."
        )
    except Exception as all_e:
        await prog_msg.edit(f"{em.gagal} Error: {all_e}")
    else:
        await prog_msg.edit(
            f"<b>Stiker berhasil dikang!</b>\n<b>Emoji:</b> {sticker_emoji}\n<b><a href=https://t.me/addstickers/{packname}>👀 Lihat Paket Disini</a></b>"
        )
        # Cleanup
        await self.delete_messages(chat_id=LOG_ME, message_ids=msg_.id, revoke=True)
        try:
            os.remove(filename)
        except OSError:
            pass


"""
@ky.ubot("unkang", sudo=False)
async def _(self: bot, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    if not rep:
        await m.reply(f"{em.gagal} Harap balas sticker yang ingin dihapus!")
        return
    if rep.sticker:
        pros = await m.reply(f"{em.proses} Mencoba menghapus stickers...")
        try:
            ee = rep.sticker
            tk = await user.send_message(bot.me.username, ee.file_id)
            decoded = FileId.decode(tk.text)
            sticker = InputDocument(
                id=decoded.media_id,
                access_hash=decoded.access_hash,
                file_reference=decoded.file_reference,
            )
            await self.invoke(RemoveStickerFromSet(sticker=sticker))
            await pros.edit(f"{em.sukses} Stiker berhasil dihapus dari paket anda.")
            return
        except Exception as e:
            await pros.edit(
                f"{em.gagal} Gagal menghapus stiker dari paket Anda.\n\nError: {e}"
            )
            return
    else:
        await pros.edit(
            f"{em.gagal} Tolong balas stiker yang dibuat oleh Anda untuk menghapus stiker dari paket Anda."
        )
        return
"""


@ky.ubot("unkang", sudo=False)
async def _(self: bot, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    if not rep:
        await m.reply(f"{em.gagal} Harap balas sticker yang ingin dihapus!")
        return
    if rep.sticker:
        pros = await m.reply(f"{em.proses} Mencoba menghapus stickers...")
        try:
            sticker_id = rep.sticker.file_id
            await self.invoke(RemoveStickerFromSet(sticker=sticker_id))
            await pros.edit(f"{em.sukses} Stiker berhasil dihapus dari paket Anda.")
        except BadRequest as e:
            await pros.edit(
                f"{em.gagal} Gagal menghapus stiker dari paket Anda.\n\nError: {e}"
            )
    else:
        await m.reply(
            f"{em.gagal} Tolong balas stiker yang dibuat oleh Anda untuk menghapus stiker dari paket Anda."
        )
