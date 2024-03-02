def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]
    return all_modules
    
    
BOT_PLUGINS = sorted(__list_all_modules())
__all__ = BOT_PLUGINS + ["BOT_PLUGINS"]