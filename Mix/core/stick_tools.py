################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty || William || Gojo_Satoru
"""
################################################################

import asyncio
import os
import re

from PIL import Image
from pyrogram import emoji


def get_emoji_regex():
    e_list = [
        getattr(emoji, e).encode("unicode-escape").decode("ASCII")
        for e in dir(emoji)
        if not e.startswith("_")
    ]
    # to avoid re.error excluding char that start with '*'
    e_sort = sorted([x for x in e_list if not x.startswith("*")], reverse=True)
    # Sort emojis by length to make sure multi-character emojis are
    # matched first
    pattern_ = f"({'|'.join(e_sort)})"
    return re.compile(pattern_)


def resize_image(filename: str) -> str:
    im = Image.open(filename)
    maxsize = 512
    scale = maxsize / max(im.width, im.height)
    sizenew = (int(im.width * scale), int(im.height * scale))
    im = im.resize(sizenew, Image.NEAREST)
    downpath, f_name = os.path.split(filename)
    # not hardcoding png_image as "sticker.png"
    # not hardcoding png_image as "sticker.png"
    png_image = os.path.join(downpath, f"{f_name.split('.', 1)[0]}.png")
    im.save(png_image, "PNG")
    if png_image != filename:
        os.remove(filename)
    return png_image


async def convert_video(filename: str) -> str:
    downpath, f_name = os.path.split(filename)
    webm_video = os.path.join(downpath, f"{f_name.split('.', 1)[0]}.webm")
    cmd = [
        "downloads",
        "-loglevel",
        "quiet",
        "-i",
        filename,
        "-t",
        "00:00:03",
        "-vf",
        "fps=30",
        "-c:v",
        "vp9",
        "-b:v:",
        "500k",
        "-preset",
        "ultrafast",
        "-s",
        "512x512",
        "-y",
        "-an",
        webm_video,
    ]

    proc = await asyncio.create_subprocess_exec(*cmd)
    # Wait for the subprocess to finish
    await proc.communicate()

    if webm_video != filename:
        os.remove(filename)
    return webm_video


EMOJI_PATTERN = get_emoji_regex()
SUPPORTED_TYPES = ["jpeg", "png", "webp"]
