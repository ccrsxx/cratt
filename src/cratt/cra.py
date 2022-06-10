import os
import re
import sys
import json
import argparse

from template import (
    APP,
    SASS,
    INDEX,
    CHANGED_FILE,
    ES_LINT_CONFIG,
    ES_LINT_IGNORE,
    ADDED_DIRECTORY,
    PRETTIER_CONFIG,
    PRETTIER_IGNORE,
)


def setup_project(app_name: str):
    name = ' '.join(app_name.split('-')).title()
    homepage = f'https://ccrsxx.github.io/{app_name}'

    with open('public\\index.html', 'r+') as f:
        html = f.read()
        html = html.replace('React App', name)
        commented_html = [
            *map(
                lambda x: x[1],
                re.findall('(png|json|div).+?(\n.+?<!--.+?-->)', html, re.DOTALL),
            )
        ]

        for comment in commented_html:
            html = html.replace(comment, '')

        f.seek(0)
        f.truncate()

        f.write(html)

    with open('public\\manifest.json', 'r+') as f:
        manifest = json.load(f)
        manifest['name'] = name
        manifest['short_name'] = name

        f.seek(0)

        json.dump(manifest, f, indent=2)

    with open('tailwind.config.js', 'r+') as f:
        tailwind = f.read()
        tailwind = tailwind.replace(
            'content: []', "content: ['./src/**/*.{ts,tsx}', './public/index.html']"
        )

        f.seek(0)
        f.truncate()

        f.write(tailwind)

    os.chdir('src')

    for folder in ADDED_DIRECTORY:
        os.makedirs(folder)
        with open(f'{folder}\\index.ts', 'w') as f:
            f.write('export default undefined;')

    for file in os.listdir():
        if file not in CHANGED_FILE:
            try:
                os.remove(file)
            except OSError:
                pass
        elif file in CHANGED_FILE[:-1]:
            if file == 'index.css':
                os.rename(file, 'index.scss')
                file = 'index.scss'

            with open(file, 'w') as f:
                f.write(
                    APP if file == 'App.tsx' else INDEX if file == 'index.tsx' else SASS
                )
        else:
            pass

    os.chdir('..')

    with open('.eslintrc.json', 'w') as f:
        json.dump(json.loads(ES_LINT_CONFIG), f, indent=2)

    with open('.eslintignore', 'w') as f:
        f.write(ES_LINT_IGNORE)

    with open('package.json', 'r+') as f:
        content = json.load(f)

        content['lint-staged'] = {'**/*': 'prettier --write --ignore-unknown'}
        content['homepage'] = homepage
        content['scripts']['predeploy'] = 'npm run build'
        content['scripts']['deploy'] = 'gh-pages -d build'

        f.seek(0)

        json.dump(content, f, indent=2)

    with open('.prettierrc.json', 'w') as f, open('.prettierignore', 'w') as j:
        json.dump(json.loads(PRETTIER_CONFIG), f, indent=2)
        j.write(PRETTIER_IGNORE.lstrip())

    os.system('npm i -D husky lint-staged && npx husky install')

    os.system(
        'npm set-script prepare "husky install" && npx husky add .husky/pre-commit "npx lint-staged"'
    )

    os.system(
        f'git ac "add things up" && gh repo create --public -h {homepage} -s . --push'
    )

    os.system(
        f'gh repo edit ccrsxx/{app_name} --add-topic=react,typescript,tailwindcss,html'
    )

    os.system('code . && npm start')


def get_airbnb_eslint_config():
    raw_packages = os.popen(
        'npm info "eslint-config-airbnb@latest" peerDependencies --json'
    ).read()

    packages: dict = json.loads(raw_packages)

    results = [
        '@typescript-eslint/eslint-plugin@latest',
        'eslint-config-airbnb-typescript@latest',
        '@typescript-eslint/parser@latest',
        'eslint-config-prettier@latest',
        'eslint-config-airbnb@latest',
        'prettier-plugin-tailwindcss',
        'autoprefixer',
        'tailwindcss',
        'prettier',
        'gh-pages',
        'postcss',
    ]

    for package, version in packages.items():
        version = version.replace('^', '@')
        if '||' in version:
            version = max([*map(lambda x: x.strip(), version.split('||'))])
        results.append(package + version)

    return ' '.join(results)


def create_react_app(app_name: str, module: list[str] = [], dev_module: list[str] = []):
    os.system(f'npx create-react-app {app_name} --template typescript')

    os.chdir(app_name)

    airbnb_config = get_airbnb_eslint_config()

    module, dev_module = [' '.join(mod) for mod in (module, dev_module)]  # type: ignore

    os.system(f'npm i sass {module if module else ""}')

    os.system(f'npm i -D {airbnb_config} {dev_module if dev_module else ""}')

    os.system('npx tailwindcss init -p')

    setup_project(app_name)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Create React App with TypeScript and tailwindcss',
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
