################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

__modles__ = "Quote"
__help__ = "
Help Command Quote

• Perintah: <code>{0}q</code>
• Penjelasan: Untuk membuat qoute teks.
"

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


bg_jing = [
    "Black",
    "Navy",
    "DarkBlue",
    "MediumBlue",
    "Blue",
    "DarkGreen",
    "Green",
    "Teal",
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "MediumSpringGreen",
    "Lime",
    "SpringGreen",
    "Aqua",
    "Cyan",
    "MidnightBlue",
    "DodgerBlue",
    "LightSeaGreen",
    "ForestGreen",
    "SeaGreen",
    "DarkSlateGray",
    "DarkSlateGrey",
    "LimeGreen",
    "MediumSeaGreen",
    "Turquoise",
    "RoyalBlue",
    "SteelBlue",
    "DarkSlateBlue",
    "MediumTurquoise",
    "Indigo  ",
    "DarkOliveGreen",
    "CadetBlue",
    "CornflowerBlue",
    "RebeccaPurple",
    "MediumAquaMarine",
    "DimGray",
    "DimGrey",
    "SlateBlue",
    "OliveDrab",
    "SlateGray",
    "SlateGrey",
    "LightSlateGray",
    "LightSlateGrey",
    "MediumSlateBlue",
    "LawnGreen",
    "Chartreuse",
    "Aquamarine",
    "Maroon",
    "Purple",
    "Olive",
    "Gray",
    "Grey",
    "SkyBlue",
    "LightSkyBlue",
    "BlueViolet",
    "DarkRed",
    "DarkMagenta",
    "SaddleBrown",
    "DarkSeaGreen",
    "LightGreen",
    "MediumPurple",
    "DarkViolet",
    "PaleGreen",
    "DarkOrchid",
    "YellowGreen",
    "Sienna",
    "Brown",
    "DarkGray",
    "DarkGrey",
    "LightBlue",
    "GreenYellow",
    "PaleTurquoise",
    "LightSteelBlue",
    "PowderBlue",
    "FireBrick",
    "DarkGoldenRod",
    "MediumOrchid",
    "RosyBrown",
    "DarkKhaki",
    "Silver",
    "MediumVioletRed",
    "IndianRed ",
    "Peru",
    "Chocolate",
    "Tan",
    "LightGray",
    "LightGrey",
    "Thistle",
    "Orchid",
    "GoldenRod",
    "PaleVioletRed",
    "Crimson",
    "Gainsboro",
    "Plum",
    "BurlyWood",
    "LightCyan",
    "Lavender",
    "DarkSalmon",
    "Violet",
    "PaleGoldenRod",
    "LightCoral",
    "Khaki",
    "AliceBlue",
    "HoneyDew",
    "Azure",
    "SandyBrown",
    "Wheat",
    "Beige",
    "WhiteSmoke",
    "MintCream",
    "GhostWhite",
    "Salmon",
    "AntiqueWhite",
    "Linen",
    "LightGoldenRodYellow",
    "OldLace",
    "Red",
    "Fuchsia",
    "Magenta",
    "DeepPink",
    "OrangeRed",
    "Tomato",
    "HotPink",
    "Coral",
    "DarkOrange",
    "LightSalmon",
    "Orange",
    "LightPink",
    "Pink",
    "Gold",
    "PeachPuff",
    "NavajoWhite",
    "Moccasin",
    "Bisque",
    "MistyRose",
    "BlanchedAlmond",
    "PapayaWhip",
    "LavenderBlush",
    "SeaShell",
    "Cornsilk",
    "LemonChiffon",
    "FloralWhite",
    "Snow",
    "Yellow",
    "LightYellow",
    "Ivory",
    "White",
]