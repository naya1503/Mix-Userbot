################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
import os
import platform
import sys
import traceback
################################################################
from datetime import datetime, timedelta
from io import BytesIO, StringIO
from subprocess import PIPE, Popen, TimeoutExpired
from time import perf_counter

import psutil
from psutil._common import bytes2human
from pytz import timezone

from Mix import *

__modles__ = "Devs"
__help__ = get_cgr("help_dev")


@ky.cegers("aktif")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    exx = c.get_arg(m)
    if not exx:
        exx = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(exx))
    udB.set_expired_date(user.me.id, expire_date)
    await m.reply(f"{em.sukses} Aktif {exx} hari.")
    return


@ky.cegers("cek")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    kmm = udB.get_expired_date(user.me.id)
    if kmm is None:
        await m.reply(f"{user.me.id} ga aktif!!")
        return
    else:
        rimen = (kmm - datetime.now()).days
        await m.reply(
            f"{user.me.id} aktif hingga {kmm.strftime('%d-%m-%Y %H:%M:%S')}. Sisa waktu aktif {rimen} hari."
        )
        return


@ky.cegers("nonaktif")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    udB.rem_expired_date(user.me.id)
    return await m.reply(f"{em.sukses} {user.me.id} expired telah dihapus")


@ky.ubot("sh", sudo=True)
@ky.bots("sh")
async def _(c, m):
    if len(m.command) < 2:
        return await m.reply(f"Input text!")
    cmd_text = m.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "Mix-Userbot#" if os.getuid() == 0 else "Mix-Userbot"
    text = f"{char} <code>{cmd_text}</code>\n\n"

    try:
        perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "Timeout expired!"
    else:
        perf_counter()
        if len(stdout) > 4096:
            anuk = await m.reply("Oversize, sending file...")
            file = open("output.txt", "w+")
            file.write(stdout)
            file.close()
            await c.send_document(
                m.chat.id,
                "output.txt",
                reply_to_message_id=m.id,
            )
            await anuk.delete()
            os.remove("output.txt")
        else:
            text += f"<code>{stdout}</code>"
        if stderr:
            text += f"<code>{stderr}</code>"
    await m.reply(text, quote=True)
    cmd_obj.kill()


@ky.ubot("trash", sudo=True)
async def _(c: user, m):
    if m.reply_to_message:
        try:
            if len(m.command) < 2:
                if len(str(m.reply_to_message)) > 4096:
                    with BytesIO(str.encode(str(m.reply_to_message))) as out_file:
                        out_file.name = "trash.txt"
                        return await m.reply_document(document=out_file)
                else:
                    return await m.reply(m.reply_to_message)
            else:
                value = eval(f"m.reply_to_message.{m.command[1]}")
                return await m.reply(value)
        except Exception as error:
            return await m.reply(str(error))
    else:
        return await m.reply("noob")


