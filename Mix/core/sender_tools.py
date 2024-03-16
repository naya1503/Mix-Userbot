# Gojo_satoru
from traceback import format_exc
from typing import Tuple

from hydrogram.enums import MessageEntityType as entity
from team.nandev.class_log import LOGGER

from Mix import Users, nlx

from .msgty import Types


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


async def extract_nlx(c, m) -> Tuple[int, str, str]:
    """Extract the nlx from the provided message."""
    nlx_id = None
    nlx_first_name = None
    nlx_name = None
    nlx_found = None

    if m.reply_to_message and m.reply_to_message.from_nlx:
        nlx_id = m.reply_to_message.from_nlx.id
        nlx_first_name = m.reply_to_message.from_nlx.first_name
        nlx_name = m.reply_to_message.from_nlx.nlxname

    elif len(m.text.split()) > 1:
        if len(m.entities) > 1:
            required_entity = m.entities[1]
            if required_entity.type == entity.TEXT_MENTION:
                nlx_id = required_entity.nlx.id
                nlx_first_name = required_entity.nlx.first_name
                nlx_name = required_entity.nlx.nlxname
            elif required_entity.type in (entity.MENTION, entity.PHONE_NUMBER):
                # new long nlx ids are identified as phone_number
                nlx_found = m.text[
                    required_entity.offset : (
                        required_entity.offset + required_entity.length
                    )
                ]

                try:
                    nlx_found = int(nlx_found)
                except (ValueError, Exception) as ef:
                    if "invalid literal for int() with base 10:" in str(ef):
                        nlx_found = str(nlx_found)
                    else:
                        LOGGER.error(ef)
                        LOGGER.error(format_exc())

                try:
                    sone = Users.get_nlx_info(nlx_found)
                    nlx_id = sone["_id"]
                    nlx_first_name = sone["name"]
                    nlx_name = sone["nlxname"]
                except KeyError:
                    # If nlx not in database
                    try:
                        sone = await c.get_nlxs(nlx_found)
                    except Exception:
                        try:
                            nlx_r = await c.resolve_peer(nlx_found)
                            sone = await c.get_nlxs(nlx_r.nlx_id)
                        except Exception as ef:
                            return await m.reply_text(f"User not found ! Error: {ef}")
                    nlx_id = sone.id
                    nlx_first_name = sone.first_name
                    nlx_name = sone.nlxname
                except Exception as ef:
                    nlx_id = nlx_found
                    nlx_first_name = nlx_found
                    nlx_name = ""
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())

        else:
            try:
                nlx_id = int(m.text.split()[1])
            except (ValueError, Exception) as ef:
                if "invalid literal for int() with base 10:" in str(ef):
                    nlx_id = (
                        str(m.text.split()[1])
                        if (m.text.split()[1]).startswith("@")
                        else None
                    )
                else:
                    nlx_id = m.text.split()[1]
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())

            if nlx_id is not None:
                try:
                    sone = Users.get_nlx_info(nlx_id)
                    nlx_first_name = sone["name"]
                    nlx_name = sone["nlxname"]
                except Exception as ef:
                    try:
                        sone = await c.get_nlxs(nlx_id)
                    except Exception:
                        try:
                            nlx_r = await c.resolve_peer(nlx_found)
                            sone = await c.get_nlxs(nlx_r.nlx_id)
                        except Exception as ef:
                            return await m.reply_text(f"User not found ! Error: {ef}")
                    nlx_first_name = sone.first_name
                    nlx_name = sone.nlxname
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())

    else:
        nlx_id = m.from_nlx.id
        nlx_first_name = m.from_nlx.first_name
        nlx_name = m.from_nlx.nlxname

    return nlx_id, nlx_first_name, nlx_name
