import argparse, os, shutil

from pathlib import Path
from .cute_python import snek


FILE_NAME = 'settings_local.py'


def main():
    print(snek)

    parser = argparse.ArgumentParser(description='Create Django Local Settings')
    parser.add_argument('-p', metavar='PATH', help='Django Project Application Path')
    parser.add_argument('-f', action='store_true', help='Show Django Local Settings Format')
    args = parser.parse_args()

    WORKING_DIR = Path(args.p or os.getcwd())
    PACKAGE_DIR = Path(__file__).resolve(strict=True).parent

    GIT_IGNORE = WORKING_DIR.parent/'.gitignore'
    DJANGO_SETTINGS = WORKING_DIR/'settings.py'

    if args.f:
        with open(PACKAGE_DIR/FILE_NAME, 'r') as fb:
            print(fb.read())
    elif os.path.isfile(WORKING_DIR/FILE_NAME):
        print(f"{FILE_NAME} is already there at {WORKING_DIR}")
    else:
        shutil.copyfile(PACKAGE_DIR/FILE_NAME, WORKING_DIR/FILE_NAME)

        if os.path.isfile(GIT_IGNORE):
            fp = open(GIT_IGNORE, 'a')
        else:
            fp = open(GIT_IGNORE, 'w')
        fp.write('\n# Added by `dsl` (Django Setting Local)\nsettings_local*\n')
        fp.close()

        fp = open(DJANGO_SETTINGS, 'a')
        fp.write("\n\n\n\n")
        fp.write("\n##################### END OF SETTINGS ################################")
        fp.write("\nfrom django_settings_local import import_local;import_local(globals())")
        fp.write("\n##################### END OF SETTINGS ################################")
        fp.close()

