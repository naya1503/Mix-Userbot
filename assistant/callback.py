################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


@ky.callback("clbk.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    kb = okb([[("Kembali", "clbk.bek")]])
    if cmd == "bhsa":
        teks = 