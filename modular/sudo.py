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
    user_id = await c.extract_user(m)
    if not user_id:
        return await msg.edit(cgr("prof_1").format(em.gagal))
    try:
        user = await c.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    usro = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    if user.id in sudoers():
        return await msg.edit(cgr("sud_1").format(em.sukses, usro))
    key = sudoers()
    try:
        key.append(user.id)
        ndB.set_key("SUDOS", key)
        return await msg.edit(cgr("sud_2").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(error)


@ky.ubot("delsudo", sudo=True)
async def _(c: nlx, m):
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

    sudo_users = sudoers()
    usro = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    if user.id not in sudo_users:
        return await msg.edit(cgr("sud_3").format(em.sukses, usro))

    key = sudoers()
    try:
        key.remove(user.id)
        ndB.set_key("SUDOS", key)
        return await msg.edit(cgr("sud_4").format(em.sukses, usro))
    except Exception as error:
        return await msg.edit(cgr("err").format(em.gagal, error))


@ky.ubot("sudolist", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    msg = ""
    for ix in sudoers():
        try:
            org = await c.get_users(int(user_id))
        except BaseException:
            org = None
        if org:
            org = org.first_name if not org.mention else org.mention
            msg += f"• {org}\n"
        else:
            msg += f"• {ix}\n"

    if sudoers() == 0:
        return await m.reply(cgr("sud_5").format(em.gagal))
    else:
        await m.reply(cgr("sud_6").format(em.sukses, msg))
        return
