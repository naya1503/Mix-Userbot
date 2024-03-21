import random

import requests
from gpytranslate import Translator
from pyrogram.errors import *

from Mix import *

__modles__ = "TOD"
__help__ = get_cgr("help_tod")

translator = Translator()


async def get_truth(category="classic|kids|party|hot|mixed"):
    try:
        categories = category.split("|")
        random_category = random.choice(categories)
        response = requests.get(
            f"https://api.safone.dev/truth?category={random_category}"
        )
        response.raise_for_status()
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
        response.raise_for_status()
        data = response.json()
        if "dare" in data:
            dare = await translator.translate(data["dare"], "en", "id")
            return dare
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Failed to fetch Dare:", e)
        return None


"""
@ky.ubot("dare", sudo=True)
async def dare_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    proses = await m.reply(cgr("proses").format(em.proses))
    dare = await get_dare()
    if dare:
        response_text = dare.get("text", dare.get("text_raw"))
        if response_text:
            response = await m.reply_text(cgr("tod_1").format(em.sukses, response_text))
        else:
            response = await m.reply_text(cgr("tod_2").format(em.gagal))
    else:
        response = await m.reply_text(cgr("tod_2").format(em.gagal))
    await m.reply(response)
    await proses.delete()


@ky.ubot("truth", sudo=True)
async def truth_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    proses = await m.reply(cgr("proses").format(em.proses))
    try:
        truth = await get_truth()
        response_text = truth.get("text", truth.get("text_raw"))
        if response_text:
            response = cgr("tod_3").format(em.sukses, response_text)
        else:
            response = cgr("tod_4").format(em.gagal)
        await proses.delete()
        await m.reply(response)
    except MessageTooLong:
        pass
    except Exception as e:
        await m.reply(f"Error :\n `{e}`")
"""


@ky.ubot("dare", sudo=True)
async def dare_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    proses = await m.reply(cgr("proses").format(em.proses))
    try:
        dare = await get_dare()
        if dare:
            response_text = dare.get("text", dare.get("text_raw"))
            if response_text:
                response_parts = [
                    response_text[i : i + 4000]
                    for i in range(0, len(response_text), 4000)
                ]
                for part in response_parts:
                    await m.reply_text(cgr("tod_1").format(em.sukses, part))
            else:
                await m.reply_text(cgr("tod_2").format(em.gagal))
        else:
            await m.reply_text(cgr("tod_2").format(em.gagal))
    except MessageTooLong:
        pass
    await proses.delete()


@ky.ubot("truth", sudo=True)
async def truth_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    proses = await m.reply(cgr("proses").format(em.proses))
    try:
        truth = await get_truth()
        response_text = truth.get("text", truth.get("text_raw"))
        if response_text:
            response_parts = [
                response_text[i : i + 4000] for i in range(0, len(response_text), 4000)
            ]
            for part in response_parts:
                await m.reply_text(cgr("tod_3").format(em.sukses, part))
        else:
            await m.reply_text(cgr("tod_4").format(em.gagal))
    except MessageTooLong:
        pass
    await proses.delete()
