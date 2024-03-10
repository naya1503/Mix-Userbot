import asyncio
import random

from pyrogram import *
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import *

from Mix import *

__modles__ = "SangMata"
__help__ = "SangMata"


@ky.ubot("sg", sudo=True)
@ky.devs("siapa")
async def _(c, m):
    em = Emojik()
    em.initialize()
    if len(m.command) < 2 and not m.reply_to_message:
        return await m.reply(f"{em.gagal} <b>sg username/id/reply</b>")
    if m.reply_to_message:
        args = m.reply_to_message.from_user.id
    else:
        args = m.command[1]
    proses = await m.reply(f"{em.proses} <b>Processing...</b>")
    if args:
        try:
            user = await c.get_users(f"{args}")
        except Exception:
            return await proses.edit(f"{em.gagal} <b>Please specify a valid user!</b>")
    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)
    try:
        a = await c.send_message(sg, f"{user.id}")
        await a.delete()
    except Exception as e:
        return await proses.edit(e)
    await asyncio.sleep(1)

    async for stalk in c.search_messages(a.chat.id):
        if stalk.text == None:
            continue
        if not stalk:
            await m.reply(f"{em.gagal} <b>botnya ngambek :( </b>")
        elif stalk:
            await m.reply(f"{em.sukses} <code>{stalk.text}</code>")
            break

    try:
        user_info = await c.resolve_peer(sg)
        await c.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await proses.delete()
