import json
import subprocess

from Mix import *

__modles__ = "Meme"
__help__ = "Meme"


async def scrape_memes(count_page=1):
    memes = []
    try:
        command = f'curl -X GET "https://api.safone.dev/meme?page={count_page}" -H "accept: application/json"'
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        if process.returncode == 0:
            try:
                data = json.loads(output)
                results = data.get("results", [])
                for meme_data in results:
                    if (
                        "image/jpeg" in meme_data.get("type", "").lower()
                        or "image/jpg" in meme_data.get("type", "").lower()
                    ):
                        image_url = meme_data.get("image")
                        memes.append(image_url)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
        else:
            print(f"Failed to scrape memes: {error.decode()}")
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
