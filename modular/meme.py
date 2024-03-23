import requests

from Mix import *

__modles__ = "Meme"
__help__ = "Meme"


async def scrape_memes():
    memes = []
    try:
        url = "https://memeapi.dev/meme"
        response = requests.get(url)
        if response.status_code == 200:
            meme_url = response.text
            memes.append(meme_url)
        else:
            print(f"Failed to scrape memes: {response.text}")
    except Exception as e:
        print(f"Failed to scrape memes: {e}")
    return memes


@ky.ubot("meme", sudo=True)
async def _(c: nlx, m):
    memes = await scrape_memes()
    if memes:
        for meme_url in memes:
            await m.reply_photo(photo=meme_url)
    else:
        await m.reply("Gagal mendapatkan meme. Silakan coba lagi nanti.")
