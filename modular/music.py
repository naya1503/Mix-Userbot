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
import time

from pytgcalls import GroupCallFactory, GroupCallFileAction
from youtubesearchpython import SearchVideos

from Mix import *
from Mix.core.tools_music import *


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
        audio = message.reply_to_message
        audio_original = await audio.download()
        vid_title = audio.title or audio.file_name
        uploade_r = audio.performer or "Unknown Artist."
        dura_ = audio.duration
        dur = datetime.timedelta(seconds=dura_)
        raw_file_name = (
            "".join(random.choice(string.ascii_lowercase) for i in range(5)) + ".raw"
        )

        url = audio.link
    else:
        search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
        rt = search.result()
        result_s = rt.get("search_result")
        if not result_s:
            return await u_s.edit(
                f"`No Song Found Matching With Query - {input_str}, Please Try Giving Some Other Name.`"
            )
        url = result_s[0]["link"]
        dur = result_s[0]["duration"]
        vid_title = result_s[0]["title"]
        result_s[0]["id"]
        uploade_r = result_s[0]["channel"]
        start = time.time()
        try:
            audio_original = await yt_dl(url, bot, message, start)
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
        return await u_s.edit(f"Playing `{vid_title}` in `{message.chat.title}`!")
    elif not group_call.is_connected:
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"**Error While Joining VC:** `{e}`")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await u_s.edit(f"Playing `{vid_title}` in `{message.chat.title}`!")
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
