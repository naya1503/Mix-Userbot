################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################
import os
from gc import get_objects

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from telegraph import upload_file

from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from Mix.core.waktu import get_time, start_time

from modular.gcast import refresh_dialog

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


# send
@ky.inline("^_send_")
async def send_inline(c, iq):
    try:
        _id = int(iq.query.split()[1])
        m = [obj for obj in get_objects() if id(obj) == _id][0]

        if m.reply_to_message.photo:
            m_d = await m.reply_to_message.download()
            photo_tg = upload_file(m_d)
            cp = m.reply_to_message.caption
            text = cp if cp else ""
            hasil = [
                InlineQueryResultPhoto(
                    photo_url=f"https://telegra.ph/{photo_tg[0]}",
                    title="kon",
                    reply_markup=m.reply_to_message.reply_markup,
                    caption=text,
                ),
            ]
            os.remove(m_d)
        else:
            hasil = [
                InlineQueryResultArticle(
                    title="kon",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ]
        await c.answer_inline_query(
            iq.id,
            cache_time=0,
            results=hasil,
        )
    except Exception as e:
        LOGGER.info(f"Error: {e}")


# alive
@ky.inline("^alive")
async def _(c, iq):
    pmper = None
    stutas = None
    start = datetime.now()
    await user.invoke(Ping(ping_id=0))
    pink = (datetime.now() - start).microseconds / 1000
    upnya = await get_time((time() - start_time))
    ape = await refresh_dialog("group")
    apa = await refresh_dialog("users")
    if user.me.id in DEVS:
        stutas = "<b>Author</b>"
    else:
        stutas = "<b>Connoisseur</b>"
    cekpr = udB.get_var(user.me.id, "PMPERMIT")
    if cekpr:
        pmper = "enable"
    else:
        pmper = "disable"
    txt = f"""
<b>Mix-Userbot</b>
    <b>status:</b> {stutas}
      <b>dc_id:</b> {user.me.dc_id}
      <b>ping_dc:</b> {str(pink).replace('.', ',')} ms
      <b>pmpermit:</b> {pmper}
      <b>peer_users:</b> {len(apa)}
      <b>peer_groups:</b> {len(ape)}
      <b>bot_uptime:</b> {upnya}
"""
    bo_ol = [[InlineKeyboardButton(text="Support", url="t.me/kynansupport")]]
    cekpic = udB.get_var(user.me.id, "ALIVEPIC")
    if not cekpic:
        duar = [
            (
                InlineQueryResultArticle(
                    title="Alive Teks",
                    input_message_content=InputTextMessageContent(txt),
                    reply_markup=InlineKeyboardMarkup(bo_ol),
                )
            )
        ]

    else:
        filem = (
            InlineQueryResultVideo
            if cekpic.endswith(".mp4")
            else InlineQueryResultPhoto
        )
        url_ling = (
            {"video_url": cekpic, "thumb_url": cekpic}
            if cekpic.endswith(".mp4")
            else {"photo_url": cekpic}
        )
        duar = [
            filem(
                **url_ling,
                title="Alive Picture",
                caption=txt,
                reply_markup=InlineKeyboardMarkup(bo_ol),
            )
        ]
    await c.answer_inline_query(iq.id, cache_time=0, results=duar)
