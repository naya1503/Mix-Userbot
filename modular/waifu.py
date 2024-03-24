import os

import requests

from Mix import *

__modles__ = "Waifu"
__help__ = "Waifu"


@ky.ubot("waifu", sudo=True)
async def get_waifu_image(c: nlx, m):
    category = m.text.lower()

    api_url = f"https://api.waifu.pics/sfw/{category}"
    response = await c.get(api_url)

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
