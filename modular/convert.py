import asyncio
import os

from pyrogram.enums import MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from Mix import *

__modles__ = "Convert"
__help__ = "Convert"


@ky.ubot("toanime", sudo=True)
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    pros = await message.reply(cgr("proses").format(em.proses))
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                get_photo = message.reply_to_message.photo.file_id
            elif message.reply_to_message.sticker:
                get_photo = await c.dln(message.reply_to_message)
            elif message.reply_to_message.animation:
                get_photo = await c.dln(message.reply_to_message)
            else:
                return await pros.edit(f"{em.gagal} Silahkan balas ke media foto")
        else:
            if message.command[1] in ["foto", "profil", "photo"]:
                chat = (
                    message.reply_to_message.from_user
                    or message.reply_to_message.sender_chat
                )
                get = await c.get_chat(chat.id)
                photo = get.photo.big_file_id
                get_photo = await c.dln(photo)
    else:
        if len(message.command) < 2:
            return await pros.edit(f"{em.gagal} Silahkan balas ke media foto")
        else:
            try:
                get = await c.get_chat(message.command[1])
                photo = get.photo.big_file_id
                get_photo = await c.dln(photo)
            except Exception as error:
                return await pros.edit(cgr("err").format(em.gagal, error))
    await pros.edit(f"{em.proses} **Converting...**")
    await c.unblock_user("@qq_neural_anime_bot")
    send_photo = await c.send_photo("@qq_neural_anime_bot", get_photo)
    await asyncio.sleep(30)
    await send_photo.delete()
    await pros.delete()
    info = await c.resolve_peer("@qq_neural_anime_bot")
    anime_photo = []
    async for anime in c.search_messages(
        "@qq_neural_anime_bot", filter=MessagesFilter.PHOTO
    ):
        anime_photo.append(
            InputMediaPhoto(
                anime.photo.file_id, caption=f"{em.sukses}<b>Maker: {c.me.mention}</b>"
            )
        )
    if anime_photo:
        await c.send_media_group(
            message.chat.id,
            anime_photo,
            reply_to_message_id=message.id,
        )
        return await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))

    else:
        await c.send_message(
            message.chat.id,
            f"{em.gagal} <b>Error API AI!!</b>",
            reply_to_message_id=message.id,
        )
        return await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))


@ky.ubot("toimg", sudo=True)
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    try:
        pros = await message.reply(cgr("proses").format(em.proses))
        file_io = await c.dln(message.reply_to_message)
        file_io.name = "sticker.png"
        await c.send_photo(
            message.chat.id,
            file_io,
            reply_to_message_id=message.id,
        )
        await pros.delete()
    except Exception as e:
        await pros.delete()
        return await c.send_message(
            message.chat.id,
            cgr("err").format(em.gagal, e),
            reply_to_message_id=message.id,
        )


@ky.ubot("tosticker|tostick", sudo=True)
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            return await message.reply_text(
                f"{em.gagal} Silahkan balas ke media foto!!"
            )
        sticker = await c.download_media(
            message.reply_to_message.photo.file_id,
            f"sticker_{message.from_user.id}.webp",
        )
        await message.reply_sticker(sticker)
        os.remove(sticker)
    except Exception as e:
        await message.reply_text(cgr("err").format(em.gagal, e))


@ky.ubot("togif", sudo=True)
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    pros = await message.reply(cgr("proses").format(em.proses))
    if not message.reply_to_message.sticker:
        return await pros.edit(f"{em.gagal} Silahkan balas ke sticker!!")
    await pros.edit(f"{em.proses} **Converting...**.")
    file = await c.download_media(
        message.reply_to_message,
        f"gift_{message.from_user.id}.mp4",
    )
    try:
        await c.send_animation(message.chat.id, file, reply_to_message_id=message.id)
        os.remove(file)
        await pros.delete()
        return
    except Exception as error:
        await pros.edit(cgr("err").format(em.gagal, star(error)))
        return


@ky.ubot("toaudio", sudo=True)
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    replied = message.reply_to_message
    pros = await message.reply(cgr("proses").format(em.proses))
    if not replied:
        return await pros.edit(f"{em.gagal} Silahkan balas ke media video!!")
    if replied.video:
        await pros.edit(f"{em.proses} **Converting...**")
        file = await c.download_media(
            message=replied,
            file_name=f"toaudio_{replied.id}",
        )
        out_file = f"{file}.mp3"
        try:
            await pros.edit(f"{em.proses} <b>Converting audio...</b>")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await c.run_cmd(cmd)
            await pros.edit(f"{em.proses} <b>Sending audio...</b>")
            await c.send_voice(
                message.chat.id,
                voice=out_file,
                reply_to_message_id=message.id,
            )
            os.remove(file)
            await pros.delete()
        except Exception as error:
            await pros.edit(error)
    else:
        return await pros.edit(f"{em.gagal} Silahkan balas ke media video!!")


