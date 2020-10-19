DEBUG = True
ALLOWED_HOSTS = ['*']


def patch_globals(g):
    ''' Patch global settings in case you don't
    want to override the whole complex settings object.
    Examples:

    g['DATABASES']['default']['HOST'] = 'localhost'
    g['INSTALLED_APPS'] += ('debug_toolbar',)
    g['MIDDLEWARE'] += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    '''
