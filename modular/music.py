# part of github.com/Yeagerist-Music-Streamer-Bot-V3/VCMusicPlayerVr4.0

import re
from youtube_dl import YoutubeDL
from config import *
from Mix import *

finalurl = ""
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links = []
playlist = []
msg = {}
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,stream)
if match:
    meta = ydl.extract_info(stream, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=stream
    
