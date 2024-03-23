from io import BytesIO

import requests
from PIL import Image

from Mix import *

__modles__ = "Meme"
__help__ = "Meme"


async def scrape_memes(count_page=1):
    memes = []
    try:
        url = f"https://api.safone.dev/meme?page={count_page}"
        response = requests.get(url)
        data = response.json()
        results = data.get("results", [])
        for i, meme_data in enumerate(results, start=1):
            if "type" in meme_data and "image/jpeg" in meme_data["type"].lower():
                image_url = meme_data.get("image")
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    memes.append(BytesIO(image_response.content))
                else:
                    print(f"Failed to fetch image from URL: {image_url}")
    except Exception as e:
        print(f"Failed to scrape memes: {e}")
    return memes


@ky.ubot("meme", sudo=True)
async def _(c: nlx, m):
    try:
        command_parts = m.text.split(" ")
        if len(command_parts) == 1:
            count_page = 1
        elif len(command_parts) == 2:
            count_page = int(command_parts[1])
        else:
            await m.reply("Format perintah salah. Gunakan: meme [count_page]")
            return
    except ValueError:
        await m.reply("Halaman harus berupa bilangan bulat.")
        return

    memes = await scrape_memes(count_page)
    if memes:
        for meme_url in memes:
            await m.reply_photo(photo=meme_url)
    else:
        await m.reply("Gagal mendapatkan meme. Silakan coba lagi nanti.")
