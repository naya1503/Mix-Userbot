import requests
from pyrogram import *

from Mix import *

processed_surah_numbers = set()

__modules__ = "Quran"
__help__ = "Quran"

"""
def get_surah_info(surah_name):
    url = f"https://equran.id/api/v2/{surah_name}"
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
    surah_name = (
        m.text.split(maxsplit=1)[1].strip().lower() if len(m.command) > 1 else None
    )

    if not surah_name:
        await m.reply(f"{em.gagal} Silahkan berikan nama surah.")
        await pros.delete()
        return

    surah_info = get_surah_info(surah_name)

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
                            audio_response.content, caption=response_text
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
        await m.reply_text(
            f"Surah dengan nama '{surah_name.capitalize()}' tidak ditemukan."
        )
        await pros.delete()
"""


def ambil_nama_surah(surah_name):
    response = requests.get("https://equran.id/api/v2/surat")
    if response.status_code == 200:
        surah_list = response.json()["data"]
        for surah_info in surah_list:
            if surah_info["namaLatin"].lower() == surah_name.lower():
                return surah_info
    return None


async def ambil_audio_surah(m, audio_url, response_text):
    try:
        audio_response = requests.get(audio_url)
        if audio_response.status_code == 200:
            await m.reply_audio(audio_response.content, caption=response_text)
        else:
            print(f"Gagal mengunduh file audio dari {audio_url}")
            await m.reply(response_text)
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        await m.reply(response_text)


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

        audio_files = surah_info["audioFull"].values()
        if audio_files:
            audio_url = next(iter(audio_files))
            await ambil_audio_surah(m, audio_url, response_text)
        else:
            await m.reply(response_text)

        await pros.delete()
    else:
        await m.reply_text(
            f"Surah dengan nama '{surah_name.capitalize()}' tidak ditemukan."
        )
        await pros.delete()
