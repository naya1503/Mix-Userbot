################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import os
import sys

from pykeyboard import InlineKeyboard
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *

from Mix import *

from .start import clbk_strt


def st_lang():
    keyboard = InlineKeyboard(row_width=2)
    languages = get_bahasa_()
    keyboard.add(
        *[
            (
                InlineKeyboardButton(
                    f"{lang['natively']}",
                    callback_data=f"set_{lang['code']}",
                )
            )
            for lang in languages
        ]
    )
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
    if cq.from_user.id != nlx.me.id:
        await cq.answer("Lu Siapa Si Memeg??", True)
        return
    cmd = cq.data.split(".")[1]
    op = get_bahasa_()
    user_name = f"<a href='tg://user?id={cq.from_user.id}'>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>"
    if cmd == "bhsa":
        meki = f"{op[0]['natively']}"
        teks = cgr("asst_4").format(meki)
        await cq.edit_message_text(text=teks, reply_markup=st_lang())
    elif cmd == "rebot":
        await cq.edit_message_text(cgr("reboot_1"))
        os.execl(sys.executable, sys.executable, "-m", "Mix")
    elif cmd == "bek":
        ts_1 = cgr("asst_1").format(user_name)
        await cq.edit_message_text(text=ts_1, reply_markup=clbk_strt())


@ky.callback("^set_(.*?)")
async def _(c, cq):
    lang_code = cq.data.split("_")[1]
    op = get_bahasa_()
    sl = next((ox for ox in op if ox["code"] == lang_code), None)
    kb = okb([[(cgr("balik"), "clbk.bek")]])
    if sl:
        ndB.set_key("bahasa", lang_code)
        await cq.edit_message_text(
            cgr("asst_5").format(sl["natively"]), reply_markup=kb
        )
    else:
        LOGGER.error(f"Language with code '{lang_code}' not found.")
