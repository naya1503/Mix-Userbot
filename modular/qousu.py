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


from Mix import *
from Mix.core.http import post


async def quotly(messages):
    if not isinstance(messages, list):
        messages = [messages]

        payload = {
            "type": "quote",
            "format": "png",
            "backgroundColor": "#1b1429",
            "messages": [
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
                    "chatId": (
                        m.forward_from.id
                        if m.forward_from
                        else m.from_user.id
                    ),
                    "avatar": True,
                    "from": (
                        {
                            "id": m.from_user.id,
                            "username": (
                                m.from_user.username
                                if m.from_user.username
                                else ""
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
                                m.forward_from.username
                                if m.forward_from.username
                                else ""
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
                        if len(messages) == 1
                        else {}
                    ),
                }
                for message in messages
            ],
        }
        response = await post("quotly", params={"payload": str(payload)})
        if response.ok:
            response.result = b64decode(
                sub("data:image/png;base64", "", response.result)
            )
        return response
