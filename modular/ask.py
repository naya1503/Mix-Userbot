import random

import requests

from Mix import *

__modles__ = "TOD"
__help__ = "TOD"


async def get_truth(category="classic|kids|party|hot|mixed"):
    try:
        categories = category.split("|")
        random_category = random.choice(categories)
        response = requests.get(
            f"https://api.safone.dev/truth?category={random_category}"
        )
        data = response.json()
        if response.status_code == 200 and "truth" in data:
            return data["truth"]
        else:
            return None
    except Exception as e:
        print("Failed to fetch Truth:", e)
        return None


async def get_dare(category="classic|kids|party|hot|mixed"):
    try:
        categories = category.split("|")
        random_category = random.choice(categories)
        response = requests.get(
            f"https://api.safone.dev/dare?category={random_category}"
        )
        data = response.json()
        if response.status_code == 200 and "dare" in data:
            return data["dare"]
        else:
            return None
    except Exception as e:
        print("Failed to fetch Dare:", e)
        return None


@ky.ubot("dare", sudo=True)
async def dare_command(client, message):
    dare = await get_dare()
    if dare:
        response = f"Dare: {dare}"
    else:
        response = "Failed to fetch Dare. Please try again later."
    await message.reply_text(response)


@ky.ubot("truth", sudo=True)
async def truth_command(client, message):
    truth = await get_truth()
    if truth:
        response = f"Truth: {truth}"
    else:
        response = "Failed to fetch Truth. Please try again later."
    await message.reply_text(response)
