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
    if len(m.text.split()) < 1 and not m.reply_to_message:
        return await m.reply("sg username/id/reply")
    if m.reply_to_message:
        args = m.reply_to_message.from_user.id
    else:
        args = m.text.split()[1]
    lol = await m.reply("<code>Processing...</code>")
    if args:
        try:
            user = await c.get_users(f"{args}")
        except Exception:
            return await lol.edit("<code>Please specify a valid user!</code>")
    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)
    try:
        a = await c.send_message(sg, f"{user.id}")
        await a.delete()
    except Exception as e:
        return await lol.edit(e)
    await asyncio.sleep(1)

    async for stalk in c.search_messages(a.chat.id):
        if stalk.text == None:
            continue
        if not stalk:
            await m.reply("botnya ngambek")
        elif stalk:
            await m.reply(f"{stalk.text}")
            break

    try:
        user_info = await c.resolve_peer(sg)
        await c.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await lol.delete()
