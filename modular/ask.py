import random
import requests
from gpytranslate import Translator
import asyncio

from Mix import *

__modles__ = "TOD"
__help__ = "TOD"

translator = Translator()


async def get_truth(category="classic|kids|party|hot|mixed"):
    try:
        categories = category.split("|")
        random_category = random.choice(categories)
        response = requests.get(
            f"https://api.safone.dev/truth?category={random_category}"
        )
        response.raise_for_status()  # Raise an error for non-200 status codes
        data = response.json()
        if "truth" in data:
            truth = await translator.translate(data["truth"], "en", "id")
            return truth
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Failed to fetch Truth:", e)
        return None


async def get_dare(category="classic|kids|party|hot|mixed"):
    try:
        categories = category.split("|")
        random_category = random.choice(categories)
        response = requests.get(
            f"https://api.safone.dev/dare?category={random_category}"
        )
        response.raise_for_status()  # Raise an error for non-200 status codes
        data = response.json()
        if "dare" in data:
            dare = await translator.translate(data["dare"], "en", "id")
            return dare
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Failed to fetch Dare:", e)
        return None


@ky.ubot("dare", sudo=True)
async def dare_command(client, message):
    proses = await message.reply(f"`Tunggu ...`")
    dare = await get_dare()
    response_text = dare.get('text', dare.get('text_raw'))
    if response_text:
        response = f"**Dare:** `{response_text}`"
    else:
        response = "**Gagal mengambil Dare. Silakan coba lagi nanti.**"
    await asyncio.gather(
        message.reply_text(response),
        proses.delete()
    )


@ky.ubot("truth", sudo=True)
async def truth_command(client, message):
    proses = await message.reply(f"`Tunggu ...`")
    truth = await get_truth()
    response_text = truth.get('text', truth.get('text_raw'))
    if response_text:
        response = f"**Truth :** `{response_text}`"
    else:
        response = "**Gagal mengambil Truth. Silakan coba lagi nanti.**"
    await asyncio.gather(
        message.reply_text(response),
        proses.delete()
    )
