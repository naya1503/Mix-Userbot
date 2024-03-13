from pyrogram import *
from pyrogram.types import *

from Mix import *


@ky.ubot("dice", sudo=True)
async def _(c, m):
    chat = m.chat.id
    message = await c.send_dice(chat, "🎲")
    await m.delete()
    # while message.dice.value != 6:
    #     await message.delete()
    #     message = await c.send_dice(chat, "🎲")
