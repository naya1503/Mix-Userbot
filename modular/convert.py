
import asyncio
import os

from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto
from Mix import *

__modles__ = "Convert"
__help__ = "Convert"



@ky.ubot("toanime")
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    pros = await message.reply(cgr("proses").format(em.proses)
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                file = "foto"
                get_photo = message.reply_to_message.photo.file_id
            elif message.reply_to_message.sticker:
                file = "sticker"
                get_photo = await c.dln(message.reply_to_message)
            elif message.reply_to_message.animation:
                file = "gift"
                get_photo = await c.dln(message.reply_to_message)
            else:
                return await pros.edit(f"{em.gagal} Silahkan balas ke media foto")
        else:
            if message.command[1] in ["foto", "profil", "photo"]:
                chat = (
                    message.reply_to_message.from_user
                    or message.reply_to_message.sender_chat
                )
                file = "foto profil"
                get = await c.get_chat(chat.id)
                photo = get.photo.big_file_id
                get_photo = await c.dln(photo)
    else:
        if len(message.command) < 2:
            return await pros.edit(f"{em.gagal} Silahkan balas ke media foto")
        else:
            try:
                file = "foto"
                get = await c.get_chat(message.command[1])
                photo = get.photo.big_file_id
                get_photo = await c.dln(photo)
            except Exception as error:
                return await pros.edit(cgr("err").format(em.gagal, error))
    await pros.edit(cgr("proses").format(em.proses))
    await c.unblock_user("@qq_neural_anime_bot")
    send_photo = await c.send_photo("@qq_neural_anime_bot", get_photo)
    await asyncio.sleep(30)
    await send_photo.delete()
    await pros.delete()
    info = await c.resolve_peer("@qq_neural_anime_bot")
    anime_photo = []
    async for anime in c.search_messages(
        "@qq_neural_anime_bot", filter=MessagesFilter.PHOTO
    ):
        anime_photo.append(
            InputMediaPhoto(
                anime.photo.file_id, caption=f"{em.sukses}<b>Maker: {c.me.mention}</b>"
            )
        )
    if anime_photo:
        await c.send_media_group(
            message.chat.id,
            anime_photo,
            reply_to_message_id=message.id,
        )
        return await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))

    else:
        await c.send_message(
            message.chat.id,
            f"{em.gagal} <b>Media {file} tidak didukung!!</b>",
            reply_to_message_id=message.id,
        )
        return await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))