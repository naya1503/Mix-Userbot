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

from Mix import *
from pyrogram.errors import *

@ky.ubot("gruplog", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    xx = await m.reply(f"{emo.proses} Processing...")
    cek = c.get_arg(m)
    logs = udB.get_logger(c.me.id)
    if cek.lower() == "on":
        if not logs:
            await c.logger_grup()
            xx = await c.get_grup()
            ff = await c.export_chat_invite_link(int(xx.id))
            return await xx.edit(f"{emo.sukses} **Log Group Berhasil Diaktifkan :\n\n{ff}**")
            udB.set_logger(c.me.id, int(xx.id))
        else:
            return await xx.edit(f"{emo.sukses} **Log Group Anda Sudah Aktif.**")
    if cek.lower() == "off":
        if logs:
            udB.rem_logger(c.me.id)
            xx = await c.get_grup()
            await c.delete_supergroup(int(xx.id))
            return await xx.edit(f"{emo.gagal} **Log Group Berhasil Dinonaktifkan.**")
        else:
            return await xx.edit(f"{emo.gagal} **Log Group Anda Sudah Dinonaktifkan.**")
    else:
        return await xx.edit(
            f"{emo.gagal} **Format yang anda berikan salah. silahkan gunakan <code>gruplog on or off</code>.**"
        )

@ky.grup()
async def _(c, m):
     db =  udB.get_logger(user.me.id)
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
         await bot.send_message(
            db,
            teks,
            disable_web_page_preview=True,
            reply_markup=donut)
     except FloodWait as e:
        await asyncio.sleep(e.value)
        await bot.send_message(
            db,
            teks,
            disable_web_page_preview=True,
            reply_markup=donut)


@ky.pm()
async def _(c: user, m):
    await c.forward_private(m)
    db =  udB.get_logger(c.me.id)
    if not db:
      return
    if m.chat.id == 777000:
      return
    await c.send_message(db, m.chat.id, reply_to_message_id=m.id)