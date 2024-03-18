################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
 
 EH KONTOL BAJINGAN !! KALO MO PAKE DIKODE PAKE AJA BANGSAT!! GAUSAH APUS KREDIT NGENTOT
"""
################################################################


import asyncio
import re
from time import time

import psutil
import speedtest
from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import *

from Mix import *
from Mix.core.sender_tools import escape_tag, parse_words
from Mix.core.waktu import get_time, start_time
from modular.pmpermit import *


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


@ky.callback("^back_permit")
async def _(c, cq):
    sapa = cq.data.split()
    gw = cq.from_user.id
    getpm_txt = udB.get_var(nlx.me.id, "PMTEXT")
    pm_text = getpm_txt if getpm_txt else DEFAULT_TEXT
    getpm_warns = udB.get_var(gw, "PMLIMIT")
    pm_warns = getpm_warns if getpm_warns else LIMIT
    teks, button = text_keyb(ikb, pm_text)
    if button:
        def_keyb = {
            "Setuju": f"pm_ okein {int(sapa[0])}",
            "Blokir": f"pm_ blokbae {int(sapa[0])}",
        }
        for row in button.inline_keyboard:
            for data in row:
                add_keyb = (
                    {data.text: data.url}
                    if data.url
                    else {data.text: data.callback_data}
                )
                def_keyb.update(add_keyb)
                keyboard = ikb(def_keyb)
    else:
        def_keyb = {
            "Setuju": f"pm_ okein {int(sapa[0])}",
            "Blokir": f"pm_ blokbae {int(sapa[0])}",
        }
        keyboard = ikb(def_keyb)
    tekss = await escape_tag(int(sapa[0]), pm_text, parse_words)
    kiki = None
    if nlx.me.id == gw:
        if int(sapa[0]) in flood2:
            flood2[int(sapa[0])] += 1
        else:
            flood2[int(sapa[0])] = 1
        async for m in nlx.get_chat_history(int(sapa[0]), limit=pm_warns):
            if m.reply_markup:
                await m.delete()
        kiki = PM_WARN.format(
            tekss,
            flood2[int(sapa[0])],
            pm_warns,
        )
        lah = udB.get_var(gw, "PMPIC")
        if lah:
            await cq.edit_message_caption(caption=kiki, reply_markup=keyboard)
        else:
            await cq.edit_message_text(kiki, reply_markup=keyboard)


@ky.callback("^pm_")
async def _(c, cq):
    org = cq.from_user.id
    data, sapa = (
        cq.data.split(None, 2)[1],
        cq.data.split(None, 2)[2],
    )
    if data == "okein":
        if org != nlx.me.id:
            return await cq.answer("This Button Not For You FCVK !!!!", True)
        udB.oke_pc(int(sapa))
        return await bot.edit_inline_text(
            cq.inline_message_id, "User Has Been Approved To PM."
        )

    if data == "blokbae":
        if org != nlx.me.id:
            return await cq.answer("This Button Not For You FCVK !!!!", True)
        await bot.edit_inline_text(
            cq.inline_message_id, "Successfully blocked the users."
        )
        await nlx.block_user(int(sapa))
        return await nlx.invoke(
            DeleteHistory(
                peer=(await nlx.resolve_peer(sapa)),
                max_id=0,
                revoke=False,
            )
        )


@ky.callback(("^suprot"))
async def _(c, cq):
    txt = cgr("supot")
    kbt = ikb(
        {
            "Support 1": f"https://t.me/kynansupport",
            "Support 2": f"https://t.me/gokilsupport",
            "Channel 1": f"https://t.me/kontenfilm",
            "Channel 2": f"https://t.me/SquirtInYourPussy",
            "Stats": "stats_mix",
        }
    )
    await cq.edit_message_text(txt, reply_markup=kbt)


@ky.callback(("^stats_mix"))
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
    prefix = await nlx.get_prefix(user_id)

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
            try:
                await cq.edit_message_text(
                    text=text1, reply_markup=button, disable_web_page_preview=True
                )
            except FloodWait as e:
                await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
                return
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
            try:
                await cq.edit_message_text(
                    text=text1, reply_markup=button, disable_web_page_preview=True
                )
            except FloodWait as e:
                await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
                return
        else:
            try:
                await cq.edit_message_text(
                    text=text + f"\n<b>© Mix-Userbot - @KynanSupport</b>",
                    reply_markup=button,
                    disable_web_page_preview=True,
                )
            except FloodWait as e:
                await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
                return

    if prev_match:
        t1 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        curr_page = int(prev_match.group(1))
        try:
            await cq.edit_message_text(
                text=t1,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, CMD_HELP, "help")
                ),
                disable_web_page_preview=True,
            )
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    if next_match:
        t2 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        next_page = int(next_match.group(1))
        try:
            await cq.edit_message_text(
                text=t2,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, CMD_HELP, "help")
                ),
                disable_web_page_preview=True,
            )
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    if back_match:
        t3 = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        try:
            await cq.edit_message_text(
                text=t3,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CMD_HELP, "help")
                ),
                disable_web_page_preview=True,
            )
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return


@ky.callback("^anim.")
async def _(c, cq):
    colmek = cq.data.split(".")[1]
    kemem = okb([[("≪", "anim.bc")]])
    user_id = cq.from_user.id
    prefix = await nlx.get_prefix(user_id)
    txt = None
    if colmek == "anm1":
        txt = get_cgr("help_anm1").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "anm2":
        txt = get_cgr("help_anm2").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "anm3":
        txt = get_cgr("help_anm3").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "anm4":
        txt = get_cgr("help_anm4").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
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
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return


@ky.callback("^to.")
async def _(c, cq):
    colmek = cq.data.split(".")[1]
    kemem = okb([[("≪", "to.bc"), ("⪼", "to.next")]])
    user_id = cq.from_user.id
    prefix = await nlx.get_prefix(user_id)
    txt = None
    if colmek == "next":
        txt = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        kemem2 = okb(
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
        try:
            await cq.edit_message_text(txt, reply_markup=kemem2)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox1":
        txt = get_cgr("help_tox1").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox2":
        txt = get_cgr("help_tox2").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox3":
        txt = get_cgr("help_tox3").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox4":
        txt = get_cgr("help_tox4").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox5":
        txt = get_cgr("help_tox5").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox6":
        txt = get_cgr("help_tox6").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox7":
        txt = get_cgr("help_tox7").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox8":
        txt = get_cgr("help_tox8").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "tox9":
        txt = get_cgr("help_tox9").format(next((p) for p in prefix))
        try:
            await cq.edit_message_text(txt, reply_markup=kemem)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return
    elif colmek == "bc":
        txt = "<b>Commands\n      Prefixes: <code>{}</code>\n      Modules: <code>{}</code></b>".format(
            " ".join(prefix), len(CMD_HELP)
        )
        kemem3 = okb(
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
        try:
            await cq.edit_message_text(txt, reply_markup=kemem3)
        except FloodWait as e:
            await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            return


@ky.callback("^cls_hlp")
async def _(_, cq):
    unPacked = unpackInlineMessage(cq.inline_message_id)
    if cq.from_user.id == nlx.me.id:
        await nlx.delete_messages(unPacked.chat_id, unPacked.message_id)
    else:
        await cq.answer(
            f"Jangan Di Pencet Anjeng.",
            True,
        )
        return


@ky.callback("^close")
async def _(_, cq):
    unPacked = unpackInlineMessage(cq.inline_message_id)
    if cq.from_user.id == nlx.me.id:
        await nlx.delete_messages(unPacked.chat_id, unPacked.message_id)
    else:
        await cq.answer(f"Jangan Di Pencet Anjeng.", True)
        return


def cb_tespeed():
    def speed_convert(size):
        power = 2**10
        zero = 0
        units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
        while size > power:
            size /= power
            zero += 1
        return f"{round(size, 2)} {units[zero]}"

    speed = speedtest.Speedtest()
    info = speed.get_best_server()
    download = speed.download()
    upload = speed.upload()
    return [speed_convert(download), speed_convert(upload), info]


@ky.callback("^gasbalap")
async def _(c, cq):
    if cq.from_user.id != nlx.me.id:
        return await cq.answer("LU SIAPA BANGSAT!! MAEN KLIK-KLIK BAE BAJINGAN.", True)
    kb = ikb({f"{cgr('ttup')}": "cls_hlp"})
    await cq.edit_message_text(text="**Processing...**", reply_markup=kb)
    loop = asyncio.get_running_loop()
    download, upload, info = await loop.run_in_executor(None, cb_tespeed)
    msg = f"""
