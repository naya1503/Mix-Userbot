import asyncio
import os

from pyrogram.errors import *

from Mix import *
from Mix.core.tools_media import *
from Mix.core.tools_music import *


@ky.ubot("play", sudo=True)
async def _(c: nlx, m):
    if "playfrom" in m.text.split()[0]:
        return  # For PlayFrom Conflict
    xx = await m.reply("proses")
    chat = m.chat.id
    from_user = m.from_user
    reply, song = None, None
    if m.reply_to_message:
        reply = m.reply_to_message
    else:
        song = m.text.split(None, 1)[1]
    if not (reply or song):
        return await xx.edit("Harap tentukan nama lagu atau balas ke file audio !")
    await xx.edit("mencoba-coba")
    if reply and reply.media and mediainfo(reply.media).startswith(("audio", "video")):
        song, thumb, song_name, link, duration = await file_download(c, reply)
    else:
        song, thumb, song_name, link, duration = await download(song)
    yoman = MP(chat)
    song_name = f"{song_name[:30]}..."
    if not yoman.group_call.is_connected:
        if not (await yoman.vc_joiner()):
            return
        await yoman.group_call.join(chat)
        await asyncio.sleep(2)
        await yoman.group_call.start_audio(song)
        add_to_queue(chat, song, song_name, link, thumb, from_user, duration)
        text = "📀 <strong>Sedang dimainkan: <a href={}>{}</a>\n⏰ Durasi:</strong> <code>{}</code>\n👥 <strong>Di:</strong> <code>{}</code>\n🙋‍♂ <strong>Diminta oleh: {}</strong>".format(
            link, song_name, duration, chat, from_user
        )
        try:
            await m.reply_photo(
                photo=thumb,
                caption=text,
                disable_web_page_preview=True,
            )
            await xx.delete()
        except ChatSendMediaForbidden:
            await xx.edit(text, disable_web_page_preview=True)
        if thumb and os.path.exists(thumb):
            os.remove(thumb)
    else:
        if not (
            reply
            and reply.media
            and mediainfo(reply.media).startswith(("audio", "video"))
        ):
            song = None
            add_to_queue(chat, song, song_name, link, thumb, from_user, duration)

        return await xx.edit(
            f"✚ Ditambahkan 🎵 <a href={link}>{song_name}</a> antrian ke #{list(VC_QUEUE[chat].keys())[-1]}."
        )
