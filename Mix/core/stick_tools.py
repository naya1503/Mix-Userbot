################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty || William || Gojo_Satoru
"""
################################################################

import re
import os
from pyrogram import emoji
from team.nandev.class_log import LOGGER


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


async def con_tgs(pat, file_name):
    try:
        mp4_path = pat.replace(f"{file_name}.tgs", f"{file_name}.mp4")
        os.system(f"ffmpeg -i {pat} {mp4_path}")
        return mp4_path
    except Exception as e:
        LOGGER.error(f"{e}")
        return None


EMOJI_PATTERN = get_emoji_regex()
SUPPORTED_TYPES = ["jpeg", "png", "webp"]
