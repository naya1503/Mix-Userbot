################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from Mix import *
from Mix.core.http import get

__modles__ = "Repository"
__help__ = "Repository"


@ky.ubot("repo|repository", sudo=True)
async def repo(c, m):
    link = await http.get(
        "https://api.github.com/repos/naya1503/Mix-Userbot/contributors"
    )
    orgnya = "".join(
        f"**{count}.** [{org['login']}]({org['html_url']})\n"
        for count, org in enumerate(link, start=1)
    )
    msg = f"""[Github](https://github.com/naya1503/Mix-Userbot) | [Group](t.me/kynansupport)
```----------------
| Contributors |
----------------```
{orgnya}"""
    await c.send_message(
        m.chat.id, msg, reply_to_message_id=ReplyCheck(m), disable_web_page_preview=True
    )
