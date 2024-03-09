################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

import re
from secrets import choice

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *
from Mix.core.sender_tools import send_cmd

__modles__ = "Filter"
__help__ = """
Help Command Filter 

• Perintah: <code>{0}filters</code>
• Penjelasan: Untuk melihat daftar filters digrup tersebut.

• Perintah: <code>{0}filter</code> [nama filter] [balas pesan]
• Penjelasan: Untuk menambahkan filters digrup tersebut.

• Perintah: <code>{0}unfilter</code> [nama filter]
• Penjelasan: Untuk menghapus filters digrup tersebut.

• Perintah: <code>{0}unfilterall</code>
• Penjelasan: Untuk menghapus semua filters digrup tersebut.
"""

# Initialise
db = Filters()


@ky.ubot("filters", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    filters_chat = f"{em.sukses} Daftar filters digrup <b>{m.chat.title}</b>:\n"
    all_filters = db.get_all_filters(m.chat.id)
    actual_filters = [j for i in all_filters for j in i.split("|")]
    if not actual_filters:
        await m.reply_text(f"{em.gagal} Tidak ada filters digrup ini.")
        return

    filters_chat += "\n".join(
        [
            f" • {' | '.join([f'<code>{i}</code>' for i in i.split('|')])}"
            for i in all_filters
        ],
    )
    return await m.reply_text(filters_chat, disable_web_page_preview=True)


@ky.ubot("filter", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    args = m.text.split(" ", 1)
    all_filters = db.get_all_filters(m.chat.id)
    actual_filters = {j for i in all_filters for j in i.split("|")}

    if (len(all_filters) >= 50) and (len(actual_filters) >= 150):
        await m.reply_text(
            f"{em.gagal} Anda mempunyai 50 kata filter, hapus salah satu dan coba lagi.",
        )
        return

    if not m.reply_to_message and len(m.text.split()) < 3:
        return await m.reply_text(
            f"{em.gagal} Format yang anda berikan salah. Gunakan format : `filter [nama filter] [balas ke pesan]`."
        )

    if m.reply_to_message and len(args) < 2:
        return await m.reply_text(
            f"{em.gagal} Format yang anda berikan salah. Gunakan format : `filter [nama filter] [balas ke pesan]`."
        )

    extracted = await split_quotes(args[1])
    keyword = extracted[0].lower()

    for k in keyword.split("|"):
        if k in actual_filters:
            return await m.reply_text(f"{em.sukses} Filter <code>{k}</code> sudah ada!")

    if not keyword:
        return await m.reply_text(
            f"{em.gagal} <code>{m.text}</code>\n\nSilahkan berikan nama filter.",
        )

    if keyword.startswith("<") or keyword.startswith(">"):
        return await m.reply_text(
            f"{em.gagal} Tidak dapat menyimpan filter dengan symbol '<' atau '>'."
        )

    eee, msgtype, file_id = get_filter_type(m)
    lol = eee if m.reply_to_message else extracted[1]
    teks = lol if msgtype == Types.TEXT else eee

    if not m.reply_to_message and msgtype == Types.TEXT and len(m.text.split()) < 3:
        return await m.reply_text(
            f"{em.gagal} <code>{m.text}</code>\n\nError: Tidak ada pesan disini!",
        )

    if not teks and not msgtype:
        return await m.reply_text(
            f"{em.gagal} Pastikan split quote sudah benar untuk format filter!",
        )

    if not msgtype:
        return await m.reply_text(
            f"{em.gagal} Pastikan format sudah benar untuk filter!",
        )

    add = db.save_filter(m.chat.id, keyword, teks, msgtype, file_id)
    if add:
        await m.reply_text(
            f"{em.sukses} Filter disimpan '<code>{'|'.join(keyword.split('|'))}</code>'.",
        )
    await m.stop_propagation()


@ky.ubot("unfilter", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    args = c.get_arg(m)

    if len(args) < 1:
        return await m.reply_text(f"{em.gagal} Filter apa yang harus dihentikan ?")

    chat_filters = db.get_all_filters(m.chat.id)
    act_filters = {j for i in chat_filters for j in i.split("|")}

    if not chat_filters:
        return await m.reply_text(f"{em.gagal} Tidak ada filter disini.")

    for keyword in act_filters:
        if keyword == m.text.split(None, 1)[1].lower():
            db.rm_filter(m.chat.id, m.text.split(None, 1)[1].lower())
            await m.reply_text(
                f"{em.sukses} Filter berhasil dihapus!",
            )
            await m.stop_propagation()
        else:
            db.rm_filter(m.chat.id, args)
            await m.reply_text(
                f"{em.sukses} Filter berhasil dihapus!",
            )
            await m.stop_propagation()

    await m.reply_text(
        f"{em.gagal} Tidak ada filters disini!",
    )
    await m.stop_propagation()


@ky.ubot("unfilterall", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    all_bls = db.get_all_filters(m.chat.id)
    if not all_bls:
        return await m.reply_text(f"{em.gagal} Tidak ada filter digrup ini!")
    db.rm_all_filters(m.chat.id)
    await m.reply_text(f"{em.sukses} Semua filter berhasil dihapus!")


async def send_filter_reply(c: user, m, trigger: str):
    """Reply with assigned filter for the trigger"""
    getfilter = db.get_filter(m.chat.id, trigger)
    if m and not m.from_user:
        return

    if not getfilter:
        return await m.reply_text(
            "<b>Error:</b> Tidak dapat menemukan filter ini!!",
        )

    msgtype = getfilter["msgtype"]
    if not msgtype:
        return await m.reply_text("<b>Error:</b> Tidak dapat menemukan filter ini!!")

    try:
        # support for random filter texts
        splitter = "%%%"
        filter_reply = getfilter["filter_reply"].split(splitter)
        filter_reply = choice(filter_reply)
    except KeyError:
        filter_reply = ""

    parse_words = [
        "first",
        "last",
        "fullname",
        "id",
        "mention",
        "username",
        "chatname",
    ]
    text = await escape_mentions_using_curly_brackets(m, filter_reply, parse_words)
    teks, button = await parse_button2(text)
    button = await build_keyboard2(button)
    button = okb(button) if button else None
    textt = teks
    try:
        if msgtype == Types.TEXT:
            if button:
                try:
                    x = await c.get_inline_bot_results(
                        bot.me.username, f"get_fil_inl {getfilter}"
                    )
                    # await m.delete()
                    await c.send_inline_bot_result(
                        m.chat.id,
                        x.query_id,
                        x.results[0].id,
                        reply_to_message_id=ReplyCheck(m),
                    )
                except Exception as e:
                    await xx.edit(f"Error {e}")
                    return
                except RPCError as ef:
                    await m.reply_text(
                        f"{ef} An error has occured! Cannot parse note.\n\nLaporkan ke @KynanSupport.",
                    )
                    return
            else:
                await m.reply_text(
                    textt,
                    # parse_mode=PM.MARKDOWN,
                    disable_web_page_preview=True,
                )
                return

        elif msgtype in (
            Types.STICKER,
            Types.VIDEO_NOTE,
            Types.CONTACT,
            Types.ANIMATED_STICKER,
        ):
            (await send_cmd(c, msgtype))(
                m.chat.id,
                getfilter["fileid"],
                reply_markup=button,
                reply_to_message_id=m.id,
            )
        else:
            (await send_cmd(c, msgtype))(
                m.chat.id,
                getfilter["fileid"],
                caption=textt,
                # parse_mode=PM.MARKDOWN,
                reply_markup=button,
                reply_to_message_id=m.id,
            )
    except Exception as ef:
        await m.reply_text(cgr("err").format(em.gagal, ef))
        return msgtype

    return msgtype


@user.on_message(filters.text & ~filters.private & ~filters.via_bot & ~filters.forwarded, group=11)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    text = m.text.lower().strip()
    if not text:
        return
    chat_filters = db.get_all_filters(m.chat.id)
    actual_filters = {j for i in chat_filters for j in i.split("|")}

    for word in actual_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            try:
                await send_filter_reply(c, m, trigger)
            except Exception as ef:
                await m.reply_text(cgr("err").format(em.gagal, ef))
            break
        continue
    return
