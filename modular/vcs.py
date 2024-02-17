
__modles__ = "Voicechat"
__help__ = """
 Help Command Voice Chat

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.

• Perintah: <code>{0}joinvc</code>
• Penjelasan: Untuk bergabunf voice chat grup.

• Perintah: <code>{0}leavevc</code>
• Penjelasan: Untuk meninggalkan voice chat grup.
"""

from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from pytgcalls.exceptions import AlreadyJoinedError
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from Mix import *
from team.nandev.class_pytgc import daftar_join

turun_dewek = False



async def get_group_call(
    c, m, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await c.resolve_peer(m.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await c.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await c.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await m.reply_text(f"**No group call Found** {err_msg}")
    return False
    
    
@ky.ubot("startvc", sudo=True)
async def _(c, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    flags = " ".join(m.command[1:])
    ky = await m.reply(f"{emo.proses} <b>Processing....</b>")
    if flags == enums.ChatType.CHANNEL:
        chat_id = m.chat.title
    else:
        chat_id = m.chat.id
    args = f"{emo.sukses} <b>Obrolan Suara Aktif</b>\n<b> Chat : </b><code>{m.chat.title}</code>"
    try:
        await c.invoke(
            CreateGroupCall(peer=(await c.resolve_peer(chat_id)), random_id=randint(10000, 999999999)))
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"{emo.gagal} <b>INFO:</b> `{e}`")


@ky.ubot("stopvc", sudo=True)
async def _(c, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    ky = await m.reply(f"{emo.proses} <b>Processing....</b>")
    m.chat.id
    if not (
        group_call := (await get_group_call(c, m, err_msg=", Kesalahan..."))
    ):
        return
    await c.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(
        f"{emo.gagal} <b>Obrolan Suara Diakhiri</b>\n<b> Chat : </b><code>{m.chat.title}</code>"
    )


@ky.ubot("joinvc", sudo=True)
async def _(c, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    global turun_dewek
    ky = await m.reply(f"{emo.proses} <b>Processing....</b>")
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        file = "core/vc.mp3"
        try:
            daftar_join.append(chat_id)
            if turun_dewek: turun_dewek = False
            await user.call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
            )
            await sleep(2)
            await ky.edit(
                f"{emo.sukses} <b>Berhasil Join Voice Chat</b>\n <b>Chat :</b><code>{m.chat.title}</code>"
            )
            await sleep(1)
        except AlreadyJoinedError:
            await ky.edit(f"{emo.gagal} Akun anda sudah diatas.")
        except Exception as e:
            return await ky.edit(f"{emo.gagal} ERROR: {e}")


@ky.ubot("leavevc", sudo=True)
async def _(c, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    global turun_dewek
    ky = await m.reply(f"{emo.proses} <b>Processing....</b>")
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        try:
            daftar_join.remove(chat_id)
            await user.call_py.leave_group_call(chat_id)
            turun_dewek = True
            await ky.edit(
                f"{emo.suksss} <b>Berhasil Meninggalkan Voice Chat</b>\n <b>Chat :</b><code>{m.chat.title}</code>"
            )
        except Exception as e:
            return await ky.edit(f"{emo.gagal} <b>ERROR:</b> {e}")
