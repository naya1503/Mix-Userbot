# part of https://github.com/thehamkercat/Telegram_VC_Bot

import asyncio
import os
import traceback

import aiofiles
import ffmpeg
import youtube_dl
from PIL import Image, ImageDraw, ImageFont
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import EditGroupCallTitle
from Python_ARQ import ARQ

from config import *
from Mix import *
from vcmus import vcmus

from .misc import aiohttpsession as session

arq_api = ndB.get_key("arq_api") or arqapi

arq = ARQ("https://arq.hamker.dev", arq_api, session)
ydl_opts = {"format": "bestaudio", "quiet": True}


def get_default_service() -> str:
    services = ["youtube", "saavn"]
    try:
        config_service = defmus.lower()
        if config_service in services:
            return config_service
        else:
            return "youtube"
    except NameError:
        return "youtube"


async def pause_skip_watcher(message: Message, duration: int):
    try:
        await vcmus["call"].set_is_mute(False)
        if "skipped" not in vcmus:
            vcmus["skipped"] = False
        if "paused" not in vcmus:
            vcmus["paused"] = False
        if "stopped" not in vcmus:
            vcmus["stopped"] = False
        if "replayed" not in vcmus:
            vcmus["replayed"] = False
        restart_while = False
        while True:
            for _ in range(duration * 10):
                if vcmus["skipped"]:
                    vcmus["skipped"] = False
                    return await message.delete()
                if vcmus["paused"]:
                    while vcmus["paused"]:
                        await asyncio.sleep(0.1)
                        continue
                if vcmus["stopped"]:
                    restart_while = True
                    break
                if vcmus["replayed"]:
                    restart_while = True
                    vcmus["replayed"] = False
                    break
                if "queue_breaker" in vcmus:
                    if vcmus["queue_breaker"] != 0:
                        break
                await asyncio.sleep(0.1)
            if not restart_while:
                break
            restart_while = False
            await asyncio.sleep(0.1)
        vcmus["skipped"] = False
    except Exception as e:
        e = traceback.format_exc()
        print(str(e))


async def change_vc_title(m, title: str):
    peer = await nlx.resolve_peer(m.chat.id)
    chat = await nlx.send(GetFullChannel(channel=peer))
    data = EditGroupCallTitle(call=chat.full_chat.call, title=title)
    await nlx.send(data)


def transcode(filename: str):
    ffmpeg.input(filename).output(
        "input.raw",
        format="s16le",
        acodec="pcm_s16le",
        ac=2,
        ar="48k",
        loglevel="error",
    ).overwrite_output().run()
    os.remove(filename)


# Download song
async def download_and_transcode_song(url):
    song = "temp.mp3"
    async with session.get(url) as resp:
        if resp.status == 200:
            f = await aiofiles.open(song, mode="wb")
            await f.write(await resp.read())
            await f.close()
    await run_async(transcode, song)


# Convert seconds to mm:ss
def convert_seconds(seconds: int):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


# Change image size
def changeImageSize(maxWidth: int, maxHeight: int, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def send(*args, **kwargs):
    await nlx.send_message(TAG_LOG, *args, **kwargs)


# Generate cover for youtube


async def generate_cover(msg, requested_by, title, artist, duration, thumbnail):
    async with session.get(thumbnail) as resp:
        if resp.status == 200:
            f = await aiofiles.open("background.png", mode="wb")
            await f.write(await resp.read())
            await f.close()
    background = "./background.png"
    final = "final.png"
    temp = "temp.png"
    image1 = Image.open(background)
    image2 = Image.open("Mix/core/banner.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(temp)
    img = Image.open(temp)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Mix/core/font.otf", 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590),
        f"Duration: {duration}",
        (255, 255, 255),
        font=font,
    )
    draw.text(
        (190, 630),
        f"Artist: {artist}",
        (255, 255, 255),
        font=font,
    )
    draw.text(
        (190, 670),
        f"Requested By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save(final)
    os.remove(temp)
    os.remove(background)
    try:
        await change_vc_title(msg, title)
    except Exception:
        await send(text="[ERROR]: FAILED TO EDIT VC TITLE, MAKE ME ADMIN.")
    return final


async def run_async(func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, func, *args, **kwargs)


async def download_transcode_gencover(
    msg, requested_by, title, artist, duration, thumbnail, url
):
    return await asyncio.gather(
        generate_cover(
            msg,
            requested_by,
            title,
            artist,
            duration,
            thumbnail,
        ),
        download_and_transcode_song(url),
    )


async def get_song(query: str, service: str):
    if service == "saavn":
        resp = await arq.saavn(query)
        if not resp.ok:
            return
        song = resp.result[0]
        title = song.song[0:30]
        duration = int(song.duration)
        thumbnail = song.image
        artist = song.singers if not isinstance(song.singers, list) else song.singers[0]
        url = song.media_url
    elif service == "youtube":
        resp = await arq.youtube(query)
        if not resp.ok:
            return
        song = resp.result[0]
        title = song.title[0:30]
        duration = time_to_seconds(song.duration)
        thumbnail = song.thumbnails[0]
        artist = song.channel
        url = "https://youtube.com" + song.url_suffix
    else:
        return

    return title, duration, thumbnail, artist, url


async def play_song(requested_by, query, message, service):
    m = await message.reply_text(
        f"**Searching for {query} on {service}.**", quote=False
    )
    # get song title, url etc
    song = await get_song(query, service)
    if not song:
        return await m.edit("There's no such song on " + service)

    title, duration, thumbnail, artist, url = song

    if service == "youtube":
        if duration > durasi_musik:
            return await m.edit("[ERROR]: Limited")

        await m.edit("**Generating thumbnail.**")
        cover = await generate_cover(
            message,
            requested_by,
            title,
            artist,
            convert_seconds(duration),
            thumbnail,
        )
        await m.edit("**Downloading**")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        await m.edit("**Transcoding.**")
        song = "audio.webm"
        os.rename(audio_file, song)
        await run_async(transcode, song)

    else:
        await m.edit("**Generating thumbnail, Downloading And Transcoding.**")
        cover, _ = await download_transcode_gencover(
            message,
            requested_by,
            title,
            artist,
            convert_seconds(duration),
            thumbnail,
            url,
        )
    await m.delete()
    caption = f"""
**Name:** {title[:45]}
**Duration:** {convert_seconds(duration)}
**Requested By:** {message.from_user.mention}
**Platform:** {service}
"""
    await m.delete()
    m = await message.reply_photo(
        photo=cover,
        caption=caption,
    )
    os.remove(cover)
    await pause_skip_watcher(m, duration)
    await m.delete()


# Telegram


async def telegram(message):
    err = "**Can't play that**"
    reply = message.reply_to_message
    if not reply:
        return await message.reply_text(err)
    if not reply.audio:
        return await message.reply_text(err)
    if not reply.audio.duration:
        return await message.reply_text(err)
    if int(reply.audio.file_size) > durasi_musik:
        return await message.reply_text("[ERROR]: SONG_TOO_BIG")
    m = await message.reply_text("__**Downloading.**__")
    song = await message.reply_to_message.download()
    await m.edit("__**Transcoding.**__")
    await run_async(transcode, song)
    await m.edit(f"__**Playing {reply.link}**__", disable_web_page_preview=True)
    await pause_skip_watcher(m, reply.audio.duration)
    if os.path.exists(song):
        os.remove(song)
