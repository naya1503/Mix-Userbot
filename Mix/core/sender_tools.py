# Gojo_satoru
import re
from html import escape
from traceback import format_exc
from typing import List, Tuple

from pyrogram.enums import MessageEntityType as entity
from team.nandev.class_log import LOGGER

from Mix import Users, nlx

from .msgty import Types
from .parser import escape_markdown

parse_words = [
    "first",
    "last",
    "fullname",
    "id",
    "mention",
    "username",
    "chatname",
]


async def send_cmd(c: nlx, msgtype: int):
    GET_FORMAT = {
        Types.TEXT.value: c.send_message,
        Types.DOCUMENT.value: c.send_document,
        Types.PHOTO.value: c.send_photo,
        Types.VIDEO.value: c.send_video,
        Types.STICKER.value: c.send_sticker,
        Types.AUDIO.value: c.send_audio,
        Types.VOICE.value: c.send_voice,
        Types.VIDEO_NOTE.value: c.send_video_note,
        Types.ANIMATION.value: c.send_animation,
        Types.ANIMATED_STICKER.value: c.send_sticker,
        Types.CONTACT: c.send_contact,
    }
    return GET_FORMAT[msgtype]


async def extract_user(c: nlx, m) -> Tuple[int, str, str]:
    """Extract the user from the provided message."""
    user_id = None
    user_first_name = None
    user_name = None
    user_found = None

    if m.reply_to_message and m.reply_to_message.from_user:
        user_id = m.reply_to_message.from_user.id
        user_first_name = m.reply_to_message.from_user.first_name
        user_name = m.reply_to_message.from_user.username

    elif len(m.text.split()) > 1:
        if len(m.entities) > 1:
            required_entity = m.entities[1]
            if required_entity.type == entity.TEXT_MENTION:
                user_id = required_entity.user.id
                user_first_name = required_entity.user.first_name
                user_name = required_entity.user.username
            elif required_entity.type in (entity.MENTION, entity.PHONE_NUMBER):
                # new long user ids are identified as phone_number
                user_found = m.text[
                    required_entity.offset : (
                        required_entity.offset + required_entity.length
                    )
                ]

                try:
                    user_found = int(user_found)
                except (ValueError, Exception) as ef:
                    if "invalid literal for int() with base 10:" in str(ef):
                        user_found = str(user_found)
                    else:
                        LOGGER.error(ef)
                        LOGGER.error(format_exc())

                try:
                    sone = Users.get_user_info(user_found)
                    user_id = sone["_id"]
                    user_first_name = sone["name"]
                    user_name = sone["username"]
                except KeyError:
                    # If user not in database
                    try:
                        sone = await c.get_users(user_found)
                    except Exception:
                        try:
                            user_r = await c.resolve_peer(user_found)
                            sone = await c.get_users(user_r.user_id)
                        except Exception as ef:
                            return await m.reply_text(f"User not found ! Error: {ef}")
                    user_id = sone.id
                    user_first_name = sone.first_name
                    user_name = sone.username
                except Exception as ef:
                    user_id = user_found
                    user_first_name = user_found
                    user_name = ""
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())

        else:
            try:
                user_id = int(m.text.split()[1])
            except (ValueError, Exception) as ef:
                if "invalid literal for int() with base 10:" in str(ef):
                    user_id = (
                        str(m.text.split()[1])
                        if (m.text.split()[1]).startswith("@")
                        else None
                    )
                else:
                    user_id = m.text.split()[1]
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())

            if user_id is not None:
                try:
                    user = await c.get_users(user_id)
                    user_first_name = user.first_name
                    user_name = user.username
                except Exception as ef:
                    try:
                        sone = await c.get_users(user_id)
                    except Exception:
                        try:
                            user_r = await c.resolve_peer(user_found)
                            sone = await c.get_users(user_r.user_id)
                        except Exception as ef:
                            return await m.reply_text(f"User not found ! Error: {ef}")
                    user_first_name = sone.first_name
                    user_name = sone.username
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())

    else:
        user_id = m.from_user.id
        user_first_name = m.from_user.first_name
        user_name = m.from_user.username

    return user_id, user_first_name, user_name


SMART_OPEN = "“"
SMART_CLOSE = "”"
START_CHAR = ("'", '"', SMART_OPEN)


async def escape_one(text: str, valids: List[str]) -> str:
    new_text = ""
    idx = 0
    while idx < len(text):
        if text[idx] == "{":
            if idx + 1 < len(text) and text[idx + 1] == "{":
                idx += 2
                new_text += "{{{{"
                continue
            success = False
            for v in valids:
                if text[idx:].startswith("{" + v + "}"):
                    success = True
                    break
            if success:
                new_text += text[idx : idx + len(v) + 2]
                idx += len(v) + 2
                continue
            new_text += "{{"

        elif text[idx] == "}":
            if idx + 1 < len(text) and text[idx + 1] == "}":
                idx += 2
                new_text += "}}}}"
                continue
            new_text += "}}"

        else:
            new_text += text[idx]
        idx += 1

    return new_text


import re


async def escape_tag(
    ore: int,
    text: str,
    parse_words: list,
) -> str:
    orang = await nlx.get_users(ore)
    if not orang:
        return ""
    text = re.sub(r"~ \[.*?\|.*?\]", "", text)

    teks = await escape_one(text, parse_words)
    if teks:
        teks = teks.format(
            first=escape(orang.first_name),
            last=escape(orang.last_name or orang.first_name),
            mention=orang.mention,
            username=(
                "@" + (await escape_markdown(escape(orang.username)))
                if orang.username
                else orang.mention
            ),
            fullname=" ".join(
                (
                    [
                        escape(orang.first_name),
                        escape(orang.last_name),
                    ]
                    if orang.last_name
                    else [escape(orang.first_name)]
                ),
            ),
            id=orang.id,
        )
    else:
        teks = ""

    return teks


async def split_quotes(text: str):
    """Split quotes in text."""
    if not any(text.startswith(char) for char in START_CHAR):
        return text.split(None, 1)
    counter = 1  # ignore first char -> is some kind of quote
    while counter < len(text):
        if text[counter] == "\\":
            counter += 1
        elif text[counter] == text[0] or (
            text[0] == SMART_OPEN and text[counter] == SMART_CLOSE
        ):
            break
        counter += 1
    else:
        return text.split(None, 1)

    # 1 to avoid starting quote, and counter is exclusive so avoids ending
    key = await remove_escapes(text[1:counter].strip())
    # index will be in range, or `else` would have been executed and returned
    rest = text[counter + 1 :].strip()
    if not key:
        key = text[0] + text[0]
    return list(filter(None, [key, rest]))


async def remove_escapes(text: str) -> str:
    """Remove the escaped from message."""
    res = ""
    is_escaped = False
    for counter in range(len(text)):
        if is_escaped:
            res += text[counter]
            is_escaped = False
        elif text[counter] == "\\":
            is_escaped = True
        else:
            res += text[counter]
    return res