list_efek = [
    "bengek",
    "robot",
    "jedug",
    "fast",
    "echo",
    "tremolo",
    "reverse",
    "flanger",
    "pitch_up",
    "pitch_down",
    "high_pass",
    "low_pass",
    "band_pass",
    "band_reject",
    "fade_in",
    "fade_out",
    "chorus",
    "vibrato",
    "phaser",
    "reverb",
    "distortion",
    "bitcrush",
    "wahwah",
    "compressor",
    "delay",
    "stereo_widen",
    "phaser2",
    "reverse_echo",
    "low_pitch",
    "high_pitch",
    "megaphone",
    "telephone",
    "radio",
]
get_efek = {
    "bengek": '-filter_complex "rubberband=pitch=1.5"',
    "robot": "-filter_complex \"afftfilt=real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75\"",
    "jedug": '-filter_complex "acrusher=level_in=8:level_out=18:bits=8:mode=log:aa=1"',
    "fast": "-filter_complex \"afftfilt=real='hypot(re,im)*cos((random(0)*2-1)*2*3.14)':imag='hypot(re,im)*sin((random(1)*2-1)*2*3.14)':win_size=128:overlap=0.8\"",
    "echo": '-filter_complex "aecho=0.8:0.9:500|1000:0.2|0.1"',
    "tremolo": '-filter_complex "tremolo=f=5:d=0.5"',
    "reverse": '-filter_complex "areverse"',
    "flanger": '-filter_complex "flanger"',
    "pitch_up": '-filter_complex "rubberband=pitch=2.0"',
    "pitch_down": '-filter_complex "rubberband=pitch=0.5"',
    "high_pass": '-filter_complex "highpass=f=200"',
    "low_pass": '-filter_complex "lowpass=f=1000"',
    "band_pass": '-filter_complex "bandpass=f=500:width_type=h:w=100"',
    "band_reject": '-filter_complex "bandreject=f=1000:width_type=h:w=100"',
    "fade_in": '-filter_complex "afade=t=in:ss=0:d=5"',
    "fade_out": '-filter_complex "afade=t=out:st=5:d=5"',
    "chorus": '-filter_complex "chorus=0.7:0.9:55:0.4:0.25:2"',
    "vibrato": '-filter_complex "vibrato=f=10"',
    "phaser": '-filter_complex "aphaser=type=t:gain=0.2"',
    "reverb": '-filter_complex "reverb"',
    "distortion": '-filter_complex "distortion=gain=6"',
    "bitcrush": '-filter_complex "acrusher=level_in=10:level_out=16:bits=4:mode=log:aa=1"',
    "wahwah": '-filter_complex "wahwah"',
    "compressor": '-filter_complex "compand=0.3|0.8:6:-70/-70/-20/-20/-20/-20:6:0:-90:0.2"',
    "delay": '-filter_complex "adelay=1000|1000"',
    "stereo_widen": '-filter_complex "stereowiden=level_in=0.5:level_out=1.0:delay=20:width=40"',
    "phaser2": '-filter_complex "aphaser=type=t:decay=1"',
    "reverse_echo": '-filter_complex "aecho=0.8:0.88:1000:0.5"',
    "low_pitch": '-filter_complex "rubberband=pitch=0.7"',
    "high_pitch": '-filter_complex "rubberband=pitch=1.3"',
    "megaphone": '-filter_complex "amix=inputs=2:duration=first:dropout_transition=2,volume=volume=3"',
    "telephone": '-filter_complex "amix=inputs=2:duration=first:dropout_transition=2,volume=volume=1.5"',
    "radio": '-filter_complex "amix=inputs=2:duration=first:dropout_transition=2,volume=volume=2.5"',
}


@ky.ubot("list-efek|efeks|lefek", sudo=True)
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    await message.reply(
        f"""
{em.sukses} Daftar Effect Suara:\n\n• {'''
• '''.join(list_efek)}"""
    )


@ky.ubot("efek|effect|voifek", sudo=True)
async def _(c: nlx, message):
    em = Emojik()
    em.initialize()
    args = c.get_arg(message)
    reply = message.reply_to_message
    prefix = await c.get_prefix(c.me.id)
    pros = await message.reply(f"{em.proses} **Proses mengubah suara ke : `{args}`**")
    if reply and list_efek:
        if args in list_efek:
            indir = await c.download_media(reply, file_name=f"{c.me.id}.mp3")
            ses = await asyncio.create_subprocess_shell(
                f"ffmpeg -i '{indir}' {get_efek[args]} audio.mp3"
            )
            await ses.communicate()
            await message.reply_voice(
                open("audio.mp3", "rb"), caption=f"{em.sukses} Efek {args}"
            )
            for files in ("audio.mp3", indir):
                if files and os.path.exists(files):
                    os.remove(files)
            await pros.delete()
        else:
            await message.reply(
                "{} **Silahkan ketik `{}list_efek` untuk melihat daftar efek yang tersedia!!**".format(
                    em.gagal, next((p) for p in prefix)
                )
            )
            await pros.delete()
    else:
        await message.reply(
            "{} **Silahkan ketik `{}list_efek` untuk melihat daftar efek yang tersedia!!**".format(
                em.gagal, next((p) for p in prefix)
            )
        )
        await pros.delete()
