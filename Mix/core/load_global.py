
from team.nandev.database import udB
from team.nandev.class_log import LOGGER
from config import GMUTE_USER, GBAN_USER

async def _global_users(c):
    LOGGER.info(f"Loading For Gbanned And Gmute User.")
    gmute = udB.get_list_from_var(c.me.id, "GMUTE", "USER")
    gbanu = udB.get_list_from_var(c.me.id, "GBANNED", "USER")
    try:
        for x in gmute:
            GMUTE_USER.add(x)
        for x in gbanu:
            GBAN_USER.add(x)
    except:
        pass