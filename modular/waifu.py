import os

import requests

from Mix import *

__modles__ = "Waifu"
__help__ = "Waifu"


categories = [
    "waifu",
    "neko",
    "shinobu",
    "megumin",
    "bully",
    "cuddle",
    "cry",
    "hug",
    "awoo",
    "kiss",
    "lick",
    "pat",
    "smug",
    "bonk",
    "yeet",
    "blush",
    "smile",
    "wave",
    "highfive",
    "handhold",
    "nom",
    "bite",
    "glomp",
    "slap",
    "kill",
    "kick",
    "happy",
    "wink",
    "poke",
    "dance",
    "cringe",
]


@ky.ubot("waifu", sudo=True)
async def get_waifu_image(c: nlx, m):
    if len(m.command) > 1:
        category = m.text.split(maxsplit=1)[1].lower()
    else:
        categories_text = "\n".join(categories)
        await m.reply_text(
            f"Silakan pilih kategori dari daftar berikut:\n\n{categories_text}"
        )
        return

    api_url = f"https://api.waifu.pics/sfw/{category}"
    response = requests.get(api_url)

    if response.ok:
        image_url = response.json()["url"]
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            await download_and_send_image(c, m, image_url, image_response.content)
        else:
            await m.reply_text("Gagal mengunduh gambar.")
    else:
        await m.reply_text("Gagal mengambil gambar.")


async def download_and_send_image(client, message, image_url, image_content):
    await client.send_photo(message.chat.id, image_content)
    folder_path = "waifu_images"
    os.makedirs(folder_path, exist_ok=True)
    filename = image_url.split("/")[-1]
    filepath = os.path.join(folder_path, filename)
    os.remove(filepath)
