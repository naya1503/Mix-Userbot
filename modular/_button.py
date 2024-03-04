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
__help__ = """
 Help Command Button

• Perintah: <code>{0}button</code> [balas pesan]
• Penjelasan: Untuk membuat teks button.

• Silahkan ketik <code>{0}markdown</code> untuk melihat format button.
"""


@ky.ubot("button", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = m.reply_to_message

    babi = await m.reply(f"{em.proses} <b>Processing...</b>")
    teks, button = nan_parse(xx.text)
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
            await babi.edit(f"Error {e}")
            return
    else:
        await m.reply(
            f"{em.gagal} Silahkan ketik `help markdown` untuk melihat format button!"
        )
    await babi.delete()
