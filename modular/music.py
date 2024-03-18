# part of https://github.com/thehamkercat/Telegram_VC_Bot

import asyncio
import os

from pyrogram.errors import *
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.raw.types import InputPeerChannel

import vcmus

vcmus.init()
from vcmus import vcmus

PLAY_LOCK = asyncio.Lock()

from Mix import *
from Mix.core.tools_music import get_default_service, telegram

from .vcs import PLAYOUT_FILE, vc

running = False


@ky.ubot("play")
async def _(_, message):
    global running
    vcmus["call"] = vc
    os.popen(f"cp Mix/core/vc.raw {PLAYOUT_FILE}")
    try:
        usage = f"{message.command} [query]"

        async with PLAY_LOCK:
            if len(message.command) < 2 and not message.reply_to_message:
                return await message.reply_text(usage)
            if "call" not in vcmus:
                try:
                    await vc.start(message.chat.id)
                except Exception:
                    peer = await nlx.resolve_peer(CHAT_ID)
                    startVC = CreateGroupCall(
                        peer=InputPeerChannel(
                            channel_id=peer.channel_id, access_hash=peer.access_hash
                        ),
                        random_id=nlx.rnd_id() // 9000000000,
                    )
                    try:
                        await nlx.send(startVC)
                        await vc.start(message.chat.id)
                    except ChatAdminRequired:
                        del vcmus["call"]
                        await message.reply("Bukan admin!!")
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
