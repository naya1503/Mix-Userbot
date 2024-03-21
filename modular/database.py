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
__help__ = get_cgr("help_dtbs")


@ky.ubot("setdb", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    jing = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 3:
        return await jing.edit(cgr("dbs_1").format(em.gagal, m.command))
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
    elif variable.lower() == "taglog":
        if value.lower() == "on":
            udB.set_var(c.me.id, "TAG_LOGGER", True)
            await jing.edit(cgr("dbs_10").format(em.sukses, value))
            return
    elif variable.lower() == "pmlog":
        if value.lower() == "on":
            udB.set_var(c.me.id, "PM_LOGGER", True)
            await jing.edit(cgr("dbs_11").format(em.sukses, value))
            return
    else:
        await jing.edit(cgr("dbs_6").format(em.gagal))
        return


@ky.ubot("getdb", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    jing = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        return await jing.edit(cgr("dbs_7").format(em.gagal, m.command))
    command, variable = m.command[:2]
    if variable.lower() == "pmtext":
        bb = udB.get_var(c.me.id, "PMTEXT")
        cc = bb if bb else DEFAULT_TEXT
        teks, button = text_keyb(ikb, cc)
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
            await jing.edit(cgr("dbs_8").format(em.sukses, variable, bb))
            return
    elif variable.lower() == "pmlimit":
        bb = udB.get_var(c.me.id, "PMLIMIT")
        await jing.edit(cgr("dbs_8").format(em.sukses, variable, bb))
        return
    elif variable.lower() == "pmpic":
        bb = udB.get_var(c.me.id, "PMPIC")
        await jing.edit(cgr("dbs_8").format(em.sukses, variable, bb))
        return
    else:
        await jing.edit(cgr("dbs_6").format(em.gagal))
        return


@ky.inline("^get_teks_but")
async def _(c, iq):
    gw = iq.from_user.id
    getpm_txt = udB.get_var(gw, "PMTEXT")
    pm_text = getpm_txt if getpm_txt else DEFAULT_TEXT
    teks, button = text_keyb(ikb, pm_text)
    duar = [
        (
            InlineQueryResultArticle(
                title="Tombol Teks PM!",
                input_message_content=InputTextMessageContent(teks),
                reply_markup=button,
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
        await jing.edit(cgr("dbs_9").format(em.sukses, variable))
        return
    elif variable.lower() == "pmpic":
        udB.remove_var(c.me.id, "PMPIC")
        await jing.edit(cgr("dbs_9").format(em.sukses, variable))
        return
    elif variable.lower() == "alivepic":
        udB.remove_var(c.me.id, "ALIVEPIC")
        await jing.edit(cgr("dbs_9").format(em.sukses, variable))
        return
    elif variable.lower() == "pmtext":
        udB.remove_var(c.me.id, "PMTEXT")
        await jing.edit(cgr("dbs_9").format(em.sukses, variable))
        return
    elif variable.lower() == "taglog":
        udB.remove_var(c.me.id, "TAG_LOGGER")
        await jing.edit(cgr("dbs_9").format(em.sukses, variable))
        return
    elif variable.lower() == "pmlog":
        udB.remove_var(c.me.id, "PM_LOGGER")
        await jing.edit(cgr("dbs_9").format(em.sukses, variable))
        return
    else:
        await jing.edit(cgr("dbs_6").format(em.gagal))
        return
