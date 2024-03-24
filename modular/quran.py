import requests
from pyrogram import *

from Mix import *

processed_surah_numbers = set()

__modules__ = "Quran"
__help__ = "Quran"


def get_surah_info():
    url = "https://equran.id/api/v2/surat"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        print("Gagal mengambil data Surah.")
        return None


@ky.ubot("surah", sudo=True)
async def surah_command(c: nlx, m):
    global processed_surah_numbers

    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    surah_info = get_surah_info()

    if surah_info:
        for surah in surah_info:
            surah_number = surah["nomor"]
            if surah_number in processed_surah_numbers:
                continue

            response_text = (
                f"Nomor Surah: `{surah_number}`\n"
                f"Nama Surah: `{surah['nama']}`\n"
                f"Nama Surah (Latin): `{surah['namaLatin']}`\n"
                f"Jumlah Ayat: `{surah['jumlahAyat']}`\n"
                f"Tempat Turun: `{surah['tempatTurun']}`\n"
                f"Arti: `{surah['arti']}`\n"
                f"Deskripsi: `{surah['deskripsi']}`\n"
            )

            audio_files = surah["audioFull"].values()
            if audio_files:
                audio_url = next(iter(audio_files))
                try:
                    audio_response = requests.get(audio_url)
                    if audio_response.status_code == 200:
                        await m.reply_audio(
                            audio_response.content,
                            caption=response_text,
                            file_name=None,
                        )
                        processed_surah_numbers.add(surah_number)
                    else:
                        print(f"Gagal mengunduh file audio dari {audio_url}")
                except Exception as e:
                    print(f"Terjadi kesalahan: {str(e)}")
                    await m.reply(response_text)
            else:
                await m.reply(response_text)
        await pros.delete()
    else:
        await m.reply_text("Tidak ada data Surah yang ditemukan.")
        await pros.delete()
