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
from asyncio import sleep

from pytgcalls import GroupCallFactory, GroupCallFileAction
from youtubesearchpython import VideosSearch

from Mix import Emojik, ReplyCheck, YoutubeDownload, cgr, get_cgr, ky, nlx
from Mix.core.tools_music import *

__modles__ = "Music"
__help__ = get_cgr("help_mus")

gbr = "https://telegra.ph//file/b2a9611753657547acf15.jpg"


@ky.ubot("play", sudo=True)
async def _(client: nlx, message):
    em = Emojik()
    em.initialize()
    group_call = play_vc.get((message.chat.id, client.me.id))
    pros = await message.reply(cgr("proses").format(em.proses))
    gt_txt = client.get_text(message)
    rep = message.reply_to_message
    org = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
    if len(message.command) == 1 and not rep:
        await pros.edit_text(
            f"{em.gagal} **Salah goblok!! Format `{message.text}` [query/balas media.**"
        )
        return
    await pros.edit_text(f"{em.proses} **Starting to download...**")
    if rep:
        if rep.text:
            search = VideosSearch(gt_txt, limit=1).result()["result"][0]
            link = f"https://youtu.be/{search['id']}"
            file_name, vid_title, url, durok, views, uploade_r, meki, data_ytp = (
                await YoutubeDownload(link, as_video=False)
            )
            try:
                audio_original = file_name
                dur = datetime.timedelta(seconds=durok)
            except BaseException as e:
                return await pros.edit(cgr("err").format(em.gagal, str(e)))
            raw_file_name = (
                "".join(random.choice(string.ascii_lowercase) for i in range(5))
                + ".raw"
            )
        else:
            if rep.video:
                await pros.edit_text(f"{em.gagal} **Ga support video bang...**")
                return
            audio = rep.audio
            audio_original = await rep.download()
            vid_title = audio.title if audio.title else audio.file_name
            uploade_r = audio.performer or "**Unknown Artist.**"
            dura_ = audio.duration
            dur = datetime.timedelta(seconds=dura_)
            if audio.thumbs:
                thumb = audio.thumbs[0]
                tumben = thumb.file_id
                meki = await client.download_media(tumben)
            else:
                meki = gbr
            raw_file_name = (
                "".join(random.choice(string.ascii_lowercase) for i in range(5))
                + ".raw"
            )

            url = rep.link
    else:
        search = VideosSearch(gt_txt, limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
        file_name, vid_title, url, durok, views, uploade_r, meki, data_ytp = (
            await YoutubeDownload(link, as_video=False)
        )
        try:
            audio_original = file_name
            dur = datetime.timedelta(seconds=durok)
        except BaseException as e:
            return await pros.edit(cgr("err").format(em.gagal, str(e)))
        raw_file_name = (
            "".join(random.choice(string.ascii_lowercase) for i in range(5)) + ".raw"
        )
    jadul = f'<a href="{url}">{vid_title}</a>'
    try:
        raw_file_name = await convert_to_raw(audio_original, raw_file_name)
    except BaseException as e:
        return await pros.edit(cgr("err").format(em.gagal, e))
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
            return await pros.edit(cgr("err").format(em.gagal, e))
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        plere = """
<u><b>🎼 Sekarang Diputar 🎶</b></u>

**🎵 Judul : {}**
**🎸 Artist : `{}`**
**⏲️️ Durasi : `{}`**
**📩 Permintaan : {}**
        """
        try:
            await message.reply_photo(
                photo=meki,
                caption=plere.format(jadul, uploade_r, dur, org),
                reply_to_message_id=ReplyCheck(message),
            )
        except:
            await message.reply(
                plere.format(jadul, uploade_r, dur, org),
                reply_to_message_id=ReplyCheck(message),
            )
        await pros.delete()
        try:
            os.remove(meki)
        except:
            pass
        return
    elif not group_call.is_connected:
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await pros.edit(cgr("err").format(em.gagal, e))
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        plere = """
<u><b>🎼 Sekarang Diputar 🎶</b></u>

**🎵 Judul : {}**
**🎸 Artist : `{}`**
**⏲️️ Durasi : `{}`**
**📩 Permintaan : {}**
        """
        try:
            await message.reply_photo(
                photo=meki,
                caption=plere.format(jadul, uploade_r, dur, org),
                reply_to_message_id=ReplyCheck(message),
            )
        except:
            await message.reply(
                plere.format(jadul, uploade_r, dur, org),
                reply_to_message_id=ReplyCheck(message),
            )
        await pros.delete()
        try:
            os.remove(meki)
        except:
            pass
        return
    else:
        s_d = stream_vc.get((message.chat.id, client.me.id))
        f_info = {
            "song_name": vid_title,
            "raw": raw_file_name,
            "singer": uploade_r,
            "dur": dur,
            "url": url,
            "thumb": meki,
        }
        if s_d:
            s_d.append(f_info)
        else:
            stream_vc[(message.chat.id, client.me.id)] = [f_info]
        s_d = stream_vc.get((message.chat.id, client.me.id))
        antrek = """
<u><b>➕ Ditambahkan Ke Antrean 📝</b></u>

**🎵 Judul : {}**
**🎸 Artist : `{}`**
**⏲️️ Durasi : `{}`**
**📩 Permintaan : {}**
**🔖 Posisi Ke : #`{}`**
"""
        await message.reply(antrek.format(jadul, uploade_r, dur, org, len(s_d) + 1))
        await pros.delete()
        try:
            os.remove(meki)
        except:
            pass
        return


@ky.ubot("skip", sudo=True)
async def _(client: nlx, message):
    em = Emojik()
    em.initialize()
    m_ = await message.reply(cgr("proses").format(em.proses))
    group_call = play_vc.get((message.chat.id, client.me.id))
    s = stream_vc.get((message.chat.id, client.me.id))
    if not group_call:
        await m_.edit(f"{em.gagal} **Ga lagi memutar musik Goblok!!**")
        return
    if not group_call.is_connected:
        await m_.edit(f"{em.gagal} **Ga lagi memutar musik Goblok!!**")
        return
    if not s:
        await m_.edit(f"{em.gagal} **Kaga ada playlist Goblok!!")
        return
    name_ = s[0]["song_name"]
    singer_ = s[0]["singer"]
    dur = s[0]["dur"]
    next_s = s[0]["raw"]
    link = s[0]["url"]
    thumb_ = s[0]["thumb"]
    s.pop(0)
    group_call.input_filename = next_s
    bij = f'<a href="{link}">{name_}</a>'
    orgu = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
    await m_.edit(f"{em.sukses} **Memutar lagu berikutnya.**")
    nxt_sg = """
<u><b>Memutar Trek Berikutnya</b></u>

**🎵 Judul : {}**
**🎸 Artist : `{}`**
**⏲️️ Durasi : `{}`**
**📩 Permintaan : {}**
"""
    try:
        await message.reply_photo(
            photo=thumb_,
            caption=nxt_sg.format(bij, singer_, dur, orgu),
            reply_to_message_id=ReplyCheck(message),
        )
    except:
        await message.reply(
            nxt_sg.format(bij, singer_, dur, orgu),
            reply_to_message_id=ReplyCheck(message),
        )
    await sleep(2)
    await m_.delete()
    return


@ky.ubot("playlist", sudo=True)
async def _(client: nlx, message):
    em = Emojik()
    em.initialize()
    group_call = play_vc.get((message.chat.id, client.me.id))
    pros = await message.reply(cgr("proses").format(em.gagal))
    song = f"{em.sukses} **Daftar Putar**: \n\n"
    s = stream_vc.get((message.chat.id, client.me.id))
    if not group_call:
        return await pros.edit(f"{em.gagal} **Ga lagi memutar musik Goblok!!**")
    if not s:
        if group_call.is_connected:
            return await pros.edit(
                f"{em.gagal} **Hanya memutar trek saat ini :** `{group_call.song_name}`"
            )
        else:
            return await pros.edit(f"{em.gagal} **Ga lagi memutar musik Goblok!!**")
    if group_call.is_connected:
        song += f"**💿 Sedang Memutar:** `{group_call.song_name}` \n\n"
    for count, i in enumerate(s, start=1):
        song += f"**• {count} ▶ [{i['song_name']}]({i['url']}) | {i['singer']} | `{i['dur']}`** \n"
    await message.reply(song, disable_web_page_preview=True)
    await pros.delete()
    return


@ky.ubot("pause", sudo=True)
async def _(client: nlx, message):
    em = Emojik()
    em.initialize()
    group_call = play_vc.get((message.chat.id, client.me.id))
    if not group_call:
        return await message.reply(f"{em.gagal} **Ga lagi memutar musik Goblok!!**")
    if not group_call.is_connected:
        return await message.reply(f"{em.gagal} **Ga lagi di obrolan suara Goblok!!**")
    await message.reply(f"⏸ **Trek dijeda** {group_call.song_name}.")
    group_call.pause_playout()
    return


@ky.ubot("resume", sudo=True)
async def _(client: nlx, message):
    em = Emojik()
    em.initialize()
    group_call = play_vc.get((message.chat.id, client.me.id))
    if not group_call:
        await message.reply(f"{em.gagal} **Ga lagi memutar musik Goblok!!**")
        return
    if not group_call.is_connected:
        await message.reply(f"{em.gagal} **Ga lagi di obrolan suara Goblok!!**")
        return
    group_call.resume_playout()
    await message.reply(f"▶️ **Trek dilanjutkan** {group_call.song_name}.")
    return


@ky.ubot("end", sudo=True)
async def _(client: nlx, message):
    em = Emojik()
    em.initialize()
    group_call = play_vc.get((message.chat.id, client.me.id))
    if not group_call:
        await message.reply(f"{em.gagal} **Ga lagi memutar musik Goblok!!**")
        return
    if not group_call.is_connected:
        await message.reply(f"{em.gagal} **Ga lagi di obrolan suara Goblok!!**")
        return
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    group_call.stop_playout()
    await message.reply(f"{em.sukses} **Pemutaran dihentikan.**")
    del play_vc[(message.chat.id, client.me.id)]
