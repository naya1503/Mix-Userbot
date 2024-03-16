################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *

__modles__ = "Sudo"
__help__ = get_cgr("help_sudo")


@ky.ubot("addsudo", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    nlx_id = await c.extract_nlx(m)
    if not nlx_id:
        return await msg.edit(cgr("prof_1").format(em.gagal))
    try:
        nlx = await c.get_nlxs(nlx_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_nlxs = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")
    usro = f"[{nlx.first_name} {nlx.last_name or ''}](tg://nlx?id={nlx.id})"
    if nlx.id in sudo_nlxs:
        return await msg.edit(cgr("1").format(em.sukses, usro))
    try:
        udB.add_to_var(c.me.id, "SUDO_USER", nlx.id, "ID_NYA")
        return await msg.edit(cgr("sud_2").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(error)


@ky.ubot("delsudo", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    nlx_id = await c.extract_nlx(m)
    if not nlx_id:
        return await m.reply(cgr("prof_1").format(em.sukses))

    try:
        nlx = await c.get_nlxs(nlx_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_nlxs = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")
    usro = f"[{nlx.first_name} {nlx.last_name or ''}](tg://nlx?id={nlx.id})"
    if nlx.id not in sudo_nlxs:
        return await msg.edit(cgr("sud_3").format(em.sukses, usro))

    try:
        udB.remove_from_var(c.me.id, "SUDO_USER", nlx.id, "ID_NYA")
        return await msg.edit(cgr("sud_4").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(cgr("err").format(em.gagal, error))


@ky.ubot("sudolist", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    sudo_nlxs = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")
    sd = 0
    hsl = "\n"
    for nlx_id in sudo_nlxs:
        try:
            org = await nlx.get_nlxs(int(nlx_id))
            org = org.first_name if not org.mention else org.mention
            sd += 1
            hsl += f"**{em.profil} {sd} - {org}**\n"
        except:
            continue

    if not sudo_nlxs:
        return await m.reply(cgr("sud_5").format(em.gagal))
    else:
        await m.reply(cgr("sud_6").format(em.sukses, hsl))
        return
