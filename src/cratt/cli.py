import argparse
import sys

from .cra import create_react_app


def parse_args():
    parser = argparse.ArgumentParser(
        description='Create React App with TypeScript and Tailwind CSS',
        prog='cra',
        allow_abbrev=False,
    )

    parser.add_argument('app_name', help='app name')

    parser.add_argument(
        'module', nargs='*', help='module to install (optional)', default=[]
    )

    parser.add_argument(
        '-D',
        '--save-dev',
        nargs='+',
        metavar='module',
        help='add module to devDependencies (optional)',
        action='store',
        dest='dev_module',
        default=[],
    )

    if len(sys.argv) == 1:
        parser.print_help()
        quit()

    return vars(parser.parse_args())


def run_cli():
    kwargs = parse_args()

    create_react_app(**kwargs)
