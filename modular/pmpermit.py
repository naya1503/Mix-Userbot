################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *

__modles__ = "PMPermit"
__help__ = get_cgr("help_pmper")

from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *

from Mix import *

PM_GUARD_WARNS_DB = {}
PM_GUARD_MSGS_DB = {}

flood = {}
flood2 = {}

DEFAULT_TEXT = cgr("pmper_1")

PM_WARN = cgr("pmper_2")

LIMIT = 5


@ky.ubot("ok|setuju", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    babi = await m.reply(cgr("proses").format(em.proses))
    chat_type = m.chat.type
    getc_pm_warns = udB.get_var(c.me.id, "PMLIMIT")
    pm_text = udB.get_var(c.me.id, "PMTEXT")
    custom_pm_txt = pm_text if pm_text else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if chat_type == "me":
        await babi.delete()
        return
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await babi.delete()
        return
    dia = m.chat.id
    ok_tak = udB.dicek_pc(dia)
    if ok_tak:
        await babi.edit(cgr("pmper_3").format(em.sukses))
        return
    teks, button = parse_button(custom_pm_txt)
    button = build_keyboard(button)
    if button:
        button = InlineKeyboardMarkup(button)
    else:
        button = None
    if button:
        async for m in c.get_chat_history(dia, limit=custom_pm_warns):
            if m.reply_markup:
                await m.delete()
    else:
        try:
            await c.delete_messages("me", message_ids=flood2[dia])
        except KeyError:
            pass
    udB.oke_pc(dia)
    await babi.edit(cgr("pmper_4").format(em.sukses))
    return


@ky.ubot("no|tolak", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    babi = await m.reply(cgr("proses").format(em.proses))
    await asyncio.sleep(2)
    chat_type = m.chat.type
    if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await babi.delete()
        return
    user_id = m.chat.id
    ok_tak = udB.dicek_pc(user_id)
    if not ok_tak:
        await babi.edit(cgr("pmper_5").format(em.sukses))
        return
    udB.tolak_pc(user_id)
    await babi.edit(cgr("pmper_6").format(em.sukses))
    return


@ky.ubot("setmsg", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    babi = await m.reply(cgr("proses").format(em.proses))
    await asyncio.sleep(2)
    user_id = c.me.id
    direp = m.reply_to_message
    args_txt = c.get_arg(m)

    if direp:
        if direp:
            pm_txt = parse_mark(direp.text, direp.reply_markup)
        else:
            pm_txt = direp.text
    elif args_txt:
        pm_txt = args_txt

    if not pm_txt:
        return await babi.edit(cgr("gcs_1").format(em.gagal))

    udB.set_var(user_id, "PMTEXT", pm_txt)
    await babi.edit(cgr("pmper_7").format(em.sukses, pm_txt))
    return


@ky.ubot("setlimit", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    babi = await m.reply(cgr("proses").format(em.proses))
    await asyncio.sleep(2)
    user_id = c.me.id
    args_txt = c.get_arg(m)
    if args_txt:
        if args_txt.isnumeric():
            pm_warns = int(args_txt)
        else:
            return await babi.edit(cgr("pmper_8").format(em.gagal, m.command))
    else:
        return await babi.edit(cgr("pmper_8").format(em.gagal, m.command))
    udB.set_var(user_id, "PMLIMIT", pm_warns)
    await babi.edit(cgr("pmper_9").format(em.sukses, pm_warns))


@user.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.bot
    & ~filters.via_bot
)
async def pm(c, m):
    em = Emojik()
    em.initialize()
    user_id = c.me.id
    siapa = m.from_user.id
    biji = m.from_user.mention
    chat_id = m.chat.id
    in_user = m.from_user
    fsdj = udB.dicek_pc(chat_id)
    is_pm_guard_enabled = udB.get_var(user_id, "PMPERMIT")
    getc_pm_txt = udB.get_var(user_id, "PMTEXT")
    getc_pm_warns = udB.get_var(user_id, "PMLIMIT")
    master = await c.get_me()
    custom_pm_txt = getc_pm_txt if getc_pm_txt else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if not is_pm_guard_enabled:
        return

    if fsdj:
        return

    if in_user.is_fake or in_user.is_scam:
        return await c.block_user(in_user.id)
    if in_user.is_support or in_user.is_verified or in_user.is_self:
        return
    if siapa in DEVS:
        try:
            await c.send_message(
                in_user.id,
                f"<b>Menerima Pesan Dari {biji} !!\nTerdeteksi Developer Dari Mix-Userbot.</b>",
                parse_mode=ParseMode.HTML,
            )
            udB.oke_pc(chat_id)
        except BaseException:
            pass
        return
    teks, button = parse_button(custom_pm_txt)
    button = build_keyboard(button)
    if button:
        button = InlineKeyboardMarkup(button)
    else:
        button = None
    if button:
        try:
            x = await c.get_inline_bot_results(
                bot.me.username, f"ambil_tombolpc {chat_id}"
            )
            await c.send_inline_bot_result(
                m.chat.id,
                x.query_id,
                x.results[0].id,
                reply_to_message_id=m.id,
            )
        except:
            pass
    else:
        gmbr = udB.get_var(user_id, "PMPIC")
        if gmbr:
            kok_poto = m.reply_video if gmbr.endswith(".mp4") else m.reply_photo
            if in_user.id in flood:
                try:
                    if chat_id in flood2:
                        await c.delete_messages(chat_id, message_ids=flood2[chat_id])
                except BaseException:
                    pass
                flood[in_user.id] += 1
                if flood[in_user.id] >= custom_pm_warns:
                    del flood[in_user.id]
                    await m.reply(cgr("pmper_5").format(em.block, custom_pm_warns))
                    return await c.block_user(in_user.id)
                else:
                    rplied_msg = await kok_poto(
                        gmbr,
                        caption=PM_WARN.format(
                            master.first_name,
                            flood[in_user.id],
                            custom_pm_warns,
                            custom_pm_txt.format(bot.me.first_name),
                        ),
                    )
            else:
                flood[in_user.id] = 1
                rplied_msg = await kok_poto(
                    gmbr,
                    caption=PM_WARN.format(
                        master.first_name,
                        flood[in_user.id],
                        custom_pm_warns,
                        custom_pm_txt.format(bot.me.first_name),
                    ),
                )
            flood2[chat_id] = rplied_msg.id
        else:
            if in_user.id in flood:
                try:
                    if chat_id in flood2:
                        await c.delete_messages(chat_id, message_ids=flood2[chat_id])
                except BaseException:
                    pass
                flood[in_user.id] += 1
                if flood[in_user.id] >= custom_pm_warns:
                    del flood[in_user.id]
                    await m.reply(cgr("pmper_5").format(em.block, custom_pm_warns))
                    return await c.block_user(in_user.id)
                else:
                    rplied_msg = await m.reply(
                        PM_WARN.format(
                            master.first_name,
                            flood[in_user.id],
                            custom_pm_warns,
                            custom_pm_txt.format(bot.me.first_name),
                        ),
                    )
            else:
                flood[in_user.id] = 1
                rplied_msg = await m.reply(
                    PM_WARN.format(
                        master.first_name,
                        flood[in_user.id],
                        custom_pm_warns,
                        custom_pm_txt.format(bot.me.first_name),
                    ),
                )
            flood2[chat_id] = rplied_msg.id
