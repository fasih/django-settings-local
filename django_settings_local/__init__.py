import importlib

from pathlib import Path
from .cute_python import snek

FILE_NAME = 'settings_local.py'


def pritty_print(msg):
    print('\n','#'*len(msg),'\n',msg,'\n','#'*len(msg))

def import_local(g):
    PROJECT_DIR = Path(g['__file__']).resolve(strict=True).parent
    try:
        msg = "Django settings local applied"
        spec = importlib.util.spec_from_file_location("settings_local",
                PROJECT_DIR/FILE_NAME)
        settings_local = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(settings_local)
        for flag in dir(settings_local):
            if flag.startswith("__"):
                continue
            g.update(flag=getattr(settings_local, flag))
        settings_local.patch_globals(g)
        #from .settings_local import *
        #patch_globals(globals())
    except (ImportError, FileNotFoundError):
        msg = "Use `settings_local.py` in the project app to override global settings"
    except (NameError, AttributeError):
        msg = "For global settings mutation @ settings_local.py see format `dsl -f`"
    finally:
        print(snek)
        pritty_print(msg)
