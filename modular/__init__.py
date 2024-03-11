from team.nandev.class_log import LOGGER


def import_modular():
    import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules


USER_MOD = sorted(import_modular())
# LOGGER.info("Userbot module loaded: %s", str(USER_MOD))
__all__ = USER_MOD + ["USER_MOD"]
