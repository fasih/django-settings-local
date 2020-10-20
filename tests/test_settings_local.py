import importlib, os
from src.django_settings_local import dsl, import_local, settings_local

def test_import_local():
    import_local(globals())

def test_valid_patch_globals():
    settings_local.patch_globals(globals())

def test_invalid_patch_globals():
    try:
        settings_local.patch_globals(1,2)
    except TypeError:
        pass

def test_main_module():
    main_module = importlib.import_module("src.django_settings_local.__main__")
    try:
        os.chdir("tests/django_project_app")
        main_module.main()
    except SystemExit:
        os.chdir("../../")

def test_main_script():
    os.chdir("tests/django_project_app")
    dsl.main(); dsl.main()
    os.chdir("../../")
