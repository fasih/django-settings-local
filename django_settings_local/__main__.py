from pathlib import Path
import argparse, os, shutil

cute_python = r"""
                    /^\/^\
                  _|__|  O|
         \/     /~     \_/ \
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~ 
                        ~--______-~                ~-___-~
"""
FILE_NAME = 'settings_local.py'

parser = argparse.ArgumentParser(description='Create Django Local Settings')
parser.add_argument('-p', metavar='PATH', help='Django Project Application Path')
parser.add_argument('-f', action='store_true', help='Show Django Local Settings Format')

def main():
    print(cute_python)
    args = parser.parse_args()
    WORKING_DIR = Path(args.p or os.getcwd())
    PACKAGE_DIR = Path(__file__).resolve(strict=True).parent
    GIT_IGNORE = WORKING_DIR.parent/'.gitignore'

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
        fp.write('\n# Added by Django Setting Local `dsl`\nsettings_local*\n')
        fp.close()

if __name__ == '__main__':
    main()
