################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from pyrogram.types import *
from pyrogram import *
from gc import get_objects
from Mix import *

from .start import clbk_strt

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
