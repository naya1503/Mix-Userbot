################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from hydrogram import *
from hydrogram.enums import *
from hydrogram.errors import *
from hydrogram.file_id import *
from hydrogram.raw.functions.messages import *
from hydrogram.raw.functions.stickers import *
from hydrogram.raw.types import *
from hydrogram.types import *

from Mix import *


def clbk_strt():
    return okb(
        [
            [
                (cgr("asst_3"), "clbk.bhsa"),
                (cgr("asst_6"), "clbk.rebot"),
            ],
            [
                (cgr("ttup"), "close_asst"),
            ],
        ],
        False,
        "close_asst",
    )


def clbk_strto():
    return okb(
        [
            [
                (cgr("ttup"), "close_asst"),
            ],
        ],
        False,
        "close_asst",
    )


@ky.bots("start", human.pv)
async def _(c, m):
    udB.add_served_user(m.from_user.id)
    owner_nih = nlx.me.id
    user_name = f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name} {m.from_user.last_name or ''}</a>"
    user2 = f"<a href='tg://user?id={nlx.me.id}'>{user.me.first_name} {user.me.last_name or ''}</a>"
    ts_1 = cgr("asst_1").format(user_name)
    ts_2 = cgr("asst_2").format(user_name, user2)
    if m.from_user.id == owner_nih:
        await m.reply(ts_1, reply_markup=clbk_strt())
    else:
        await m.reply(ts_2, reply_markup=clbk_strto())
