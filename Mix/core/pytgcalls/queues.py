from asyncio import Queue as _Queue
from asyncio import QueueEmpty as Empty


class Queue(_Queue):
    _queue: list = []

    def clear(self):
        self._queue.clear()


queues = {}


async def put(chat_id, **kwargs):
    if chat_id not in queues:
        queues[chat_id] = Queue()
    await queues[chat_id].put({**kwargs})
    return queues[chat_id].qsize()


def get(chat_id):
    if chat_id in queues:
        try:
            return queues[chat_id].get_nowait()
        except Empty:
            return {}
    return {}


def is_empty(chat_id):
    return queues[chat_id].empty() if chat_id in queues else True


def task_done(chat_id):
    if chat_id in queues:
        try:
            queues[chat_id].task_done()
        except ValueError:
            pass


def clear(chat_id):
    if chat_id in queues:
        if queues[chat_id].empty():
            raise Empty
        else:
            queues[chat_id].clear()
    raise Empty
