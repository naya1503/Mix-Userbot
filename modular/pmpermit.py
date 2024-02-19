################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *

__modles__ = "PMPermit"
__help__ = """
 Help Command PMPermit

• Perintah: <code>{0}setmsg</code> [balas atau berikan pesan]
• Penjelasan: Untuk mengatur pesan PMPERMIT.

• Perintah: <code>{0}setlimit</code> [angka]
• Penjelasan: Untuk mengatur peringatan pesan blokir.

• Perintah: <code>{0}ok atau setuju</code>
• Penjelasan: Untuk menyetujui pesan.

• Perintah: <code>{0}no atau tolak</code>
• Penjelasan: Untuk menolak pesan.

• Untuk menghidupkan PMPermit Silahkan Ketik:
<code>{0}setdb pmpermit on</code>
"""

from pyrogram import *
from pyrogram.types import *

from Mix import *

PM_GUARD_WARNS_DB = {}
PM_GUARD_MSGS_DB = {}

flood = {}
flood2 = {}

DEFAULT_TEXT = """
I am {} maintains this Chat Room . Don't spam or You will be auto blocked.
"""

PM_WARN = """
<b>Security Message of {} . You have <code>{}/{}</code> warnings !! </b>

<b>{}</b>
"""

LIMIT = 5


@ky.ubot("ok|setuju", sudo=True)
async def _(c: user, m):

    babi = await m.reply(f"{c.proses} <b>Processing...</b>")
    chat_type = m.chat.type
    getc_pm_warns = udB.get_var(c.me.id, "PMLIMIT")
    pm_text = udB.get_var(c.me.id, "PMTEXT")
    custom_pm_txt = pm_text if pm_text else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if chat_type == "me":
        return
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return
    dia = m.chat.id
    ok_tak = udB.dicek_pc(dia)
    if ok_tak:
        await babi.edit(f"{c.sukses} <b>Pengguna ini sudah disetujui.</b>")
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
    await babi.edit(
        f"{c.sukses} <b>Baiklah, pengguna ini disetujui untuk mengirim pesan.</b>"
    )
    return


@ky.ubot("no|tolak", sudo=True)
async def _(c: user, m):

    babi = await m.reply(f"{c.proses} <b>Processing...</b>")
    await asyncio.sleep(2)
    chat_type = m.chat.type
    if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return
    user_id = m.chat.id
    ok_tak = udB.dicek_pc(user_id)
    if not ok_tak:
        await babi.edit(
            f"{c.gagal} <b>Pengguna ini memang belum disetujui untuk mengirim pesan.</b>"
        )
        return
    udB.tolak_pc(user_id)
    await babi.edit(
        f"{c.sukses} <b>Baiklah, pengguna ini ditolak untuk mengirim pesan.</b>"
    )
    return


@ky.ubot("setmsg", sudo=True)
async def _(c: user, m):

    babi = await m.reply(f"{c.proses} <b>Processing...</b>")
    await asyncio.sleep(2)
    user_id = c.me.id
    r_msg = m.reply_to_message
    args_txt = c.get_arg(m)
    if r_msg:
        if r_msg.text:
            pm_txt = r_msg.text
        else:
            return await babi.edit(
                f"{c.gagal} <b>Silakan balas ke pesan untuk dijadikan teks PMPermit !</b>"
            )
    elif args_txt:
        pm_txt = args_txt
    else:
        return await babi.edit(
            f"{c.gagal} <b>Silakan balas ke pesan atau berikan pesan untuk dijadikan teks PMPermit !\nContoh :<code>{m.command} Halo saya anuan.</code></b>"
        )
    teks, _ = parse_button(pm_txt)
    udB.set_var(user_id, "PMTEXT", pm_txt)
    await babi.edit(
        f"{c.sukses} <b>Pesan PMPermit berhasil diatur menjadi : <code>{pm_txt}</code>.</b>"
    )
    return


