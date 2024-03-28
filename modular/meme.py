import os

import requests

from Mix import *

__modles__ = "Meme"
__help__ = """
 Meme
• Perintah: `{0}meme`
• Penjelasan: Untuk generate random meme.
"""


TEMP_DIR = "temp"


async def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if not os.path.exists(TEMP_DIR):
                os.makedirs(TEMP_DIR)
            file_path = os.path.join(TEMP_DIR, "meme.jpg")
            with open(file_path, "wb") as file:
                file.write(response.content)
            return file_path
        else:
            print(f"Failed to download image: {response.text}")
            return None
    except Exception as e:
        print(f"Failed to download image: {e}")
        return None


async def scrape_memes():
    try:
        url = "https://memeapi.dev/meme"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            meme_url = data.get("data")
            return meme_url
        else:
            print(f"Failed to scrape memes: {response.text}")
            return None
    except Exception as e:
        print(f"Failed to scrape memes: {e}")
        return None


@ky.ubot("meme", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    try:
        meme_url = await scrape_memes()
        if meme_url:
            image_path = await download_image(meme_url)
            if image_path:
                await m.reply_photo(photo=image_path)
                os.remove(image_path)
                await pros.delete()
            else:
                await m.reply(
                    f"{em.gagal} Gagal mendownload gambar. Silakan coba lagi nanti."
                )
                await pros.delete()
        else:
            await m.reply(
                f"{em.gagal} Gagal mendapatkan URL gambar. Silakan coba lagi nanti."
            )
            await pros.delete()
    except Exception as e:
        print(f"Failed to process meme: {e}")
        await m.reply(f"{em.gagal} Terjadi kesalahan dalam pemrosesan meme.")
        await pros.delete()
