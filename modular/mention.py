import random

from pyrogram import *
from pyrogram.types import *

__modles__ = "Mention"
__help__ = "Mention"

berenti = False  # Inisialisasi variabel berenti sebagai pengontrol penghentian proses tag_all_members


def random_emoji():
    emojis = ["👤", "👥", "🧑‍💼", "🧑‍🔬", "🧑‍🚀"]
    return random.choice(emojis)


@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: user, m: Message):
    global berenti
    chat_id = m.chat.id
    admins = False
    try:
        administrator = []
        async for admin in c.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            administrator.append(admin)
        await c.get_chat_member(chat_id, m.from_user.id)
        admins = administrator
    except Exception as e:
        await m.reply(f"Error : {e}")
        print(e)

    if not admins:
        await m.reply_text("Anda harus menjadi admin untuk menggunakan perintah ini!")
        return

    if berenti:  # Periksa apakah berenti telah diatur menjadi True
        await m.reply_text(
            "Proses tagall sedang berlangsung. Harap tunggu sampai selesai atau gunakan perintah stop."
        )
        return

    berenti = (
        False  # Setel kembali berenti ke False sebelum memulai proses tag_all_members
    )

    if len(m.command) < 2:
        await m.reply_text("Harap berikan teks untuk di-mention.")
        return

    text = " ".join(m.command[1:])

    mention_texts = []
    async for member in c.iter_chat_members(chat_id):
        if not member.user.is_bot:
            mention_texts.append(f"{random_emoji()} @{member.user.username}")
            if len(mention_texts) == 4:
                mention_text = f"{text}\n"
                mention_text += "\n".join(mention_texts)
                await c.send_message(chat_id, mention_text)
                mention_texts = []

        if (
            berenti
        ):  # Periksa apakah berenti telah diatur menjadi True setiap kali iterasi anggota chat
            break

    if mention_texts:
        mention_text = f"{text}\n"
        mention_text += "\n".join(mention_texts)
        await c.send_message(chat_id, mention_text)

    berenti = (
        False  # Setel kembali berenti ke False setelah proses tag_all_members selesai
    )


@ky.ubot("stop", sudo=True)
async def stop_tagall(c: user, m: Message):
    global berenti
    if not berenti:
        await m.reply_text("Tidak ada proses tagall yang sedang berlangsung.")
        return

    berenti = True  # Setel berenti ke True untuk menghentikan proses tag_all_members
    await m.reply_text("Tagall telah dihentikan.")
