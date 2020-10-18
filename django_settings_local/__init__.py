# Import settings for local environment
# settings_local.py will be always unchecked
# Add settings_local.py is .gitignore file

try:
    msg = "Django settings local applied"
    from .settings_local import *
    patch_globals(globals())
    print('\n','#'*len(msg),'\n',msg,'\n','#'*len(msg))
except ImportError:
    msg = "Use `settings_local.py` in the project app to override global settings"
    print('\n','#'*len(msg),'\n',msg,'\n','#'*len(msg))
except NameError:
    msg = "For global settings mutation @ settings_local.py see format `dsl -f`"
    print('\n','#'*len(msg),'\n',msg,'\n','#'*len(msg))