**Download:** `{download}`
**Upload:** `{upload}`
**Latency:** `{info['latency']} ms`
**Country:** `{info['country']} [{info['cc']}]`
**Latitude:** `{info['lat']}`
**Longitude:** `{info['lon']}`
"""
    await cq.edit_message_text(msg, reply_markup=kb)


@ky.callback("^#")
async def _(c, cq):
    try:
        btn_data = cq.data
        if btn_data.startswith("#"):
            notetag = btn_data[1:]
            noteval = udB.get_note(nlx.me.id, notetag)
            if not noteval:
                await cq.answer("Catatan tidak ditemukan.", True)
                return
            if noteval["type"] in [Types.PHOTO, Types.VIDEO]:
                file_type = "jpg" if noteval["type"] == Types.PHOTO else "mp4"
                if noteval["type"] == Types.PHOTO:
                    note, button = text_keyb(ikb, noteval.get("value"))
                    try:
                        await cq.edit_message_caption(caption=note, reply_markup=button)
                    except FloodWait as e:
                        await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
                        return
                elif noteval["type"] == Types.VIDEO:
                    note, button = text_keyb(ikb, noteval.get("value"))
                    try:
                        await cq.edit_message_caption(caption=note, reply_markup=button)
                    except FloodWait as e:
                        await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
                        return
            elif noteval["type"] == Types.TEXT:
                note, button = text_keyb(ikb, noteval.get("value"))
                try:
                    await cq.edit_message_text(text=note, reply_markup=button)
                except FloodWait as e:
                    await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
                    return

    except Exception as e:
        print(f"Error in callback handler: {e}")
