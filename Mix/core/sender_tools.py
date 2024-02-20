# Gojo_satoru
from Mix import user

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
