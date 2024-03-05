################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from pykeyboard import InlineKeyboard
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
import os
import sys
from Mix import *

from .start import clbk_strt


def st_lang(languages):
    keyboard = InlineKeyboard(row_width=2)
    languages = get_bahasa_()
    for lang in languages:
        buttons = [
            InlineKeyboardButton(
                f"{lang['natively']}",
                callback_data=f"set_{lang['code']}",
            )
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
    op = get_bahasa_()
    okb([[("Back", "clbk.bek")]])
    user_name = f"<a href='tg://user?id={cq.from_user.id}'>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>"
    ts_1 = cgr("asst_1").format(user_name)
    if cmd == "bhsa":
        meki = f"{op[0]['natively']}"
        teks = cgr("asst_4").format(meki)
        await cq.edit_message_text(text=teks, reply_markup=st_lang(op))
    elif cmd == "rebot":
        await cq.edit_message_text(text="Reboot has been initiated successfully! Wait for 1 - 2 minutes until the bot restarts.")
        os.execl(sys.executable, sys.executable, "-m", "Mix")
    elif cmd == "bek":
        txt = "<b>To view markdown format please click the button below.</b>"
        await cq.edit_message_text(text=txt, reply_markup=clbk_strt())


@ky.callback("^set_(.*?)")
async def _(c, cq):
    lang_code = cq.matches[0].group(1)
    op = get_bahasa_()
    meki = f"{op[0]['natively']}"
    kb = okb([[(cgr("balik"), "clbk.bek")]])
    udB.set_lang(lang_code)
    await cq.edit_message_text(cgr("asst_5").format(meki), reply_markup=kb)
