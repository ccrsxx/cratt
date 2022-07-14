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
        'module',
        nargs='*',
        action='store',
        help='module to install (optional)',
        default=[],
    )

    parser.add_argument(
        '-p',
        '--push-github',
        action='store_true',
        help='push to github (optional)',
    )

    parser.add_argument(
        '-D',
        '--save-dev',
        nargs='+',
        action='store',
        metavar='module',
        help='add module to devDependencies (optional)',
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


run_cli()
