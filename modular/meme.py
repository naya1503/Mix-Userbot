import requests

from Mix import *

__modles__ = "Meme"
__help__ = "Meme"


async def scrape_memes():
    memes = []
    try:
        url = "https://memeapi.dev/api/v1/memes"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            meme_data = data.get("data")
            if meme_data and "image" in meme_data:
                image_url = meme_data["image"]
                memes.append(image_url)
        else:
            print(f"Failed to scrape memes: {response.text}")
    except Exception as e:
        print(f"Failed to scrape memes: {e}")
    return memes


@ky.ubot("meme", sudo=True)
async def _(c: nlx, m):
    memes = await scrape_memes()
    if memes:
        for image_url in memes:
            await m.reply_photo(photo=image_url)
    else:
        await m.reply("Gagal mendapatkan meme. Silakan coba lagi nanti.")
