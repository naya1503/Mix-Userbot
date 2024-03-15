from pyrogram import *
from pyrogram.types import *

from Mix import *

__modles__ = "Games"
__help__ = get_cgr("help_games")


@ky.ubot("catur", sudo=True)
async def _(c, m):
    try:
        x = await c.get_inline_bot_results("GameFactoryBot")
        msg = m.reply_to_message or m
        await c.send_inline_bot_result(
            m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await m.reply(error)


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
