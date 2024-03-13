from pyrogram import *
from pyrogram.types import *

from Mix import *


@ky.ubot("dice", sudo=True)
async def _(c, m):
    six = (m.from_user.id in DEVS) if m.from_user else False

    c = m.chat.id
    if not six:
        return await c.send_dice(c, "🎲")

    m = await c.send_dice(c, "🎲")

    while m.dice.value != 6:
        await m.delete()
        m = await c.send_dice(c, "🎲")
