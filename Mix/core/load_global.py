
from team.nandev.database import udB
from team.nandev.class_log import LOGGER
from pyrogram import filters
from Mix import user

GBAN_USER = filters.user()
GMUTE_USER = filters.user()

async def _global_users():
    LOGGER.info(f"Loading For Gbanned And Gmute User.")
    gmute = udB.get_list_from_var(user.me.id, "GMUTE", "USER")
    gbanu = udB.get_list_from_var(user.me.id, "GBANNED", "USER")
    try:
        for x in gmute:
            GMUTE_USER.add(x)
        for x in gbanu:
            GBAN_USER.add(x)
    except:
        pass