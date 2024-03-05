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

from .start import clbk_strt


def markdown_help():

    return okb(
        [
            [
                ("Markdown Format", "markd.butformat"),
                ("Fillings", "markd.filing"),
            ],
        ],
        True,
        "help_back",
    )


def sini_croot():
    keyboard = InlineKeyboard(row_width=1)
    keyboard.row(
        InlineKeyboardButton(text="English", callback_data=f"bahasa_:en"),
        InlineKeyboardButton(text="Indonesia", callback_data=f"bahasa_:id"),
    )
    keyboard.row(
        InlineKeyboardButton(cgr("balik"), callback_data="clbk.bek"),
    )
    return keyboard


@ky.inline("^dibikin_button")
async def _(c, iq):

    # iq.from_user.id
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


@ky.callback("^cls_hlp")
async def _(_, cq):
    unPacked = unpackInlineMessage(cq.inline_message_id)
    if cq.from_user.id == user.me.id:
        await user.delete_messages(unPacked.chat_id, unPacked.message_id)
    else:
        await cq.answer(
            f"Jangan Di Pencet Anjeng.",
            True,
        )
        return


@ky.callback("close_asst")
async def _(c, cq):
    await cq.message.delete()


@ky.callback("clbk.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    okb([[("Kembali", "clbk.bek")]])
    languages = get_bahasa_()
    chs = f"{languages[mx]['natively']} [{mx.lower()}]"
    tultd = [InlineKeyboardButton(f"{chs}", callback_data=f"set_{chs}")]
    buttons = list(zip(tultd[::2], tultd[1::2]))
    if len(tultd) % 2 == 1:
        buttons.append((tultd[-1],))
    if cmd == "bhsa":
        teks = cgr("asst_4")
        await cq.edit_message_text(
            text=teks, reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif cmd == "bek":
        txt = "<b>Untuk melihat format markdown silahkan klik tombol dibawah.</b>"
        await cq.edit_message_text(text=txt, reply_markup=clbk_strt())


@ky.callback("^set_:(.*?)")
async def _(c, cq):
    lang = query.matches[0].group(1)
    bhs = get_bahasa_()
    kb = okb([[(cgr("balik"), "clbk.bek")]])
    if lang == "en":
        ndB.del_key("bahasa")
    else:
        ndB.set_key("bahasa", lang)
    await cq.edit_message_text(cgr("asst_5").format(bhs["name"]), reply_markup=kb)


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


@ky.callback("markd.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    kb = okb([[("Kembali", "bace.markd")]])
    if cmd == "butformat":
        nan = """<b>Markdown Formatting</b>
<b>Anda dapat memformat pesan Anda menggunakan <b>tebal</b>, <i>miring</i>, <u>garis bawah</u>, <strike>coret</strike>, dan banyak lagi.</b>

<code>`kata kode`</code>: Tanda kutip terbalik digunakan untuk font monospace. Ditampilkan sebagai: <code>kata kode</code>.
<code>__miring__</code>: Garis bawah digunakan untuk font miring. Ditampilkan sebagai: <i>kata miring</i>.
<code>**tebal**</code>: Asterisk digunakan untuk font tebal. Ditampilkan sebagai: <b>kata tebal</b>.
<code>--garis bawah--</code>: Untuk membuat teks <u>garis bawah</u>.
<code>~~coret~~</code>: Tilda digunakan untuk strikethrough. Ditampilkan sebagai: <strike>coret</strike>.
<code>||spoiler||</code>: Garis vertikal ganda digunakan untuk spoiler. Ditampilkan sebagai: <spoiler>Spoiler</spoiler>.
<code>[hyperlink](contoh)</code>: Ini adalah pemformatan yang digunakan untuk hyperlink. Ditampilkan sebagai: <a href="https://example.com/">hyperlink</a>.
<code>[Tombol Saya](buttonurl://contoh)</code>: Ini adalah pemformatan yang digunakan untuk membuat tombol.
Jika Anda ingin mengirimkan tombol dalam satu baris yang sama, gunakan pemformatan <code>:same</code>.
<b>Contoh:</b>
<code>[tombol 1](buttonurl://1)</code>
<code>[tombol 2](buttonurl://2:same)</code>
<code>[tombol 3](buttonurl://3)</code>
Ini akan menampilkan tombol 1 dan 2 di baris yang sama, sementara 3 akan berada di bawahnya."""
        await cq.edit_message_text(text=nan, reply_markup=kb, parse_mode=ParseMode.HTML)
    elif cmd == "filing":
        nen = """<b>Fillings</b>

Anda juga dapat menyesuaikan isi pesan Anda dengan data kontekstual. Misalnya, Anda bisa menyebut nama pengguna dalam pesan selamat datang, atau menyebutnya dalam filter!

<b>Isian yang didukung:</b>

<code>{first}</code>: Nama depan pengguna.
<code>{last}</code>: Nama belakang pengguna.
<code>{fullname}</code>: Nama lengkap pengguna.
<code>{username}</code>: Nama pengguna pengguna. Jika mereka tidak memiliki satu, akan menyebutkan pengguna tersebut.
<code>{mention}</code>: Menyebutkan pengguna dengan nama depan mereka.
<code>{id}</code>: ID pengguna.
<code>{chatname}</code>: Nama obrolan."""
        await cq.edit_message_text(
            text=nen,
            reply_markup=kb,
            parse_mode=ParseMode.HTML,
        )


@ky.callback("bace")
async def _(c, cq):
    txt = "<b>Untuk melihat format markdown silahkan klik tombol dibawah.</b>"
    await cq.edit_message_text(text=txt, reply_markup=markdown_help())


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
    top_text = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
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


@ky.callback("copymsg_")
async def _(c, cq):
    global nyolong_jalan
    try:
        q = int(cq.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        await m._c.unblock_user(bot.me.username)
        await cq.edit_message_text(cgr("proses_1"))
        copy = await m._c.send_message(bot.me.username, f"/copy {m.text.split()[1]}")
        msg = m.reply_to_message or m
        await asyncio.sleep(1.5)
        await copy.delete()
        nyolong_jalan = True
        async for g in m._c.search_messages(bot.me.username, limit=1):
            await m._c.copy_message(
                m.chat.id, bot.me.username, g.id, reply_to_message_id=msg.id
            )
            await m._c.delete_messages(m.chat.id, COPY_ID[m._c.me.id])
            await g.delete()
            nyolong_jalan = False
    except Exception as e:
        await callback_query.edit_message_text(cgr("err_1").format(e))
