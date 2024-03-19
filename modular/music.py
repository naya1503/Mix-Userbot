"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
import ffmpeg
import asyncio
import subprocess
from config import *
from signal import SIGINT
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from Mix import *
from Mix.core.tools_music import *

msg={}
playlist=[]
durasi_musik

@ky.ubot("play")
async def _(c: nlx, message):
    type=""
    yturl=""
    ysearch=""
    if m.audio:
        type="audio"
        m_audio = m
    elif m.reply_to_message and m.reply_to_message.audio:
        type="audio"
        m_audio = m.reply_to_message
    else:
        if m.reply_to_message:
            link=m.reply_to_message.text
            regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
            match = re.match(regex,link)
            if match:
                type="youtube"
                yturl=link
        elif " " in m.text:
            text = m.text.split(" ", 1)
            query = text[1]
            regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
            match = re.match(regex,query)
            if match:
                type="youtube"
                yturl=query
            else:
                type="query"
                ysearch=query
        else:
            await m.reply_text("Silahkan balas audio atau berikan query!!")
            
            return
    user=f"[{m.from_user.first_name}](tg://user?id={message.from_user.id})"
    group_call = mixmus.group_call
    if type=="audio":
        if round(m_audio.audio.duration / 60) > durasi_musik:
            d=await m.reply_text(f"❌ Audio lebih panjang dari {durasi_musik} menit tidak diizinkan, Audio yang diizinkan adalah {round(m_audio.audio.duration/60)} menit!")
            return
        if playlist and playlist[-1][2] == m_audio.audio.file_id:
            d=await m.reply_text(f"➕ **Sudah ditambahkan ke daftar putar!**")
            return
        data={1:m_audio.audio.title, 2:m_audio.audio.file_id, 3:"telegram", 4:user}
        playlist.append(data)
        if len(playlist) == 1:
            m_status = await m.reply_text("Processing...")
            await mixmus.download_audio(playlist[0])
            if 1 in RADIO:
                if group_call:
                    group_call.input_filename = ''
                    RADIO.remove(1)
                    RADIO.add(0)
                process = FFMPEG_PROCESSES.get(m.chat.id)
                if process:
                    try:
                        process.send_signal(SIGINT)
                    except subprocess.TimeoutExpired:
                        process.kill()
                    except Exception as e:
                        print(e)
                        pass
                    FFMPEG_PROCESSES[m.chat.id] = ""
            if not group_call.is_connected:
                await mixmus.start_call()
            file=playlist[0][1]
            group_call.input_filename = os.path.join(
                _.workdir,
                DEFAULT_DOWNLOAD_DIR,
                f"{file}.raw"
            )
            await m_status.delete()
            print(f"- START PLAYING: {playlist[0][1]}")
        if not playlist:
            pl = f"{emoji.NO_ENTRY} **Tidak ada playlist!**"
        else:   
            pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        if EDIT_TITLE:
            await mixmus.edit_title()
        if m.chat.type == ChatType.PRIVATE:
            await m.reply_text(pl)        
        elif TAG_LOG:
            await mixmus.send_playlist()
        elif not TAG_LOG and m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            k=await m.reply_text(pl)
        for track in playlist[:2]:
            await mixmus.download_audio(track)


    if type=="youtube" or type=="query":
        if type=="youtube":
            msg = await m.reply_text("🔍")
            url=yturl
        elif type=="query":
            try:
                msg = await m.reply_text("🔍")
                ytquery=ysearch
                results = YoutubeSearch(ytquery, max_results=1).to_dict()
                url = f"https://youtube.com{results[0]['url_suffix']}"
                title = results[0]["title"][:40]
            except Exception as e:
                await msg.edit(
                    "**Literary Found Noting!\nTry Searching On Inline 😉!**"
                )
                print(str(e))
                return
        else:
            return
        ydl_opts = {
            "geo-bypass": True,
            "nocheckcertificate": True
        }
        ydl = YoutubeDL(ydl_opts)
        try:
            info = ydl.extract_info(url, False)
        except Exception as e:
            print(e)
            k=await msg.edit(
                f"❌ **YouTube Download Error !** \n\n{e}"
                )
            print(str(e))
            return
        duration = round(info["duration"] / 60)
        title= info["title"]
        if int(duration) > durasi_musik:
            k=await m.reply_text(f"❌ __Videos Longer Than {durasi_musik} Minute(s) Aren't Allowed, The Provided Video Is {duration} Minute(s)!__")
            return
        data={1:title, 2:url, 3:"youtube", 4:user}
        playlist.append(data)
        group_call = mixmus.group_call
        client = group_call.client
        if len(playlist) == 1:
            m_status = await msg.edit("⚡️")
            await mixmus.download_audio(playlist[0])
            if 1 in RADIO:
                if group_call:
                    group_call.input_filename = ''
                    RADIO.remove(1)
                    RADIO.add(0)
                process = FFMPEG_PROCESSES.get(m.chat.id)
                if process:
                    try:
                        process.send_signal(SIGINT)
                    except subprocess.TimeoutExpired:
                        process.kill()
                    except Exception as e:
                        print(e)
                        pass
                    FFMPEG_PROCESSES[m.chat.id] = ""
            if not group_call.is_connected:
                await mixmus.start_call()
            file=playlist[0][1]
            group_call.input_filename = os.path.join(
                client.workdir,
                DEFAULT_DOWNLOAD_DIR,
                f"{file}.raw"
            )
            await m_status.delete()
            print(f"- START PLAYING: {playlist[0][1]}")
        else:
            await msg.delete()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} **Tidak ada playlist!**"
        else:
            pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        if EDIT_TITLE:
            await mixmus.edit_title()
        if m.chat.type == ChatType.PRIVATE:
            await m.reply_text(pl)
        if TAG_LOG:
            await mixmus.send_playlist()
        elif not TAG_LOG and m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            k=await m.reply_text(pl)
        for track in playlist[:2]:
            await mixmus.download_audio(track)

