################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty || William || Gojo_Satoru
"""
################################################################

import re
from pyrogram import emoji
from Mix import user
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
 
async def con_tgs(pat):
    try:
        gif_path = pat.replace(".tgs", ".gif")
        mp4_path = pat.replace(".tgs", ".mp4")

        gas = f"ffmpeg -i {file_path} {gif_path}"
        await user.run_cmd(gas)
        gs = f"ffmpeg -i {file_path} {mp4_path}"
        await user.run_cmd(gs)
        return gif_path, mp4_path
    except Exception as e:
        LOGGER.error(f"{e}")
        return None, None
    
EMOJI_PATTERN = get_emoji_regex()
SUPPORTED_TYPES = ["jpeg", "png", "webp"]