################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from pyrogram import *
from pyrogram.types import *

from Mix import *

__modles__ = "Button"
__help__ = get_cgr("help_butt")


@ky.ubot("button", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = m.reply_to_message

    babi = await m.reply(cgr("proses").format(em.proses))
    teks, button = parse_button(xx.text)
    button = build_keyboard(button)
    if button:
        button = InlineKeyboardMarkup(button)
    else:
        button = None
    if button:
        try:
            x = await c.get_inline_bot_results(
                bot.me.username, f"dibikin_button {id(m)}"
            )
            await c.send_inline_bot_result(
                m.chat.id,
                x.query_id,
                x.results[0].id,
                reply_to_message_id=m.id,
            )

        except Exception as e:
            await babi.edit(cgr("err").format(em.gagal, e))
            return
    else:
        await m.reply(cgr("butt_1").format(em.gagal))
    await babi.delete()


@ky.ubot("button2", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = m.reply_to_message

    babi = await m.reply(cgr("proses").format(em.proses))
    teks, button = parse_button(xx.text)
    button = build_keyboard(button)
    if button:
        button = InlineKeyboardMarkup(button)
    else:
        button = None
    if button:
        try:
            x = await c.get_inline_bot_results(
                bot.me.username, f"dibikin_button2 {id(m)}"
            )
            await c.send_inline_bot_result(
                m.chat.id,
                x.query_id,
                x.results[0].id,
                reply_to_message_id=m.id,
            )

        except Exception as e:
            await babi.edit(cgr("err").format(em.gagal, e))
            return
    else:
        await m.reply(cgr("butt_1").format(em.gagal))
    await babi.delete()
