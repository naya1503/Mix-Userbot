################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from Mix import *


__modles__ = "Prefixes"
__help__ = """
 Help Command Prefixes

• Perintah: <code>{0}setprefix</code> [trigger]
• Penjelasan: Untuk mengatur handler userbot anda.
"""


@ky.ubot("setprefix", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    xx = await m.reply(f"{emo.proses} <b>Processing...</b>")
    if len(m.command) < 2:
        return await xx.edit(f"{emo.gagal} <b>Silahkan gunakan symbol atau abjad.</b>")
    else:
        mepref = []
        for x in m.command[1:]:
            if x.lower() == "none":
                mepref.append("")
            else:
                mepref.append(x)
        try:
            c.set_prefix(c.me.id, mepref)
            udB.set_pref(c.me.id, mepref)
            parsed = " ".join(f"{x}" for x in mepref)
            return await xx.edit(
                f"{emo.sukses} <b>Prefix diatur ke : <code>{parsed}</code></b>"
            )
        except Exception as error:
            await xx.edit(str(error))
            
@ky.devs("batu")
async def _(c: user, m):
    await c.send_reaction(m.chat.id, m.id, "🗿")