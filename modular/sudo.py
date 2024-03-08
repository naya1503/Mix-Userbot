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
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    user_id = await c.extract_user(m)
    if not user_id:
        return await msg.edit(cgr("prof_1").format(em.gagal))
    try:
        user = await c.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")
    usro = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    if user.id in sudo_users:
        return await msg.edit(cgr("1").format(em.sukses, usro))
    try:
        udB.add_to_var(c.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(cgr("sud_2").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(error)


@ky.ubot("delsudo", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    user_id = await c.extract_user(m)
    if not user_id:
        return await m.reply(cgr("prof_1").format(em.sukses))

    try:
        user = await c.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")
    usro = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    if user.id not in sudo_users:
        return await msg.edit(cgr("sud_3").format(em.sukses, usro))

    try:
        udB.remove_from_var(c.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(cgr("sud_4").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(cgr("err").format(em.gagal, error))


@ky.ubot("sudolist", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    msg = await m.reply(cgr("proses").format(em.proses))
    sudo_users = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")

    if not sudo_users:
        return await msg.edit(cgr("sudo_5").format(em.gagal))

    sudo_list = []
    for user_id in sudo_users:
        try:
            org = await c.get_users(int(user_id))
            org = org.first_name if not org.mention else org.mention
            sudo_list.append(
                f"**•** {org}"
            )
            mmfe = " ".join(sudo_list)
        except:
            continue

    if sudo_list:
        return await msg.edit(cgr("sud_6").format(em.sukses, mmfe))
    else:
        return await msg.edit("<b>Eror</b>")
