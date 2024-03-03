################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from pyrogram import *
from pyrogram.types import *

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
<code>alivepic</code>
"""


@ky.ubot("setdb", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    jing = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 3:
        return await jing.edit(cgr("dbs_1").format(em.gagal))
    command, variable, value = m.command[:3]
    if variable.lower() == "pmpermit":
        if value.lower() == "on":
            udB.set_var(c.me.id, "PMPERMIT", True)
            await jing.edit(cgr("dbs_2").format(em.sukses))
            return
    elif variable.lower() == "pmpic":
            udB.set_var(c.me.id, "PMPIC", value)
            await jing.edit(cgr("dbs_3").format(em.sukses, value))
            return
    elif variable.lower() == "alivepic":
            udB.set_var(c.me.id, "ALIVEPIC", value)
            await jing.edit(cgr("dbs_4").format(em.sukses, value))
            return
    elif variable.lower() == "pmtext":
        if value.lower() == "clear":
            udB.remove_var(c.me.id, "PMTEXT")
            await jing.edit(cgr("dbs_5").format(em.sukses))
            return
    else:
        await jing.edit(cgr("dbs_6").format(em.gagal))
        return
@ky.ubot("getdb", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    jing = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        return await jing.edit(cgr("dbs_7").format(em.gagal, m.command))
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
                    reply_to_message_id=m.id,
                )
                await jing.delete()
            except Exception as e:
                await jing.edit(f"Error {e}")
        else:
            await jing.edit(cgr("dbs_8").format(em.sukses, variable, bb)
            return
    elif variable.lower() == "pmlimit":
        bb = udB.get_var(c.me.id, "PMLIMIT")
        await jing.edit(cgr("dbs_8").format(em.sukses, variable, bb)
        return
    elif variable.lower() == "pmpic":
        bb = udB.get_var(c.me.id, "PMPIC")
        await jing.edit(cgr("dbs_8").format(em.sukses, variable, bb)
        return
    else:
        await jing.edit(cgr("dbs_6").format(em.gagal)
        return


@ky.inline("^get_teks_but")
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
    jing = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        return await jing.edit(cgr("dbs_6").format(em.gagal))
    command, variable = m.command[:2]
    if variable.lower() == "pmpermit":
        udB.remove_var(c.me.id, "PMPERMIT")
        await jing.edit(cgr("dbs_9").format(em.sukses, variabel)
        return
    elif variable.lower() == "pmpic":
        udB.remove_var(c.me.id, "PMPIC")
        await jing.edit(cgr("dbs_9").format(em.sukses, variabel)
        return
    elif variable.lower() == "alivepic":
        udB.remove_var(c.me.id, "ALIVEPIC")
        await jing.edit(cgr("dbs_9").format(em.sukses, variabel)
        return
    elif variable.lower() == "pmtext":
        udB.remove_var(c.me.id, "PMTEXT")
        await jing.edit(cgr("dbs_9").format(em.sukses, variabel)
        return
    else:
        await jing.edit(cgr("dbs_6").format(em.gagal))
        return
