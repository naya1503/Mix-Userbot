# part of https://github.com/thehamkercat/Telegram_VC_Bot

import asyncio

import pytgcalls
from pyrogram.errors import *

import vcmus

vcmus.init()
from vcmus import vcmus

PLAY_LOCK = asyncio.Lock()

from Mix import *
from Mix.core.tools_music import get_default_service, play_song, telegram

from .vcs import CLIENT_TYPE, OUTGOING_AUDIO_BITRATE_KBIT, PLAYOUT_FILE

running = False


async def start_queue(message=None):
    while vcmus:
        if "queue_breaker" in vcmus and vcmus.get("queue_breaker") != 0:
            vcmus["queue_breaker"] -= 1
            if vcmus["queue_breaker"] == 0:
                del vcmus["queue_breaker"]
            break
        if vcmus["queue"].empty():
            if "playlist" not in vcmus or not vcmus["playlist"]:
                vcmus["running"] = False
                break
            else:
                await playlist(nlx, message, redirected=True)
        data = await vcmus["queue"].get()
        service = data["service"]
        if service == "telegram":
            await telegram(data["message"])
        else:
            await play_song(
                data["requested_by"],
                data["query"],
                data["message"],
                service,
            )


@ky.ubot("joinos")
async def joinvc(_, message, manual=False):
    if "call" in vcmus:
        return await message.reply_text("__**Bot Is Already In The VC**__")
    os.popen(f"cp Mix/core/vc.raw {PLAYOUT_FILE}")
    vc = pytgcalls.GroupCallFactory(
        nlx, CLIENT_TYPE, OUTGOING_AUDIO_BITRATE_KBIT
    ).get_file_group_call(PLAYOUT_FILE)
    vcmus["call"] = vc
    try:
        await vc.start(message.chat.id)
    except Exception:
        peer = await nlx.resolve_peer(message.chat.id)
        startVC = CreateGroupCall(
            peer=InputPeerChannel(
                channel_id=peer.channel_id,
                access_hash=peer.access_hash,
            ),
            random_id=nlx.rnd_id() // 9000000000,
        )
        try:
            await nlx.send(startVC)
            await vc.start(message.chat.id)
        except ChatAdminRequired:
            del vcmus["call"]
            return await message.reply_text(
                "Make me admin with message delete and vc manage permission"
            )
    await message.reply_text(
        "__**Joined The Voice Chat.**__ \n\n**Note:** __If you can't hear anything,"
        + " Send /leavevc and then /joinvc again.__"
    )
    await message.delete()


@ky.ubot("play")
async def _(_, message):
    global running
    try:
        usage = f"{message.command} [query]"

        async with PLAY_LOCK:
            if len(message.command) < 2 and not message.reply_to_message:
                return await message.reply_text(usage)
            # if "call" not in vcmus:
            # await vc.start(message.chat.id)
            if message.reply_to_message:
                if message.reply_to_message.audio:
                    service = "telegram"
                    song_name = message.reply_to_message.audio.title
                else:
                    return await message.reply_text(
                        "**Reply to a telegram audio file**"
                    )
            else:
                text = message.text.split("\n")[0]
                text = text.split(None, 2)[1:]
                service = text[0].lower()
                services = ["youtube", "saavn"]
                if service in services:
                    song_name = text[1]
                else:
                    service = get_default_service()
                    song_name = " ".join(text)
                if "http" in song_name or ".com" in song_name:
                    return await message.reply("Links aren't supported.")

            requested_by = message.from_user.first_name
            if "queue" not in vcmus:
                vcmus["queue"] = asyncio.Queue()
            if not vcmus["queue"].empty() or vcmus.get("running"):
                await message.reply_text("__**Added To Queue.__**")

            await vcmus["queue"].put(
                {
                    "service": service or telegram,
                    "requested_by": requested_by,
                    "query": song_name,
                    "message": message,
                }
            )
        if not vcmus.get("running"):
            vcmus["running"] = True
            await start_queue()
    except Exception as e:
        await message.reply_text(str(e))


async def playlist(_, message: Message, redirected=False):
    if message.reply_to_message:
        raw_playlist = message.reply_to_message.text
    elif len(message.text) > 9:
        raw_playlist = message.text[10:]
    else:
        usage = """
**Usage: Same as /play
Example:
    __**/playlist song_name1
    song_name2
    youtube song_name3**__"""

        return await message.reply_text(usage)
    if "call" not in vcmus:
        return await message.reply_text("**Use /joinvc First!**")
    if "playlist" not in vcmus:
        vcmus["playlist"] = False
    if "running" in vcmus and vcmus.get("running"):
        vcmus["queue_breaker"] = 1
    vcmus["playlist"] = True
    vcmus["queue"] = asyncio.Queue()
    for line in raw_playlist.split("\n"):
        services = ["youtube", "saavn"]
        if line.split()[0].lower() in services:
            service = line.split()[0].lower()
            song_name = " ".join(line.split()[1:])
        else:
            service = "youtube"
            song_name = line
        requested_by = message.from_user.first_name
        await vcmus["queue"].put(
            {
                "service": service or telegram,
                "requested_by": requested_by,
                "query": song_name,
                "message": message,
            }
        )
    if not redirected:
        vcmus["running"] = True
        await message.reply_text("**Playlist Started.**")
        await start_queue(message)
