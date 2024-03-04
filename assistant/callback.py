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
    ck_bhs = udB.get_key("bahasa")
    bhs = get_bahasa_()
    if cmd == "bhsa":
        teks = cgr("asst_4")