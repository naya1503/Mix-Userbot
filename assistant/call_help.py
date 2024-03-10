################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from time import time

import psutil
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *

from Mix import *
from Mix.core.waktu import get_time, start_time


def clbk_stasm():
    return okb(
        [
            [
                (cgr("ttup"), "cls_hlp"),
            ],
        ],
        False,
        "close_asst",
    )


@ky.callback(("stats_mix"))
async def _(c, cq):

    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
**Uptime:** `{uptime}`
**Bot:** `{round(process.memory_info()[0] / 1024 ** 2)} MB`
**Cpus:** `{cpu}%`
**Ram:** `{mem}%`
**Disk:** `{disk}%`
**Modules:** `{len(CMD_HELP)}`
"""
    await cq.edit_message_text(stats, reply_markup=clbk_stasm())


@ky.callback("help_(.*?)")
async def _(c, cq):
    mod_match = re.match(r"help_module\((.+?)\)", cq.data)
    prev_match = re.match(r"help_prev\((.+?)\)", cq.data)
    next_match = re.match(r"help_next\((.+?)\)", cq.data)
    back_match = re.match(r"help_back", cq.data)
    user_id = cq.from_user.id
    prefix = await user.get_prefix(user_id)

    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = f"<b>{CMD_HELP[module].__help__}</b>\n".format(next((p) for p in prefix))
        button = okb([[("≪", "help_back")]])
        if "Animasi" in text:
            text1 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
                " ".join(prefix), len(CMD_HELP)
            )
            button = okb(
                [
                    [
                        ("Animasi 1", "anim.anm1"),
                        ("Animasi 2", "anim.anm2"),
                    ],
                    [
                        ("Animasi 3", "anim.anm3"),
                        ("Animasi 4", "anim.anm4"),
                    ],
                    [
                        ("≪", "help_back"),
                    ],
                ]
            )
        elif "Toxic" in text:
            text1 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
                " ".join(prefix), len(CMD_HELP)
            )
            button = okb(
                [
                    [
                        ("Toxic 1", "to.tox1"),
                        ("Toxic 2", "to.tox2"),
                    ],
                    [
                        ("Toxic 3", "to.tox3"),
                        ("Toxic 4", "to.tox4"),
                    ],
                    [
                        ("≪", "help_back"),
                        ("⪼", "to.next"),
                    ],
                ]
            )
            await cq.edit_message_text(
                text=text1, reply_markup=button, disable_web_page_preview=True
            )
        else:
            await cq.edit_message_text(
                text=text + f"\n<b>© Mix-Userbot - @KynanSupport</b>",
                reply_markup=button,
                disable_web_page_preview=True,
            )

    if prev_match:
        t1 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        curr_page = int(prev_match.group(1))
        await cq.edit_message_text(
            text=t1,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        t2 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        next_page = int(next_match.group(1))
        await cq.edit_message_text(
            text=t2,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        t3 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        await cq.edit_message_text(
            text=t3,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, CMD_HELP, "help")),
            disable_web_page_preview=True,
        )


@ky.callback("^anim.")
async def _(c, cq):
    colmek = cq.data.split(".")[1]
    kemem = okb([[("≪", "anim.bc")]])
    user_id = cq.from_user.id
    prefix = await user.get_prefix(user_id)
    txt = None
    if colmek == "anm1":
        txt = get_cgr("help_anm1").format(next((p) for p in prefix))
    elif colmek == "anm2":
        txt = get_cgr("help_anm2").format(next((p) for p in prefix))
    elif colmek == "anm3":
        txt = get_cgr("help_anm3").format(next((p) for p in prefix))
    elif colmek == "anm4":
        txt = get_cgr("help_anm4").format(next((p) for p in prefix))
    elif colmek == "bc":
        txt = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        kemem = okb(
            [
                [
                    ("Animasi 1", "anim.anm1"),
                    ("Animasi 2", "anim.anm2"),
                ],
                [
                    ("Animasi 3", "anim.anm3"),
                    ("Animasi 4", "anim.anm4"),
                ],
                [
                    ("≪", "help_back"),
                ],
            ]
        )
    await cq.edit_message_text(txt, reply_markup=kemem)


@ky.callback("^to.")
async def _(c, cq):
    colmek = cq.data.split(".")[1]
    kemem = okb([[("≪", "to.bc"), ("⪼", "to.next")]])
    user_id = cq.from_user.id
    prefix = await user.get_prefix(user_id)
    txt = None
    if colmek == "next":
        txt = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        kemem = okb(
            [
                [
                    ("Toxic 5", "to.tox5"),
                    ("Toxic 6", "to.tox6"),
                ],
                [
                    ("Toxic 7", "to.tox7"),
                    ("Toxic 8", "to.tox8"),
                ],
                [
                    ("Toxic 9", "to.tox9"),
                ],
                [
                    ("≪", "to.bc"),
                ],
            ]
        )
    elif colmek == "tox1":
        txt = get_cgr("help_tox1").format(next((p) for p in prefix))
    elif colmek == "tox2":
        txt = get_cgr("help_tox2").format(next((p) for p in prefix))
    elif colmek == "tox3":
        txt = get_cgr("help_tox3").format(next((p) for p in prefix))
    elif colmek == "tox4":
        txt = get_cgr("help_tox4").format(next((p) for p in prefix))
    elif colmek == "bc":
        txt = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        kemem = okb(
            [
                [
                    ("Toxic 1", "to.tox1"),
                    ("Toxic 2", "to.tox2"),
                ],
                [
                    ("Toxic 3", "to.tox3"),
                    ("Toxic 4", "to.tox4"),
                ],
                [
                    ("≪", "help_back"),
                    ("⪼", "to.next"),
                ],
            ]
        )
    await cq.edit_message_text(txt, reply_markup=kemem)


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
