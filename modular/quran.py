import requests
from pyrogram import *

from Mix import *

processed_surah_numbers = set()

__modules__ = "Quran"
__help__ = "Quran"


def ambil_nama_surah(surah_name):
    response = requests.get("https://equran.id/api/v2/surat")
    if response.status_code == 200:
        surah_list = response.json()["data"]
        for surah_info in surah_list:
            if surah_info["namaLatin"].lower() == surah_name.lower():
                return surah_info
    return None


@ky.ubot("surat|surah|quran", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))

    surah_name = (
        m.text.split(maxsplit=1)[1].strip().lower() if len(m.command) > 1 else None
    )

    if not surah_name:
        await m.reply(f"{em.gagal} Silahkan berikan nama surah.")
        await pros.delete()
        return

    surah_info = ambil_nama_surah(surah_name)

    if surah_info:
        response_text = (
            f"Nomor Surah: `{surah_info['nomor']}`\n"
            f"Nama Surah: `{surah_info['nama']}`\n"
            f"Nama Surah (Latin): `{surah_info['namaLatin']}`\n"
            f"Jumlah Ayat: `{surah_info['jumlahAyat']}`\n"
            f"Tempat Turun: `{surah_info['tempatTurun']}`\n"
            f"Arti: `{surah_info['arti']}`\n"
            f"Deskripsi: `{surah_info['deskripsi']}`\n"
        )

        audio_url = next(iter(surah_info["audioFull"].values()), None)
        if audio_url:
            aud = await m.reply_audio(audio_url, reply_to_message_id=ReplyCheck(m))
            if len(response_text) > 4096:
                file_name = f"{surah_name.capitalize()}.txt"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response_text)
                await m.reply_document(file_name, reply_to_message_id=aud.id)
            else:
                await m.reply(response_text, reply_to_message_id=aud.id)
        else:
            await m.reply(response_text, reply_to_message_id=ReplyCheck(m))

        await pros.delete()
    else:
        await m.reply_text(
            f"Surah dengan nama '{surah_name.capitalize()}' tidak ditemukan."
        )
        await pros.delete()
