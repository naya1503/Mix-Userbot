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
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = c.get_text(m)
    babi = await m.reply(cgr("proses").format(em.proses))
    text, keyboard = text_keyb(ikb, xx)
    if keyboard:
        try:
            x = await c.get_inline_bot_results(bot.me.username, f"buat_button {id(m)}")
            await c.send_inline_bot_result(
                m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=m.id
            )
        except Exception as e:
            await babi.edit(cgr("err").format(em.gagal, e))
            return
    else:
        await m.reply(cgr("butt_1").format(em.gagal))
    await babi.delete()
