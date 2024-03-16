################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from modular.copy_con import *


@ky.bots("copy")
async def _(c, m):
    if m.from_user.id != nlx.me.id:
        return
    xx = await m.reply("Tunggu Sebentar...")
    link = nlx.get_arg(m)
    if not link:
        return await xx.edit(f"<b><code>{m.text}</code> [link]</b>")
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            g = await c.get_messages(chat, msg_id)
            await g.copy(m.chat.id)
            await xx.delete()
        except Exception as error:
            await xx.edit(error)
    else:
        await xx.edit("Link tidak valid.")
