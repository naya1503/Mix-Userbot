# @TomiX

from datetime import datetime, timedelta
from time import time as waktunya

start_time = waktunya()
from team.nandev.database import cleanmode, ndB


async def get_time(seconds):
    lng = ndB.get_key("bahasa")
    count = 0
    up_time = ""
    time_list = []

    if lng == "en":
        time_suffix_list = [
            "s",
            "m",
            "h",
            "d",
            "w",
            "m",
            "y",
        ]
    elif lng == "id":
        time_suffix_list = ["d", "m", "j", "h", "m", "b", "t"]
    else:
        time_suffix_list = [
            "s",
            "m",
            "h",
            "d",
            "w",
            "m",
            "y",
        ]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        up_time += time_list.pop() + ":"

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


async def put_cleanmode(org, message_id):
    if org not in cleanmode:
        cleanmode[org] = []
    elif not isinstance(cleanmode[org], list):
        cleanmode[org] = [cleanmode[org]]
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=1),
    }
    cleanmode[org].append(put)
