import asyncio
import os
from contextlib import suppress
from random import randint
from typing import Optional

import ffmpeg
from pyrogram import enums
from pyrogram.errors import *
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import (CreateGroupCall, DiscardGroupCall,
                                          EditGroupCallTitle)
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat

from Mix import *

__modles__ = "Voicechat"

__help__ = get_cgr("help_vcs")

from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError

vc = None
CLIENT_TYPE = GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
OUTGOING_AUDIO_BITRATE_KBIT = 128
PLAYOUT_FILE = "input.raw"


def init_client(func):
    async def wrapper(client, message):
        global vc
        if not vc:
            vc = GroupCallFactory(
                nlx, CLIENT_TYPE, OUTGOING_AUDIO_BITRATE_KBIT
            ).get_group_call()
            vc.enable_logs_to_console = False
        return await func(client, message)

    return wrapper


async def get_group_call(c: nlx, m, err_msg: str = "") -> Optional[InputGroupCall]:
    em = Emojik()
    em.initialize()
    chat_peer = await c.resolve_peer(m.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await c.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await c.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await m.reply_text(cgr("vc_1").format(em.gagal, err_msg))
    return False


@ky.ubot("startvc", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    flags = " ".join(m.command[1:])
    ky = await m.reply(cgr("proses").format(em.proses))
    if flags == enums.ChatType.CHANNEL:
        chat_id = m.chat.title
    else:
        chat_id = m.chat.id
    args = cgr("vc_2").format(em.sukses)
    try:
        await c.invoke(
            CreateGroupCall(
                peer=(await c.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
            )
        )
        await ky.edit(args)
        return
    except Exception as e:
        await ky.edit(cgr("err").format(em.gagal, e))
        return


@ky.ubot("stopvc", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    ky = await m.reply(cgr("proses").format(em.proses))
    if not (group_call := (await get_group_call(c, m, err_msg=", Kesalahan..."))):
        return
    await c.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(cgr("vc_3").format(em.sukses))
    return


"""
Ini Gw Bikin Dewek Ya Anj, Kalo Masih Dikata Copas Coba Cari Jing. ANAK KONTOL EMANG LOE PADA !!
"""


@ky.ubot("vctitle", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    txt = c.get_arg(m)
    ky = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        await ky.edit(cgr("vc_4").format(em.gagal, m.command))
        return
    if not (group_call := (await get_group_call(c, m, err_msg=", Kesalahan..."))):
        return
    try:
        await c.invoke(EditGroupCallTitle(call=group_call, title=f"{txt}"))
    except Forbidden:
        await ky.edit(cgr("vc_5").format(em.gagal))
        return
    await ky.edit(cgr("vc_6").format(em.sukses, txt))
    return


@ky.ubot("joinvc", sudo=True)
@ky.devs("Jvcs")
@init_client
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()

    ky = await m.reply(cgr("proses").format(em.proses))
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        try:
            await vc.start(chat_id)
            await ky.edit(cgr("vc_7").format(em.sukses, chat_id))
            await asyncio.sleep(2)
            await vc.set_is_mute(True)
            return
        except GroupCallNotFoundError as e:
            return await ky.edit(cgr("err").format(em.gagal, e))


@ky.ubot("leavevc", sudo=True)
@ky.devs("Lvcs")
@init_client
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    ky = await m.reply(cgr("proses").format(em.proses))
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        try:
            await vc.stop()
            await ky.edit(cgr("vc_9").format(em.sukses, chat_id))
            return
        except Exception as e:
            await ky.edit(cgr("err").format(em.gagal, e))
            return
    else:
        return ky.edit(cgr("vc_10").format(em.gagal))


@ky.ubot("play", sudo=True)
@init_client
async def start_playout(_, message):
    if not vc:
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
    vc.input_filename = input_filename


@ky.ubot("volume", sudo=True)
@init_client
async def volume(_, message):
    if len(message.command) < 2:
        await message.edit("<b>You forgot to pass volume [1-200]</b>")
    await vc.set_my_volume(message.command[1])
    await message.edit(
        f"<b>Your volume is set to</b><code> {message.command[1]}</code>"
    )


@ky.ubot("stop", sudo=True)
@init_client
async def stop_playout(_, message):
    vc.stop_playout()
    await message.edit("<b>Stoping successfully!</b>")


@ky.ubot("vmute", sudo=True)
@init_client
async def mute(_, message):
    vc.set_is_mute(True)
    await message.edit("<b>Sound off!</b>")


@ky.ubot("vunmute", sudo=True)
@init_client
async def unmute(_, message):
    vc.set_is_mute(False)
    await message.edit("<b>Sound on!</b>")


@ky.ubot("pause", sudo=True)
@init_client
async def pause(_, message):
    vc.pause_playout()
    await message.edit("<b>Paused!</b>")


@ky.ubot("resume", sudo=True)
@init_client
async def resume(_, message):
    vc.resume_playout()
    await message.edit("<b>Resumed!</b>")
