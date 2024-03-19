"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import re
from asyncio import sleep

from config import *
from Mix import *
from Mix.core.tools_music import *


@ky.ubot("play")
async def play(client: nlx, m):
    msg = await m.reply_text("🔄 **Processing ...**")
    chat_id = m.chat.id
    media = m.reply_to_message
    if not media and not " " in m.text:
        await msg.edit(
            "❗ __Send Me An Live Radio Link / YouTube Video Link / Reply To An Audio To Start Audio Streaming!__"
        )

    elif " " in m.text:
        text = m.text.split(" ", 1)
        query = text[1]
        if not "http" in query:
            return await msg.edit(
                "❗ __Send Me An Live Stream Link / YouTube Video Link / Reply To An Video To Start Video Streaming!__"
            )
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, query)
        if match:
            await msg.edit("🔄 **Starting YouTube Audio Stream ...**")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get("formats", [meta])
                for f in formats:
                    ytstreamlink = f["url"]
                link = ytstreamlink
            except Exception as e:
                return await msg.edit(f"❌ **YouTube Download Error !** \n\n`{e}`")
                print(e)

        else:
            await msg.edit("🔄 **Starting Live Audio Stream ...**")
            link = query

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_audio(link, repeat=False)
            AUDIO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_text(
                f"▶️ **Started [Audio Streaming]({query}) In {m.chat.title} !**"
            )
            """
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="⏸",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="▶️",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="⏹️",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
            """
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured !** \n\nError: `{e}`")
            return await group_call.stop()

    elif media.audio or media.document:
        await msg.edit("🔄 **Downloading ...**")
        audio = await client.download_media(media)

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_audio(audio, repeat=False)
            AUDIO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_text(
                f"▶️ **Started [Audio Streaming](@NATSUKISUPPORT_OFFICIAL) In {m.chat.title} !**"
            )
            """
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="⏸",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="▶️",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="⏹️",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
            """
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured !** \n\nError: `{e}`")
            return await group_call.stop()

    else:
        await msg.edit("💁🏻‍♂️ Do you want to search for a YouTube song?")


"""
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
"""
