################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import re

from pyrogram.types import *

from Mix import *


@ky.ubot("help", sudo=True)
async def _(c: user, m):
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
            await m.reply(f"<b>Tidak ada modul bernama <code>{nama}</code></b>")


@ky.inline("^help")
async def _(c, iq):
    user_id = iq.from_user.id
    emut = await user.get_prefix(user_id)
    msg = "<b>Help Commands\n     Prefixes: `{}`\n    Modules: <code>{}</code></b>".format(
        " ".join(emut), len(CMD_HELP)
    )
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    description=f"Menu Bantuan",
                    thumb_url="https://telegra.ph//file/57376cf2486052ffae0ad.jpg",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, CMD_HELP, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


@ky.callback("help_(.*?)")
async def _(c, cq):
    mod_match = re.match(r"help_module\((.+?)\)", cq.data)
    prev_match = re.match(r"help_prev\((.+?)\)", cq.data)
    next_match = re.match(r"help_next\((.+?)\)", cq.data)
    back_match = re.match(r"help_back", cq.data)
    user_id = cq.from_user.id
    prefix = await user.get_prefix(user_id)
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = f"<b>{CMD_HELP[module].__help__}</b>\n".format(next((p) for p in prefix))
        button = [[InlineKeyboardButton("≪", callback_data="help_back")]]
        await cq.edit_message_text(
            text=text + f"\n<b>© Mix-Userbot - @KynanSupport</b>",
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    top_text = "<b>Help Commands\n    Prefixes: <code>{}</code>\n     Modules: <code>{}</code></b>".format(
        " ".join(prefix), len(CMD_HELP)
    )

    if prev_match:
        curr_page = int(prev_match.group(1))
        await cq.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        next_page = int(next_match.group(1))
        await cq.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        await cq.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, CMD_HELP, "help")),
            disable_web_page_preview=True,
        )
