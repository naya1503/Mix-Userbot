################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import os
from gc import get_objects

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from telegraph import upload_file

from Mix import *

COPY_ID = {}

nyolong_jalan = False


def clbk_strt():
    return okb(
        [
            [
                (cgr("asst_3"), "clbk.bhsa"),
            ],
        ],
        False,
        "close_asst",
    )


def clbk_strto():
    return okb(
        [
            [
                (cgr("ttup"), "clbk.info"),
            ],
        ],
        False,
        "close_asst",
    )


@ky.bots("start")
async def _(c, m):
    udB.add_served_user(m.from_user.id)
    owner_nih = user.me.id
    user_name = f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name} {m.from_user.last_name or ''}</a>"
    ts_1 = cgr("asst_1").format(user_name)
    ts_2 = cgr("asst_2").format(user_name, user.me.mention)
    if m.from_user.id == owner_nih:
        await m.reply(ts_1, reply_markup=clbk_strt())
    else:
        await m.reply(ts_2, reply_markup=clbk_strto())


@ky.bots("copy")
async def _(c, m):
    if m.from_user.id != user.me.id:
        return
    xx = await m.reply("Tunggu Sebentar...")
    link = user.get_arg(m)
    if not link:
        return await xx.edit(f"<b><code>{m.text}</code> [link]</b>")
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            g = await c.get_messages(chat, msg_id)
            await g.copy(m.chat.id)
            await xx.delete()
        except Exception as error:
            await xx.edit(error)
    else:
        await xx.edit("Link tidak valid.")


# @Tomi


@ky.ubot("send", sudo=True)
async def _(c: user, m):
    if m.reply_to_message:
        chat_id = m.chat.id if len(m.command) < 2 else m.text.split()[1]
        try:
            if c.me.id != bot.me.id:
                if m.reply_to_message.reply_markup:
                    x = await c.get_inline_bot_results(
                        bot.me.username, f"_send_ {id(m)}"
                    )
                    return await c.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await m.reply(error)
        else:
            try:
                return await m.reply_to_message.copy(chat_id)
            except Exception as t:
                return await m.reply(f"{t}")
    else:
        if len(m.command) < 3:
            return
        chat_id, chat_text = m.text.split(None, 2)[1:]
        try:
            if "/" in chat_id:
                to_chat, msg_id = chat_id.split("/")
                return await c.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
            else:
                return await c.send_message(chat_id, chat_text)
        except Exception as t:
            return await m.reply(f"{t}")


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
