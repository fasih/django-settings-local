import os

def test_main_console_script():
    cmd0 = ['cd', 'src', '&&', 'python3', '-m', 'django_settings_local', '-p', '../tests/project_app/']
    os.system(" ".join(cmd0))
    os.system(" ".join(cmd0))

    cmd1 = cmd0[:-2] + ["-f"]
    os.system(" ".join(cmd1))
