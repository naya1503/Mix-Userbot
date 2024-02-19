from Mix import user, udB

async def load_emo():
    eping = "🏓"
    ping_id = "<emoji id=5269563867305879894>🏓</emoji>"
    epong = "🥵"
    pong_id = "<emoji id=6183961455436498818>🥵</emoji>"
    eproses = "🔄"
    proses_id = "<emoji id=6113844439292054570>🔄</emoji>"
    egagal = "❌"
    gagal_id = "<emoji id=6113872536968104754>❌</emoji>"
    esukses = "✅"
    sukses_id = "<emoji id=6113647841459047673>✅</emoji>"
    eprofil = "👤"
    profil_id = "<emoji id=5373012449597335010>👤</emoji>"
    ealive = "⭐"
    alive_id = "<emoji id=6127272826341690178>⭐</emoji>"
    ewarn = "❗️"
    warn_id = "<emoji id=6172475875368373616>❗️</emoji>"
    eblock = "🚫"
    block_id = "<emoji id=5240241223632954241>🚫</emoji>"
    a = udB.get_var(user.me.id, "emo_ping")
    b = udB.get_var(user.me.id, "emo_pong")
    c = udB.get_var(user.me.id, "emo_proses")
    d = udB.get_var(user.me.id, "emo_gagal")
    e = udB.get_var(user.me.id, "emo_sukses")
    f = udB.get_var(user.me.id, "emo_profil")
    g = udB.get_var(user.me.id, "emo_alive")
    h = udB.get_var(user.me.id, "emo_warn")
    i = udB.get_var(user.me.id, "emo_block")
    uprem = user.me.is_premium
    if uprem == True:
        if (a, b, c, d, e, f, g, h, i) is not None:
            return
        else:
            udB.set_var(user.me.id, "emo_ping", ping_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_pong", pong_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_proses", proses_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_gagal", gagal_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_sukses", sukses_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_profil", profil_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_alive", alive_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_warn", warn_id)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_block", block_id)
    elif uprem == False:
        if (a, b, c, d, e, f, g, h, i) is not None:
            return
        else:
            udB.set_var(user.me.id, "emo_ping", eping)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_pong", epong)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_proses", eproses)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_gagal", egagal)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_sukses", esukses)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_profil", eprofil)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_alive", ealive)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_warn", ewarn)
            await asyncio.sleep(0.5)
            udB.set_var(user.me.id, "emo_block", eblock)
