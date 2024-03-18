import asyncio
from contextlib import suppress
from random import randint
from typing import Optional

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

vc = None
CLIENT_TYPE = pytgcalls.GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
OUTGOING_AUDIO_BITRATE_KBIT = 128
PLAYOUT_FILE = "Mix/core/vc.raw"


def init_client(func):
    async def wrapper(client, message):
        global vc
        if not vc:
            vc = GroupCallFactory(
                nlx, CLIENT_TYPE, OUTGOING_AUDIO_BITRATE_KBIT
            ).get_file_group_call(PLAYOUT_FILE)
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
        except Exception as e:
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
