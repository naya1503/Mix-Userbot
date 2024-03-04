################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *
from pyrogram.types import *

def clbk_strt():
    return okb(
        [
            [
                (cgr("asst_3"), "clbk.bhsa"),
            ],
        ],
        False,
        "close_asst",
    )


def clbk_strto():
    return okb(
        [
            [
                (cgr("asst_3"), "clbk.info"),
            ],
        ],
        False,
        "close_asst",
    )


@ky.bots("start")
async def _(c, m):
    udB.add_served_user(m.from_user.id)
    owner_nih = user.me.id
    if m.from_user.id == owner_nih:
        await m.reply(cgr("asst_1"), reply_markup=clbk_strt())
    else:
        await m.reply(cgr("asst_2"), reply_markup=clbk_strto())
