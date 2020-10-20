"""Entry-point for the :program:`dsl` command."""
import sys

def main():
    from .dsl import main as _main
    sys.exit(_main())

if __name__ == '__main__':
    main()
