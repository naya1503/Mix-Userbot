################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from gc import get_objects

from pykeyboard import InlineKeyboard
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *

from Mix import *

from .start import clbk_strt


def st_lang(languages):
    keyboard = InlineKeyboard(row_width=2)
    buttons = [
        InlineKeyboardButton(
            f"{lang['natively']} [{lang['code'].lower()}]",
            callback_data=f"set_{lang['code']}",
        )
        for lang in languages
    ]
    for button in buttons:
        keyboard.add(button)
    keyboard.row(
        InlineKeyboardButton(text="Back", callback_data="clbk.bek"),
        InlineKeyboardButton(text="Close", callback_data="close_asst"),
    )
    return keyboard
    
@ky.callback("close_asst")
async def _(c, cq):
    await cq.message.delete()


@ky.callback("clbk.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    languages = get_bahasa_()
    okb([[("Back", "clbk.bek")]])
    if cmd == "bhsa":
        teks = cgr("asst_4")
        await cq.edit_message_text(text=teks, reply_markup=st_lang(languages))
    elif cmd == "bek":
        txt = "<b>To view markdown format please click the button below.</b>"
        await cq.edit_message_text(text=txt, reply_markup=clbk_strt())


@ky.callback("^set_(.*?)")
async def _(c, cq):
    lang_code = cq.matches[0].group(1)
    bhs = get_bahasa_()
    kb = okb([[(cgr("balik"), "clbk.bek")]])
    ndB.set_key("bahasa", lang_code)
    await cq.edit_message_text(cgr("asst_5").format(lang_name), reply_markup=kb)