"""
@Client.on_message(filters.command(["current", f"current@{USERNAME}"]) & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def current(_, m: Message):
    if not playlist:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Playing!**")
        return
    else:
        pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
            f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
            for i, x in enumerate(playlist)
            ])
    if m.chat.type == "private":
        await m.reply_text(
            pl,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄", callback_data="replay"),
                        InlineKeyboardButton("⏸", callback_data="pause"),
                        InlineKeyboardButton("⏭", callback_data="skip")
                    
                    ],

                ]
                )
        )
    else:
        if msg.get('playlist') is not None:
            await msg['playlist'].delete()
        msg['playlist'] = await m.reply_text(
            pl,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄", callback_data="replay"),
                        InlineKeyboardButton("⏸", callback_data="pause"),
                        InlineKeyboardButton("⏭", callback_data="skip")
                    
                    ],

                ]
                )
        )


@Client.on_message(filters.command(["volume", f"volume@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def set_vol(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.ROBOT} **Didn't Joined Any Voice Chat!**")
        return
    if len(m.command) < 2:
        k=await m.reply_text(f"{emoji.ROBOT} **You Forgot To Pass Volume (0-200)!**")
        return
    await group_call.set_my_volume(int(m.command[1]))
    k=await m.reply_text(f"{emoji.SPEAKER_MEDIUM_VOLUME} **Volume Set To {m.command[1]}!**")


@Client.on_message(filters.command(["skip", f"skip@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def skip_track(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Playing To Skip!**")
        return
    if len(m.command) == 1:
        await mixmus.skip_current_playing()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} **Emixmusty Playlist!**"
        else:
            pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
            f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
            for i, x in enumerate(playlist)
            ])
        if m.chat.type == "private":
            await m.reply_text(pl)
        if TAG_LOG:
            await mixmus.send_playlist()
        elif not TAG_LOG and m.chat.type == "supergroup":
            k=await m.reply_text(pl)
    else:
        try:
            items = list(dict.fromkeys(m.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"{playlist[i][1]}"
                    playlist.pop(i)
                    text.append(f"{emoji.WASTEBASKET} **Succesfully Skipped** - {i}. **{audio}**")
                else:
                    text.append(f"{emoji.CROSS_MARK} **Can't Skip First Two Song** - {i}")
            k=await m.reply_text("\n".join(text))
            if not playlist:
                pl = f"{emoji.NO_ENTRY} **Emixmusty Playlist!**"
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
                    for i, x in enumerate(playlist)
                    ])
            if m.chat.type == "private":
                await m.reply_text(pl)
            if TAG_LOG:
                await mixmus.send_playlist()
            elif not TAG_LOG and m.chat.type == "supergroup":
                k=await m.reply_text(pl)
        except (ValueError, TypeError):
            k=await m.reply_text(f"{emoji.NO_ENTRY} **Invalid Input!**",
                                       disable_web_page_preview=True)


@Client.on_message(filters.command(["join", f"join@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def join_group_call(client, m: Message):
    group_call = mixmus.group_call
    if group_call.is_connected:
        k=await m.reply_text(f"{emoji.ROBOT} **Already Joined To The Voice Chat!**")
        return
    await mixmus.start_call()
    chat = await client.get_chat(m.chat.id)
    k=await m.reply_text(f"{emoji.CHECK_MARK_BUTTON} **Joined The Voice Chat In {chat.title} Successfully!**")


@Client.on_message(filters.command(["leave", f"leave@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def leave_voice_chat(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.ROBOT} **Didn't Joined Any Voice Chat!**")
        return
    playlist.clear()
    if 1 in RADIO:
        await mixmus.stop_radio()
    group_call.input_filename = ''
    await group_call.stop()
    k=await m.reply_text(f"{emoji.CROSS_MARK_BUTTON} **Left From The Voice Chat Successfully!**")


@Client.on_message(filters.command(["stop", f"stop@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def stop_playing(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Playing To Stop!**")
        return
    if 1 in RADIO:
        await mixmus.stop_radio()
    group_call.stop_playout()
    k=await m.reply_text(f"{emoji.STOP_BUTTON} **Stopped Playing!**")
    playlist.clear()


@Client.on_message(filters.command(["replay", f"replay@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def restart_playing(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Playing To Replay!**")
        return
    if not playlist:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Emixmusty Playlist!**")
        return
    group_call.restart_playout()
    k=await m.reply_text(
        f"{emoji.COUNTERCLOCKWISE_ARROWS_BUTTON}  "
        "**Playing From The Beginning!**"
    )


@Client.on_message(filters.command(["pause", f"pause@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def pause_playing(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Playing To Pause!**")
        return
    mixmus.group_call.pause_playout()
    k=await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} **Paused Playing!**",
                               quote=False)


@Client.on_message(filters.command(["resume", f"resume@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def resume_playing(_, m: Message):
    if not mixmus.group_call.is_connected:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Paused To Resume!**")
        return
    mixmus.group_call.resume_playout()
    k=await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} **Resumed Playing!**",
                               quote=False)

@Client.on_message(filters.command(["clean", f"clean@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def clean_raw_pcm(client, m: Message):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    all_fn: list[str] = os.listdir(download_dir)
    for track in playlist[:2]:
        track_fn = f"{track[1]}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    k=await m.reply_text(f"{emoji.WASTEBASKET} **Cleaned {count} Files!**")


@Client.on_message(filters.command(["mute", f"mute@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def mute(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Playing To Mute!**")
        return
    await group_call.set_is_mute(True)
    k=await m.reply_text(f"{emoji.MUTED_SPEAKER} **User Muted!**")


@Client.on_message(filters.command(["unmute", f"unmute@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def unmute(_, m: Message):
    group_call = mixmus.group_call
    if not group_call.is_connected:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Muted To Unmute!**")

        return
    await group_call.set_is_mute(False)
    k=await m.reply_text(f"{emoji.SPEAKER_MEDIUM_VOLUME} **User Unmuted!**")


@Client.on_message(filters.command(["playlist", f"playlist@{USERNAME}"]) & (filters.chat(m.chat.id) | filters.private | filters.chat(TAG_LOG)))
async def show_playlist(_, m: Message):
    if not playlist:
        k=await m.reply_text(f"{emoji.NO_ENTRY} **Nothing Is Playing!**")

        return
    else:
        pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
            f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
            for i, x in enumerate(playlist)
            ])
    if m.chat.type == "private":
        await m.reply_text(pl)
    else:
        if msg.get('playlist') is not None:
            await msg['playlist'].delete()
        msg['playlist'] = await m.reply_text(pl)

"""