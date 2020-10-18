DEBUG = True
ALLOWED_HOSTS = ['*']

def patch_globals(g):
    '''
    g['DATABASES']['default']['HOST'] = 'localhost'
    g['DATABASES']['default']['PORT'] = '5432'
    g['DATABASES']['default']['NAME'] = 'postgres'
    g['DATABASES']['default']['USER'] = 'postgres'
    g['DATABASES']['default']['PASSWORD'] = 'root'
    g['INSTALLED_APPS'] += ('debug_toolbar',)
    g['MIDDLEWARE'] += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    '''
