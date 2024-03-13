from pyrogram import *
from pyrogram.types import *

from Mix import *

__modles__ = "Games"
__help__ = get_cgr("help_games")


@ky.ubot("dice", sudo=True)
async def _(c, m):
    await c.send_dice(m.chat.id, "🎲")
    await m.delete()


@ky.ubot("dart", sudo=True)
async def _(c, m):
    await c.send_dice(m.chat.id, "🎯")
    await m.delete()


@ky.ubot("basket", sudo=True)
async def _(c, m):
    await c.send_dice(m.chat.id, "🏀")
    await m.delete()


@ky.ubot("bowling", sudo=True)
async def _(c, m):
    await c.send_dice(m.chat.id, "🎳")
    await m.delete()


@ky.ubot("football", sudo=True)
async def _(c, m):
    await c.send_dice(m.chat.id, "⚽")
    await m.delete()


@ky.ubot("slot", sudo=True)
async def _(c, m):
    await c.send_dice(m.chat.id, "🎰")
    await m.delete()
