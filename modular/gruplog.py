################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

__modles__ = "Gruplog"
__help__ = """
Help Command GrupLog

• Perintah: <code>{0}gruplog</code> [on/off]
• Penjelasan: Aktifkan tag log dan pm log.
"""


from pyrogram.errors import *

from Mix import *


@ky.ubot("gruplog", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} Processing...")
    cek = c.get_arg(m)
    logs = udB.get_logger(c.me.id)
    if cek.lower() == "on":
        if not logs:
            await c.logger_grup()
            xx = await c.get_grup()
            ff = await c.export_chat_invite_link(int(xx.id))
            return await xx.edit(
                f"{em.sukses} **Log Group Berhasil Diaktifkan :\n\n{ff}**"
            )
            udB.set_logger(c.me.id, int(xx.id))
        else:
            return await xx.edit(f"{em.sukses} **Log Group Anda Sudah Aktif.**")
    if cek.lower() == "off":
        if logs:
            udB.rem_logger(c.me.id)
            xx = await c.get_grup()
            await c.delete_supergroup(int(xx.id))
            return await xx.edit(f"{em.gagal} **Log Group Berhasil Dinonaktifkan.**")
        else:
            return await xx.edit(f"{em.gagal} **Log Group Anda Sudah Dinonaktifkan.**")
    else:
        return await xx.edit(
            f"{em.gagal} **Format yang anda berikan salah. silahkan gunakan <code>gruplog on or off</code>.**"
        )


@ky.grup()
async def _(c, m):

    db = udB.get_logger(user.me.id)
    if not db:
        return
    org = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    lenk = m.link
    teks = f"""
📨 <b>TAGS MESSAGE</b>
• <b>Logs:</b> <code>{user.me.first_name}</code>
• <b>Group:</b> <code>{m.chat.title}</code>
• <b>Dari :</b> <code>{org}</code>
• <b>Pesan:</b> <code>{m.text}</code>
"""
    donut = InlineKeyboardMarkup([[InlineKeyboardButton("Tautan Grup", url=lenk)]])
    try:
        ret = await bot.send_message(
            db, teks, disable_web_page_preview=True, reply_markup=donut
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
        ret = await bot.send_message(
            db, teks, disable_web_page_preview=True, reply_markup=donut
        )
    tag_add(ret.id, m.chat.id, m.from_user.id)

@user.on_message(filters.reply & filters.me & filters.group, group=69)
async def _(c: user, m):
    reply_ = m.reply_to_message.message_id
    chat, msg = who_tag(reply_)
    if chat and msg:
        try:
            await c.send_message(chat, m, reply_to_message_id=msg)
            return
        except Exception as e:
            await m.reply(f"{e}")
            return

@ky.pc()
async def _(_, m):
    await user.forward_private(m)
