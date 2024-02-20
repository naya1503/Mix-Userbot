################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *

from .pmpermit import DEFAULT_TEXT

__modles__ = "Settings"
__help__ = """
 Help Command Settings

• Perintah: <code>{0}setdb</code> [variable] [value]
• Penjelasan: Untuk mengubah tampilan emoji.

• Perintah: <code>{0}getdb</code>
• Penjelasan: Untuk melihat variabel dan value anda.

• Perintah: <code>{0}deldb</code>
• Penjelasan: Untuk menghapus variabel dan value anda.

• Variabel Yang Bisa Digunakan :

<code>pmtext</code>
<code>pmpic</code>
<code>pmpermit</code>
"""


@ky.ubot("setdb", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    jing = await m.reply(f"{em.proses} <b>Processing...</b>")
    if len(m.command) < 3:
        return await jing.edit(
            f"{em.gagal} <b>Gunakan Format : <code>setdb variable value</code>.</b>"
        )
    command, variable, value = m.command[:3]
    if variable.lower() == "pmpermit":
        if value.lower() == "off":
            udB.remove_var(c.me.id, "PMPERMIT")
            await jing.edit(f"{em.sukses} <b>PMPermit Dimatikan.</b>")
        else:
            udB.set_var(c.me.id, "PMPERMIT", True)
            await jing.edit(f"{em.sukses} <b>PMPermit Dihidupkan.</b>")
    elif variable.lower() == "pmpic":
        if value.lower() == "off":
            udB.remove_var(c.me.id, "PMPIC")
            await jing.edit(f"{em.sukses} <b>PM PIC Dimatikan.</b>")
        else:
            udB.set_var(c.me.id, "PMPIC", value)
            await jing.edit(
                f"{em.sukses} <b>PM PIC Diatur ke : <code>{value}<code>.</b>"
            )
    elif variable.lower() == "pmtext":
        if value.lower() == "clear":
            udB.remove_var(c.me.id, "PMTEXT")
            await jing.edit(f"{em.sukses} <b>PM TEXT Diatur ke Default.</b>")
    else:
        await jing.edit(
            f"{em.gagal} <b>Silakan ketik <code>help {m.command}<code>.</b>"
        )


@ky.ubot("getdb", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    jing = await m.reply(f"{em.proses} <b>Processing...</b>")
    if len(m.command) < 2:
        return await jing.edit(f"{em.gagal} <b>Tidak ada variabel tersebut !!")
    command, variable = m.command[:2]
    if variable.lower() == "pmtext":
        bb = udB.get_var(c.me.id, "PMTEXT")
        cc = bb if bb else DEFAULT_TEXT
        teks, button = parse_button(cc)
        button = build_keyboard(button)
        if button:
            button = InlineKeyboardMarkup(button)
        else:
            button = None
        if button:
            try:
                x = await c.get_inline_bot_results(
                    bot.me.username, f"get_teks_but {m.chat.id}"
                )
                await c.send_inline_bot_result(
                    m.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=ReplyCheck(m),
                )
                await jing.delete()
            except Exception as e:
                await jing.edit(f"Error {e}")
        else:
            await jing.edit(f"{em.sukses} <b>Ini PM Text anda :\n<code>{bb}</code></b>")
    elif variable.lower() == "pmlimit":
        bb = udB.get_var(c.me.id, "PMLIMIT")
        await jing.edit(f"{em.sukses} <b>Ini PM Limit anda :\n<code>{bb}</code></b>")
    elif variable.lower() == "pmpic":
        bb = udB.get_var(c.me.id, "PMPIC")
        await jing.edit(f"{em.sukses} <b>Ini PM Pic anda :\n<code>{bb}</code></b>")
    else:
        await jing.edit(f"{em.gagal} <b>Tidak ada variabel tersebut !!")


@ky.ubot("^get_teks_but")
async def _(c, iq):
    gw = iq.from_user.id
    getpm_txt = udB.get_var(gw, "PMTEXT")
    pm_text = getpm_txt if getpm_txt else DEFAULT_TEXT
    teks, button = parse_button(pm_text)
    button = build_keyboard(button)
    duar = [
        (
            InlineQueryResultArticle(
                title="Tombol Teks PM!",
                input_message_content=InputTextMessageContent(getpm_txt),
                reply_markup=InlineKeyboardMarkup(button),
            )
        )
    ]
    await c.answer_inline_query(iq.id, cache_time=0, results=duar)


@ky.ubot("deldb", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    jing = await m.reply(f"{em.proses} <b>Processing...</b>")
    if len(m.command) < 2:
        return await jing.edit(f"{em.gagal} <b>Tidak ada variabel tersebut !!")
    command, variable = m.command[:2]
    if variable.lower() == "pmpermit":
        udB.remove_var(c.me.id, "PMPERMIT")
        await jing.edit(f"{em.sukses} <b>PMPermit Dimatikan.</b>")
    elif variable.lower() == "pmpic":
        udB.remove_var(c.me.id, "PMPIC")
        await jing.edit(f"{em.sukses} <b>PM PIC Dimatikan.</b>")
    elif variable.lower() == "pmtext":
        udB.remove_var(c.me.id, "PMTEXT")
        await jing.edit(f"{em.sukses} <b>PM TEXT Diatur ke Default.</b>")
    else:
        await jing.edit(
            f"{em.gagal} <b>Silakan ketik <code>help {m.command}<code>.</b>"
        )