@ky.ubot("eval|ev", sudo=True)
@ky.cegers("ceval")
@ky.bots("eval|ev")
async def _(c, m):
    if not user.get_arg(m):
        return
    xx = await m.reply_text("Processing ...")
    cmd = m.text.split(" ", maxsplit=1)[1]
    reply_to_ = m.reply_to_message or m
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await user.aexec(cmd, c, m)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "<b>OUTPUT</b>:\n"
    final_output += f"<b>{evaluation.strip()}</b>"
    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output, quote=True)
    await xx.delete()


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@ky.ubot("host", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} Processing...")
    uname = platform.uname()
    softw = "Informasi Sistem\n"
    softw += f"Sistem   : {uname.system}\n"
    softw += f"Rilis    : {uname.release}\n"
    softw += f"Versi    : {uname.version}\n"
    softw += f"Mesin    : {uname.machine}\n"

    boot_time_timestamp = psutil.boot_time()

    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"Waktu Hidup: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"

    softw += "\nInformasi CPU\n"
    softw += "Physical cores   : " + str(psutil.cpu_count(logical=False)) + "\n"
    softw += "Total cores      : " + str(psutil.cpu_count(logical=True)) + "\n"
    cpufreq = psutil.cpu_freq()
    softw += f"Max Frequency    : {cpufreq.max:.2f}Mhz\n"
    softw += f"Min Frequency    : {cpufreq.min:.2f}Mhz\n"
    softw += f"Current Frequency: {cpufreq.current:.2f}Mhz\n\n"
    softw += "CPU Usage Per Core\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        softw += f"Core {i}  : {percentage}%\n"
    softw += "Total CPU Usage\n"
    softw += f"Semua Core: {psutil.cpu_percent()}%\n"

    softw += "\nBandwith Digunakan\n"
    softw += f"Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    softw += f"Download: {get_size(psutil.net_io_counters().bytes_recv)}\n"

    svmem = psutil.virtual_memory()
    softw += "\nMemori Digunakan\n"
    softw += f"Total     : {get_size(svmem.total)}\n"
    softw += f"Available : {get_size(svmem.available)}\n"
    softw += f"Used      : {get_size(svmem.used)}\n"
    softw += f"Percentage: {svmem.percent}%\n"

    await xx.edit(f"{softw}")


async def generate_sysinfo(workdir):
    # user total

    # uptime
    info = {
        "BOOT": (
            datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        )
    }
    # CPU
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    info["CPU"] = (
        f"{psutil.cpu_percent(interval=1)}% " f"({psutil.cpu_count()}) " f"{cpu_freq}"
    )
    # Memory
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()
    info["RAM"] = f"{bytes2human(vm.used)}, " f"/ {bytes2human(vm.total)}"
    info["SWAP"] = f"{bytes2human(sm.total)}, {sm.percent}%"
    # Disks
    du = psutil.disk_usage(workdir)
    dio = psutil.disk_io_counters()
    info["DISK"] = (
        f"{bytes2human(du.used)} / {bytes2human(du.total)} " f"({du.percent}%)"
    )
    if dio:
        info["DISK I/O"] = (
            f"R {bytes2human(dio.read_bytes)} | W {bytes2human(dio.write_bytes)}"
        )
    # Network
    nio = psutil.net_io_counters()
    info["NET I/O"] = (
        f"TX {bytes2human(nio.bytes_sent)} | RX {bytes2human(nio.bytes_recv)}"
    )
    # Sensors
    sensors_temperatures = psutil.sensors_temperatures()
    if sensors_temperatures:
        temperatures_list = [x.current for x in sensors_temperatures["coretemp"]]
        temperatures = sum(temperatures_list) / len(temperatures_list)
        info["TEMP"] = f"{temperatures}\u00b0C"
    info = {f"{key}:": value for (key, value) in info.items()}
    max_len = max(len(x) for x in info)
    return "\n" + "\n".join([f"{x:<{max_len}} {y}" for x, y in info.items()]) + ""


@ky.ubot("stats", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    response = await generate_sysinfo(c.workdir)
    await m.reply(
        f"{em.proses} # {user.me.first_name}\nStats : Total Usage\n" + response,
    )


def ban_all(c, m):
    chat_id = m.chat.id
    members = c.get_chat_members(chat_id)
    for member in members:
        if not member.user.is_self:
            c.kick_chat_member(chat_id, member.user.id)


def unban_all(c, m):
    chat_id = m.chat.id
    banned_members = c.get_chat_members_banned(chat_id)
    for banned_member in banned_members:
        c.unban_chat_member(chat_id, banned_member.user.id)


@ky.ubot("ban_all", sudo=True)
def ban_all_command(c, m):
    if m.from_user.id == m.chat.id:
        ban_all(c, m)


@ky.ubot("unban_all", sudo=True)
def unban_all_command(c, m):
    if m.from_user.id == m.chat.id:
        unban_all(c, m)
