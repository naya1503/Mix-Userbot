################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from pyrogram.types import *

from Mix import *


@ky.ubot("help", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if not c.get_arg(m):
        try:
            x = await c.get_inline_bot_results(bot.me.username, "help")
            await m.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            await m.reply(error)
    else:
        nama = c.get_arg(m)
        if c.get_arg(m) in CMD_HELP:
            prefix = await c.get_prefix(c.me.id)
            await m.reply(
                CMD_HELP[c.get_arg(m)].__help__.format(next((p) for p in prefix))
                + f"\n<b>© Mix-Userbot - @KynanSupport</b>",
                quote=True,
            )
        else:
            await m.reply(cgr("hlp_1").format(em.gagal, nama))
