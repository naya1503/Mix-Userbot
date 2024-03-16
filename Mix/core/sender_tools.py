# Gojo_satoru
from traceback import format_exc
from typing import Tuple

from hydrogram.enums import MessageEntityType as entity
from team.nandev.class_log import LOGGER

from Mix import Users, user

from .msgty import Types


async def send_cmd(c: user, msgtype: int):
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


async def extract_user(c, m) -> Tuple[int, str, str]:
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
                    sone = Users.get_user_info(user_id)
                    user_first_name = sone["name"]
                    user_name = sone["username"]
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
