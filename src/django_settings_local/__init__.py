import importlib
import os

from pathlib import Path
from .cute_python import snek

__version__ = '0.1.7'

DSL_CACHE = os.environ.get("DSL_CACHE")

def pritty_print(msg):
    print('\n','#'*len(msg),'\n',msg,'\n','#'*len(msg))

def import_local(g):
    PROJECT_APP = Path(g['__file__']).resolve(strict=True).parent.name
    try:
        msg = "Django local settings applied"
        settings_local = importlib.import_module(".settings_local", PROJECT_APP)
        for flag in dir(settings_local):
            if flag.startswith("__"):
                continue
            g[flag] = getattr(settings_local, flag)
        settings_local.patch_globals(g)
    except ImportError:
        msg = "Use `settings_local.py` in the project app to override global settings"
    except AttributeError:
        msg = "For global settings mutation, see format of settings_local.py `dsl -f`"
    finally:
        if not DSL_CACHE:
            print(snek)
            pritty_print(msg)
        os.environ.setdefault("DSL_CACHE", "PRINTED")
