import requests
import subprocess

from Mix import *

__modles__ = "Meme"
__help__ = "Meme"


async def scrape_memes(count_page=1):
    memes = []
    try:
        command = f'curl -X GET "https://api.safone.dev/meme?page={count_page}" -H "accept: application/json"'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            data = json.loads(output)
            results = data.get("results", [])
            for meme_data in results:
                if "image/jpeg" in meme_data.get("type", "").lower():
                    image_url = meme_data.get("image")
                    memes.append(image_url)
        else:
            print(f"Failed to scrape memes: {error.decode()}")
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
        for image_url in memes:
            await m.reply_photo(photo=image_url)
    else:
        await m.reply("Gagal mendapatkan meme. Silakan coba lagi nanti.")
