################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from pyrogram.enums import *
from pyrogram.types import *

from Mix import *

__modles__ = "Markdown"
__help__ = """
Help Command Markdown

• Perintah: <code>{0}markdown</code>
• Penjelasan: Untuk melihat format button.
"""


def markdown_help():
    return okb(
        [
            [
                ("Markdown Format", "markd.butformat"),
                ("Fillings", "markd.filing"),
            ],
        ],
        True,
        "1_cls",
    )


@ky.ubot("markdown", sudo=True)
async def _(c: user, m):
    try:
        xi = await c.get_inline_bot_results(bot.me.username, "mark_in")
        await m.delete()
        await c.send_inline_bot_result(
            m.chat.id, xi.query_id, xi.results[0].id, reply_to_message_id=ReplyCheck(m)
        )
    except Exception as e:
        await m.edit(f"{e}")
        return


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


@ky.callback("^markd.")
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
        await cq.edit_message_text(
            text=nan, reply_markup=kb, parse_mode=ParseMode.HTML
        )
    elif cmd == "filing":
        nen="""<b>Fillings</b>

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


@ky.callback("^bacek.")
async def _(c, cq):
    txt = "<b>Untuk melihat format markdown silahkan klik tombol dibawah.</b>"
    await cq.edit_message_text(text=txt, reply_markup=markdown_help())
