################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *
from pyrogram.types import *
from .start import clbk_strt

@ky.callback("close_asst")
async def _(c, cq):
    await cq.message.delete()

@ky.callback("clbk.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    kb = okb([[("Kembali", "clbk.bek")]])
    ck_bhs = udB.get_key("bahasa")
    bhs = get_bahasa_()
    buttons = [
        [
            InlineKeyboardButton(
                f"{bhs[lang]['penulis']} [{lang.lower()}]",
                callback_data=f"set_{lang}"
            )
        ]
        for lang in bhs
    ]
    buttons.append([InlineKeyboardButton(cgr("balik"), callback_data="clbk.bek")])
    if cmd == "bhsa":
        teks = cgr("asst_4").format(bhs['nama'])
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
    await cq.edit_message_text(cgr("asst_5").format(bhs[lang]['penulis'][lang]), reply_markup=kb)
       