from Mix import Emojii, user


def fexid():
    emo = Emojii(user.me.id)
    emo.initialize()


fex = fexid()
