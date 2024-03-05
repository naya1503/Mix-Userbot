################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################
from gc import get_objects

from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *

from Mix import *
from modular.copy_con import *
from modular.pmpermit import *

# button


@ky.inline("^dibikin_button")
async def _(c, iq):
    _id = int(iq.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    rep = m.reply_to_message
    teks, button = parse_button(rep.text)
    button = build_keyboard(button)
    duar = [
        (
            InlineQueryResultArticle(
                title="Tombol Teks!",
                input_message_content=InputTextMessageContent(teks),
                reply_markup=InlineKeyboardMarkup(button),
            )
        )
    ]
    await c.answer_inline_query(iq.id, cache_time=0, results=duar)


# markdown


@ky.inline("^mark_in")
async def _(c, iq):
    txt = "<b>Untuk melihat format markdown silahkan klik tombol dibawah.</b>"
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Marketing!",
                    reply_markup=markdown_help(),
                    input_message_content=InputTextMessageContent(txt),
                )
            )
        ],
    )


# help


@ky.inline("^help")
async def _(c, iq):
    user_id = iq.from_user.id
    emut = await user.get_prefix(user_id)
    msg = (
        "<b>Commands\n      Prefixes: `{}`\n      Modules: <code>{}</code></b>".format(
            " ".join(emut), len(CMD_HELP)
        )
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


# copy


@ky.inline("^get_msg")
async def _(c, iq):
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="message",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text=cgr("klk_1"),
                                    callback_data=f"copymsg_{int(iq.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTexxxessageContent(cgr("cpy_3")),
                )
            )
        ],
    )


# pmpermit
