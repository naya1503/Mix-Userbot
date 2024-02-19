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

• Perintah: <code>{0}vctitle</code>
• Penjelasan: Untuk mengubah voice chat grup.
"""

from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, EditGroupCallTitle
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.errors import *
from pytgcalls.exceptions import AlreadyJoinedError
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from Mix import *

from .music import daftar_join


async def get_group_call(c: user, m, err_msg: str = "") -> Optional[InputGroupCall]:
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
    await m.reply_text(f"**No group call Found** {err_msg}")
    return False


@ky.ubot("startvc", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    flags = " ".join(m.command[1:])
    ky = await m.reply(f"{em.proses} <b>Processing....</b>")
    if flags == enums.ChatType.CHANNEL:
        chat_id = m.chat.title
    else:
        chat_id = m.chat.id
    args = f"{em.sukses} <b>Obrolan Suara Aktif</b>\n<b> Chat : </b><code>{m.chat.title}</code>"
    try:
        await c.invoke(
            CreateGroupCall(
                peer=(await c.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
            )
        )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"{em.gagal} <b>INFO:</b> `{e}`")


@ky.ubot("stopvc", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    ky = await m.reply(f"{em.proses} <b>Processing....</b>")
    if not (group_call := (await get_group_call(c, m, err_msg=", Kesalahan..."))):
        return
    await c.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(
        f"{em.gagal} <b>Obrolan Suara Diakhiri</b>\n<b> Chat : </b><code>{m.chat.title}</code>"
    )

@ky.ubot("vctitle", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    txt = c.get_arg(m)
    ky = await m.reply(f"{em.proses} <b>Processing....</b>")
    if len(m.command) < 2:
        await m.reply(f"{em.gagal} <b>Berikan judul voice chat grup.</b>")
        return
    if not (group_call := (await get_group_call(c, m, err_msg=", Kesalahan..."))):
        return
    try:
        await c.send(EditGroupCallTitle(call=group_call, title=f"{txt}"))
    except ChatAdminRequired:
        await m.reply(f"{em.gagal} <b>Anda bukan admin digrup ini.</b>")
        return
    await ky.edit(
        f"{em.gagal} <b>Judul Voice Chat: </b><code>{txt}</code>"
    )

@ky.ubot("joinvc", sudo=True)
async def _(c: user, m):
    global turun_dewek
    em = Emojik()
    em.initialize()

    ky = await m.reply(f"{em.proses} <b>Processing....</b>")
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        file = "Mix/core/vc.mp3"
        try:
            daftar_join.append(chat_id)
            if turun_dewek:
                turun_dewek = False
            await c.call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
            )
            await sleep(2)
            await ky.edit(
                f"{em.sukses} <b>Berhasil Join Voice Chat</b>\n <b>Chat :</b><code>{m.chat.title}</code>"
            )
            await sleep(1)
        except AlreadyJoinedError:
            await ky.edit(f"{em.gagal} Akun anda sudah diatas.")
        except Exception as e:
            return await ky.edit(f"{em.gagal} ERROR: {e}")


@ky.ubot("leavevc", sudo=True)
async def _(c: user, m):
    global turun_dewek
    em = Emojik()
    em.initialize()

    ky = await m.reply(f"{em.proses} <b>Processing....</b>")
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        try:
            daftar_join.remove(chat_id)
            await c.call_py.leave_group_call(chat_id)
            turun_dewek = True
            await ky.edit(
                f"{em.sukses} <b>Berhasil Meninggalkan Voice Chat</b>\n <b>Chat :</b><code>{m.chat.title}</code>"
            )
        except Exception as e:
            await ky.edit(f"{em.gagal} <b>ERROR:</b> {e}")
    else:
        return ky.edit(
            f"{em.gagal} Akun anda sedang tidak berada dalam obrolan {chat_id}."
        )
