from asyncio import QueueEmpty

from pytgcalls.exceptions import NoActiveGroupCall, NotInGroupCallError
from pytgcalls.types import StreamAudioEnded, Update

from Mix import user
from Mix.core.pytgcalls import queues


@user.pytgc_dec()
async def _(_, chat: int):
    try:
        queues.clear(chat)
    except QueueEmpty:
        pass


@user.pytgc_dec()
async def _(c: user, u: Update):
    if isinstance(u, StreamAudioEnded):
        queues.task_done(u.chat_id)
        if queues.is_empty(u.chat_id):
            try:
                await c.call_py.leave_group_call(u.chat_id)
            except (NotInGroupCallError, NoActiveGroupCall):
                pass
        else:
            await c.change_stream(u.chat_id, queues.get(u.chat_id)["file"])
