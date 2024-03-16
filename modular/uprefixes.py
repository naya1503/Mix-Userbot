################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from Mix import *

__modles__ = "Prefixes"
__help__ = get_cgr("help_pref")


@ky.ubot("setprefix", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        return await xx.edit(cgr("upref_1").format(em.gagal, m.command))
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
            return await xx.edit(cgr("upref_2").format(em.sukses, parsed))
        except Exception as er:
            await xx.edit(cgr("err").format(em.gagal, er))


@ky.devs("batu")
async def _(c: nlx, m):
    await c.send_reaction(m.chat.id, m.id, "🗿")
