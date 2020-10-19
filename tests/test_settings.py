from src.django_settings_local import import_local

def test_import_local():
    import_local(globals())
