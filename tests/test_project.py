import os
from src.django_settings_local.dsl import main


def test_main_console_script():
    os.chdir("tests/project_app")
    main();main()
    os.chdir("../../")
