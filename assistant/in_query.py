from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Help Menu!",
            description=f"Menu Bantuan",
            thumb_url="https://telegra.ph//file/57376cf2486052ffae0ad.jpg",
            input_message_content=InputTextMessageContent("help"),
        ),
    ]
)
