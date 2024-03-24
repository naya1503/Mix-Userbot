from pyrogram import *
import requests

from Mix import *

__modles__ = "Quran"
__help__ = "Quran"


def get_surah_info():
    url = "https://equran.id/api/v2/surat"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        print("Gagal mengambil data Surah.")
        return None


@ky.ubot("surah", sudo=True)
async def surah_command(client, message):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    surah_info = get_surah_info()

    if surah_info:
        response_text = ""
        for surah in surah_info:
            response_text += f"Nomor Surah: {surah['nomor']}\n"
            response_text += f"Nama Surah: {surah['nama']}\n"
            response_text += f"Nama Surah (Latin): {surah['namaLatin']}\n"
            response_text += f"Jumlah Ayat: {surah['jumlahAyat']}\n"
            response_text += f"Tempat Turun: {surah['tempatTurun']}\n"
            response_text += f"Arti: {surah['arti']}\n"
            response_text += f"Deskripsi: {surah['deskripsi']}\n"
            response_text += "Audio Full:\n"
            for key, value in surah["audioFull"].items():
                response_text += f"  {key}: {value}\n"
            response_text += "\n"
        await message.reply_text(response_text)
        await pros.delete()
    else:
        await message.reply_text("Tidak ada data Surah yang ditemukan.")
        await pros.delete()