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
from random import choice

async def quotly(messages):
      if not isinstance(messages, list):
            messages = [messages]

            payload = {
                "type": "quote",
                "format": "png",
                "backgroundColor": "#1b1429",
                "messages": [
                    {
                        "entities": [
                            {
                                "type": entity.type,
                                "offset": entity.offset,
                                "length": entity.length,
                            }
                            for entity in message.entities
                        ]
                        if message.entities
                        else [],
                        "chatId": message.forward_from.id
                        if message.forward_from
                        else message.from_user.id,
                        "avatar": True,
                        "from": {
                            "id": message.from_user.id,
                            "username": message.from_user.username
                            if message.from_user.username
                            else "",
                            "photo": {
                                "small_file_id": message.from_user.photo.small_file_id,
                                "small_photo_unique_id": message.from_user.photo.small_photo_unique_id,
                                "big_file_id": message.from_user.photo.big_file_id,
                                "big_photo_unique_id": message.from_user.photo.big_photo_unique_id,
                            }
                            if message.from_user.photo
                            else "",
                            "type": message.chat.type,
                            "name": _get_name(message.from_user),
                        }
                        if not message.forward_from
                        else {
                            "id": message.forward_from.id,
                            "username": message.forward_from.username
                            if message.forward_from.username
                            else "",
                            "photo": {
                                "small_file_id": message.forward_from.photo.small_file_id,
                                "small_photo_unique_id": message.forward_from.photo.small_photo_unique_id,
                                "big_file_id": message.forward_from.photo.big_file_id,
                                "big_photo_unique_id": message.forward_from.photo.big_photo_unique_id,
                            }
                            if message.forward_from.photo
                            else "",
                            "type": message.chat.type,
                            "name": _get_name(message.forward_from),
                        },
                        "text": message.text if message.text else "",
                        "replyMessage": (
                            {
                                "name": _get_name(
                                message.reply_to_message.from_user),
                                "text": message.reply_to_message.text,
                                "chatId": message.reply_to_message.from_user.id}
                            if message.reply_to_message
                            else {}
                        )
                        if len(messages) == 1
                        else {},
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


