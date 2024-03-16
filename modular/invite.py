from hydrogram.enums import *
from hydrogram.errors import *
from hydrogram.methods import *
from hydrogram.types import *

from Mix import *

__modles__ = "Invite"
__help__ = get_cgr("help_inv")


@ky.ubot("invite|undang", sudo=True)
@ky.devs("sinijoin")
async def _(c, m):
    em = Emojik()
    em.initialize()
    mg = await m.reply_text(cgr("inv_1").format(em.proses))
    if len(m.command) < 2:
        await mg.edit(cgr("inv_2").format(em.gagal))
        return

    nlx_s_to_add = m.command[1]
    nlx_list = nlx_s_to_add.split(" ")
    nlx_id = await c.extract_nlx(m)

    if not nlx_list:
        await mg.edit(cgr("inv_2").format(em.gagal))
        return
    try:
        await c.add_chat_members(m.chat.id, nlx_list, forward_limit=100)
    except errors.BadRequest as e:
        await mg.edit(
            f"{em.gagal} <b>Gagal menambahkan pengguna. Alasan:</b> <code>{str(e)}</code>"
        )
        return
    mention = (await c.get_nlxs(nlx_id)).mention
    await mg.edit(cgr("inv_3").format(em.sukses, mention, m.chat.title))


@ky.ubot("getlink|invitelink", sudo=True)
@ky.devs("getling")
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = await m.reply_text(cgr("proses").format(em.proses))

    if m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        m.chat.title
        try:
            link = await c.export_chat_invite_link(m.chat.id)
            await Nan.edit(cgr("inv_4").format(em.sukses, link))
        except Exception:
            await Nan.edit(cgr("inv_5").format(em.gagal))
    elif m.chat.type == ChatType.CHANNEL:
        try:
            link = await c.export_chat_invite_link(m.chat.id)
            await Nan.edit(cgr("inv_4").format(em.sukses, link))
        except Exception:
            await Nan.edit(cgr("inv_5").format(em.gagal))
    else:
        await Nan.edit(cgr("inv_6").format(em.gagal))