@ky.ubot("setlimit", sudo=True)
async def _(c: user, m):

    babi = await m.reply(f"{c.proses} <b>Processing...</b>")
    await asyncio.sleep(2)
    user_id = c.me.id
    args_txt = c.get_arg(m)
    if args_txt:
        if args_txt.isnumeric():
            pm_warns = int(args_txt)
        else:
            return await babi.edit(
                f"{c.gagal} <b>Silakan berikan untuk angka limit !</b>"
            )
    else:
        return await babi.edit(
            f"{c.gagal} <b>Silakan berikan pesan untuk dijadikan angka limit !\nContoh :<code> {m.command}setlimit 5.</code></b>"
        )
    udB.set_var(user_id, "PMLIMIT", pm_warns)
    await babi.edit(
        f"{c.sukses} <b>Pesan Limit berhasil diatur menjadi : <code>{args_txt}</code>.</b>"
    )


@ky.permit()
async def _(c, m):
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
        await m.reply("Sepertinya anda mencurigakan...")
        return await c.block_user(in_user.id)
    if in_user.is_support or in_user.is_verified or in_user.is_self:
        return
    if siapa in DEVS:
        try:
            await c.send_message(
                in_user.id,
                f"<b>Menerima Pesan Dari {biji} !!\nTerdeteksi Developer Dari Mix-Userbot.</b>",
                parse_mode=enums.ParseMode.HTML,
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
                    await m.reply(
                        f"{c.gagal} <b>Saya sudah memberi tahu `{custom_pm_warns}` peringatan\nTunggu tuan saya menyetujui pesan anda, atau anda akan diblokir !</b>"
                    )
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
                    await m.reply(
                        f"{c.gagal} <b>Saya sudah memberi tahu `{custom_pm_warns}` peringatan\nTunggu tuan saya menyetujui pesan anda, atau anda akan diblokir !</b>"
                    )
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


@ky.inline("^ambil_tombolpc")
async def _(c, iq):
    org = iq.query.split()
    gw = iq.from_user.id
    getpm_txt = udB.get_var(gw, "PMTEXT")
    getpm_warns = udB.get_var(gw, "PMLIMIT")
    pm_warns = getpm_warns if getpm_warns else LIMIT
    pm_text = getpm_txt if getpm_txt else DEFAULT_TEXT
    teks, button = parse_button(pm_text)
    button = build_keyboard(button)
    kiki = None
    if user.me.id == gw:
        if int(org[1]) in flood2:
            flood2[int(org[1])] += 1
        else:
            flood2[int(org[1])] = 1
        async for m in user.get_chat_history(int(org[1]), limit=pm_warns):
            if m.reply_markup:
                await m.delete()
        kiki = PM_WARN.format(
            user.me.first_name,
            flood2[int(org[1])],
            pm_warns,
            teks.format(bot.me.first_name),
        )
        if flood2[int(org[1])] > pm_warns:
            await user.send_message(int(org[1]), "Spam Terdeteksi !!! Blokir.")
            del flood2[int(org[1])]
            await user.block_user(int(org[1]))
            return
        lah = udB.get_var(gw, "PMPIC")
        if lah:
            filem = (
                InlineQueryResultVideo
                if lah.endswith(".mp4")
                else InlineQueryResultPhoto
            )
            url_ling = (
                {"video_url": lah, "thumb_url": lah}
                if lah.endswith(".mp4")
                else {"photo_url": lah}
            )
            duar = [
                filem(
                    **url_ling,
                    title="PIC Buttons !",
                    caption=kiki,
                    reply_markup=InlineKeyboardMarkup(button),
                )
            ]
        else:
            duar = [
                (
                    InlineQueryResultArticle(
                        title="Tombol PM!",
                        input_message_content=InputTextMessageContent(kiki),
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                )
            ]
        await c.answer_inline_query(iq.id, cache_time=0, results=duar)
