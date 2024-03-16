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
    udB.add_served_nlx(m.from_nlx.id)
    owner_nih = nlx.me.id
    nlx_name = f"<a href='tg://nlx?id={m.from_nlx.id}'>{m.from_nlx.first_name} {m.from_nlx.last_name or ''}</a>"
    nlx2 = f"<a href='tg://nlx?id={nlx.me.id}'>{nlx.me.first_name} {nlx.me.last_name or ''}</a>"
    ts_1 = cgr("asst_1").format(nlx_name)
    ts_2 = cgr("asst_2").format(nlx_name, nlx2)
    if m.from_nlx.id == owner_nih:
        await m.reply(ts_1, reply_markup=clbk_strt())
    else:
        await m.reply(ts_2, reply_markup=clbk_strto())
