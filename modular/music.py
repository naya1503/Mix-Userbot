# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

import datetime
import os
import random
import string

from pytgcalls import GroupCallFactory, GroupCallFileAction

from Mix import ReplyCheck, ky, nlx
from Mix.core.tools_music import *

gbr = "https://telegra.ph//file/b2a9611753657547acf15.jpg"


@ky.ubot("play", sudo=True)
async def _(client: nlx, message):
    group_call = play_vc.get((message.chat.id, client.me.id))
    u_s = await client.eor(message, "`Processing..`")
    input_str = client.get_text(message)
    rep = message.reply_to_message
    if len(message.command) == 1 and not rep:
        return await u_s.edit_text("`Reply To A File To PLay It.`")
    if rep:
        await u_s.edit_text("`Please Wait, Let Me Download This File!`")
        audio = rep.audio
        audio_original = await rep.download()
        vid_title = audio.title or audio.file_name
        uploade_r = audio.performer or "Unknown Artist."
        dura_ = audio.duration
        dur = datetime.timedelta(seconds=dura_)
        if audio.thumbs:
            thumb = audio.thumbs[0]
            tumben = thumb.file_id
            meki = await client.download_media(tumben)
        else:
            meki = gbr
        raw_file_name = (
            "".join(random.choice(string.ascii_lowercase) for i in range(5)) + ".raw"
        )

        url = rep.link
    else:
        search = VideosSearch(input_str, limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
        file_name, vid_title, url, dur, views, uploade_r, meki, data_ytp = (
            await YoutubeDownload(link, as_video=False)
        )
        try:
            # audio_original = await yt_dl(url, bot, message, start)
            audio_original = file_name
        except BaseException as e:
            return await u_s.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        raw_file_name = (
            "".join(random.choice(string.ascii_lowercase) for i in range(5)) + ".raw"
        )

    try:
        raw_file_name = await convert_to_raw(audio_original, raw_file_name)
    except BaseException as e:
        return await u_s.edit(
            f"`FFmpeg Failed To Convert Song To raw Format.` \n**Error :** `{e}`"
        )
    if os.path.exists(audio_original):
        os.remove(audio_original)
    if not group_call:
        group_call = GroupCallFactory(
            client, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
        ).get_file_group_call()
        group_call.song_name = vid_title
        play_vc[(message.chat.id, client.me.id)] = group_call
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"**Error While Joining VC:** `{e}`")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        plere = """
<u><b>🎼 Sekarang Diputar 🎶</b></u>

**🎵 Judul : `{}`**
**🎸 Artist : `{}`**
**⏲️️ Durasi : `{}`**
**📩 Pesan : [Disini]({})**
        """
        try:
            await message.reply_photo(
                photo=meki,
                caption=plere.format(vid_title, uploade_r, dur, url),
                reply_to_message_id=ReplyCheck(message),
            )
        except:
            await client.eor(
                message,
                plere.format(vid_title, uploade_r, dur, url),
                reply_to_message_id=ReplyCheck(message),
            )
        await u_s.delete()
        try:
            os.remove(meki)
        except:
            pass
        return
        # return await u_s.edit(f"Playing `{vid_title}` in `{message.chat.title}`!")
    elif not group_call.is_connected:
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"**Error While Joining VC:** `{e}`")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        plere = """
<u><b>🎼 Sekarang Diputar 🎶</b></u>

**🎵 Judul : `{}`**
**🎸 Artist : `{}`**
**⏲️️ Durasi :` {}`**
**📩 Channel : [Youtube]({})**
        """
        try:
            await message.reply_photo(
                photo=meki,
                caption=plere.format(vid_title, uploade_r, dur, url),
                reply_to_message_id=ReplyCheck(message),
            )
        except:
            await client.eor(
                message,
                plere.format(vid_title, uploade_r, dur, url),
                reply_to_message_id=ReplyCheck(message),
            )
        await u_s.delete()
        return
        # return await u_s.edit(f"Playing `{vid_title}` in `{message.chat.title}`!")
    else:
        s_d = stream_vc.get((message.chat.id, client.me.id))
        f_info = {
            "song_name": vid_title,
            "raw": raw_file_name,
            "singer": uploade_r,
            "dur": dur,
            "url": url,
        }
        if s_d:
            s_d.append(f_info)
        else:
            stream_vc[(message.chat.id, client.me.id)] = [f_info]
        s_d = stream_vc.get((message.chat.id, client.me.id))
        return await u_s.edit(f"Added `{vid_title}` To Position `#{len(s_d)+1}`!")
