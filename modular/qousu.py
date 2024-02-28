################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

"""
__modles__ = "Quote"
__help__ = "
Help Command Quote

• Perintah: <code>{0}q</code>
• Penjelasan: Untuk membuat qoute teks.
"""


from base64 import b64decode

from pyrogram.types import User

from Mix import *
from Mix.core.http import post


def _get_name(from_user: User) -> str:
    return f"{from_user.first_name} {from_user.last_name or ''}".rstrip()


async def quotly(ms):
    if not isinstance(ms, list):
        ms = [ms]

    payload = {
        "type": "quote",
        "format": "png",
        "backgroundColor": "#1b1429",
        "ms": [
            {
                "entities": (
                    [
                        {
                            "type": entity.type,
                            "offset": entity.offset,
                            "length": entity.length,
                        }
                        for entity in m.entities
                    ]
                    if m.entities
                    else []
                ),
                "chatId": (m.forward_from.id if m.forward_from else m.from_user.id),
                "avatar": True,
                "from": (
                    {
                        "id": m.from_user.id,
                        "username": (
                            m.from_user.username if m.from_user.username else ""
                        ),
                        "photo": (
                            {
                                "small_file_id": m.from_user.photo.small_file_id,
                                "small_photo_unique_id": m.from_user.photo.small_photo_unique_id,
                                "big_file_id": m.from_user.photo.big_file_id,
                                "big_photo_unique_id": m.from_user.photo.big_photo_unique_id,
                            }
                            if m.from_user.photo
                            else ""
                        ),
                        "type": m.chat.type,
                        "name": _get_name(m.from_user),
                    }
                    if not m.forward_from
                    else {
                        "id": m.forward_from.id,
                        "username": (
                            m.forward_from.username if m.forward_from.username else ""
                        ),
                        "photo": (
                            {
                                "small_file_id": m.forward_from.photo.small_file_id,
                                "small_photo_unique_id": m.forward_from.photo.small_photo_unique_id,
                                "big_file_id": m.forward_from.photo.big_file_id,
                                "big_photo_unique_id": m.forward_from.photo.big_photo_unique_id,
                            }
                            if m.forward_from.photo
                            else ""
                        ),
                        "type": m.chat.type,
                        "name": _get_name(m.forward_from),
                    }
                ),
                "text": m.text if m.text else "",
                "replyMessage": (
                    (
                        {
                            "name": _get_name(m.reply_to_message.from_user),
                            "text": m.reply_to_message.text,
                            "chatId": m.reply_to_message.from_user.id,
                        }
                        if m.reply_to_message
                        else {}
                    )
                    if len(ms) == 1
                    else {}
                ),
            }
            for m in ms
        ],
    }
    convert_payload = {
        "type": payload["type"],
        "format": payload["format"],
        "backgroundColor": payload["backgroundColor"],
        "ms": [
            {
                "entities": entity["entities"],
                "chatId": entity["chatId"],
                "avatar": entity["avatar"],
                "from": entity["from"],
                "text": entity["text"],
                "replyMessage": entity["replyMessage"],
            }
            for entity in payload["ms"]
        ],
    }

    response = await post("quotly", json=convert_payload)
    if response.ok:
        response.result = b64decode(sub("data:image/png;base64", "", response.result))
    return response
