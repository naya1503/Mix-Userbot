################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Download"
__help__ = "Download"


@ky.ubot("dtik", sudo=False)
async def _(self: user, m):
    em = Emojik()
    em.initialize()
    hm = "luciferbukanrobot_bot"
    await user.unblock_user(hm.me.username)
    await user.send_message(hm.me.username, "/tiktok", {m.command[1]})
    pros = await m.reply(cgr("proses").format(em.proses))
    ai = await user.forward_messages(hm.me.username, m.chat.id, message_ids=m.id)
    await user.send_message(hm.me.username, "/kang", reply_to_message_id=ai.id)
    await asyncio.sleep(5)
    async for tai in user.search_messages(
        hm.me.username, limit=1
    ):
        await asyncio.sleep(5)
        await tai.copy(m.chat.id)
    await pros.delete()
    ulat = await user.resolve_peer(hm.me.username)
    await user.invoke(DeleteHistory(peer=ulat, max_id=0, revoke=True))
    return