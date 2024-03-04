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


@ky.inline("^dibikin_button")
async def _(c, iq):

    # iq.from_user.id
    _id = int(iq.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    rep = m.reply_to_message
    teks, button = nan_parse(rep.text)
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
    udB.get_key("bahasa")
    bhs = get_bahasa_()
    buttons = [
        [
            InlineKeyboardButton(
                f"{bhs[lang]['penulis']} [{lang.lower()}]", callback_data=f"set_{lang}"
            )
        ]
        for lang in bhs
    ]
    buttons.append([InlineKeyboardButton(cgr("balik"), callback_data="clbk.bek")])
    if cmd == "bhsa":
        teks = cgr("asst_4").format(bhs["nama"])
        await cq.edit_message_text(text=teks, reply_markup=buttons)
    elif cmd == "bek":
        txt = "<b>Untuk melihat format markdown silahkan klik tombol dibawah.</b>"

        await cq.edit_message_text(text=txt, reply_markup=clbk_strt())


@ky.callback("^set_(.*)$")
async def _(c, cq):
    lang = query.matches[0].group(1)
    bhs = get_bahasa_()
    kb = okb([[(cgr("balik"), "clbk.bek")]])
    if lang == "en":
        ndB.del_key("bahasa")
    else:
        ndB.set_key("bahasa", lang)
    await cq.edit_message_text(
        cgr("asst_5").format(bhs[lang]["penulis"][lang]), reply_markup=kb
    )


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
