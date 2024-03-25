import io
import os

import requests

from Mix import *

__modles__ = "Waifu"
__help__ = get_cgr("help_waif")


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
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) > 1:
        category = m.text.split(maxsplit=1)[1].lower()
    else:
        categories_text = "\n".join(
            [f"{i+0}) <code>{cat}</code>" for i, cat in enumerate(categories, start=1)]
        )
        await m.reply(cgr("waif_1").format(em.gagal, categories_text))
        await pros.delete()
        return

    api_url = f"https://api.waifu.pics/sfw/{category}"
    response = requests.get(api_url)

    if response.ok:
        image_url = response.json()["url"]
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            await download_and_send_image(c, m, image_url, image_response.content)
            await pros.delete()
        else:
            await m.reply(f"{em.gagal} **Gagal mengunduh gambar.**")
            await pros.delete()
    else:
        await m.reply(f"{em.gagal} **Gagal mengambil gambar.**")
        await pros.delete()


async def download_and_send_image(client, message, image_url, image_content):
    image_bytes = io.BytesIO(image_content)
    image_bytes.name = "image.jpg"

    await client.send_photo(message.chat.id, photo=image_bytes)

    folder_path = "waifu_images"
    os.makedirs(folder_path, exist_ok=True)
    filename = image_url.split("/")[-1]
    filepath = os.path.join(folder_path, filename)

    if os.path.exists(filepath):
        os.remove(filepath)
