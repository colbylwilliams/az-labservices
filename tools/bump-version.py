import argparse
from pathlib import Path
from re import search

from packaging.version import parse  # pylint: disable=unresolved-import

parser = argparse.ArgumentParser()
parser.add_argument('--major', action='store_true', help='bump major version')
parser.add_argument('--minor', action='store_true', help='bump minor version')
parser.add_argument('--notes', nargs='*', default=['Bug fixes and minor improvements.'], help='bump minor version')

args = parser.parse_args()

major = args.major
minor = args.minor
notes = '+ {}'.format('\n* '.join(args.notes))

if major and minor:
    raise ValueError('usage error: --major | --minor')

patch = not minor and not major

version = None

with open(Path(Path.cwd() / 'labservices') / 'setup.py', 'r') as f:
    for line in f:
        if line.startswith('VERSION'):
            txt = str(line).rstrip()
            match = search(r'VERSION = [\'\"](.*)[\'\"]$', txt)
            if match:
                version = match.group(1)

if not version:
    raise ValueError('no version found')

v = parse(version)

n_major = v.major + 1 if major else v.major
n_minor = 0 if major else v.minor + 1 if minor else v.minor
n_patch = 0 if major or minor else v.micro + 1

n = parse('{}.{}.{}'.format(n_major, n_minor, n_patch))


print('bumping version: {} -> {}'.format(v.public, n.public))

setup_fmt = 'VERSION = \'{}\''
readme_fmt = 'https://github.com/colbylwilliams/az-labservices/releases/latest/download/labservices-{}-py2.py3-none-any.whl'
history_fmt = '{}\n++++++\n{}\n\n{}'


print('..updating setup.py')

with open(Path(Path.cwd() / 'labservices') / 'setup.py', 'r') as f:
    setup = f.read()

setup = setup.replace(setup_fmt.format(v.public), setup_fmt.format(n.public))

with open(Path(Path.cwd() / 'labservices') / 'setup.py', 'w') as f:
    f.write(setup)


print('..updating HISTORY.rst')

with open(Path(Path.cwd() / 'labservices') / 'HISTORY.rst', 'r') as f:
    history = f.read()

history = history.replace(v.public, history_fmt.format(n.public, notes, v.public))

with open(Path(Path.cwd() / 'labservices') / 'HISTORY.rst', 'w') as f:
    f.write(history)


print('..updating README.md')

with open(Path(Path.cwd()) / 'README.md', 'r') as f:
    readme = f.read()

readme = readme.replace(readme_fmt.format(v.public), readme_fmt.format(n.public))

with open(Path(Path.cwd()) / 'README.md', 'w') as f:
    f.write(readme)
