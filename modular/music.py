# memek
import os

import ffmpeg

from Mix import *
from Mix.core.tools_music import *


@ky.ubot("play", sudo=True)
@init_client
async def start_playout(_, message):
    if not group_call:
        await message.reply(
            f"<b>You are not joined [type <code>{message.command}join</code>]</b>"
        )
        return
    if not message.reply_to_message.audio:
        await message.edit("<b>Reply to a message containing audio</b>")
        return
    input_filename = "input.raw"
    await message.edit("<b>Downloading...</b>")
    audio_original = await message.reply_to_message.download()
    await message.edit("<b>Converting..</b>")
    ffmpeg.input(audio_original).output(
        input_filename, format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(audio_original)
    await message.edit(f"<b>Playing {message.reply_to_message.audio.title}</b>...")
    group_call.input_filename = input_filename


@ky.ubot("volume", sudo=True)
@init_client
async def volume(_, message):
    if len(message.command) < 2:
        await message.edit("<b>You forgot to pass volume [1-200]</b>")
    await group_call.set_my_volume(message.command[1])
    await message.edit(
        f"<b>Your volume is set to</b><code> {message.command[1]}</code>"
    )


@ky.ubot("stop", sudo=True)
@init_client
async def stop_playout(_, message):
    group_call.stop_playout()
    await message.edit("<b>Stoping successfully!</b>")


@ky.ubot("vmute", sudo=True)
@init_client
async def mute(_, message):
    group_call.set_is_mute(True)
    await message.edit("<b>Sound off!</b>")


@ky.ubot("vunmute", sudo=True)
@init_client
async def unmute(_, message):
    group_call.set_is_mute(False)
    await message.edit("<b>Sound on!</b>")


@ky.ubot("pause", sudo=True)
@init_client
async def pause(_, message):
    group_call.pause_playout()
    await message.edit("<b>Paused!</b>")


@ky.ubot("resume", sudo=True)
@init_client
async def resume(_, message):
    group_call.resume_playout()
    await message.edit("<b>Resumed!</b>")
