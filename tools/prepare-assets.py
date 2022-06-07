import argparse
import json
import os
from pathlib import Path
from re import search

# parser = argparse.ArgumentParser()
# parser.add_argument('version', help='version number string')

# args = parser.parse_args()

# version = args.version.lower()

# if version[:1].isdigit():
#     version = 'v' + version

ci = os.environ.get('CI', False)

assets = []

assets_dir = '{}/{}'.format(Path.cwd(), 'release_assets' if ci else 'local/release_assets')


# Get CLI version
with open(Path(Path.cwd() / 'labservices') / 'setup.py', 'r') as f:
    for line in f:
        if line.startswith('VERSION'):
            txt = str(line).rstrip()
            match = search(r'VERSION = [\'\"](.*)[\'\"]$', txt)
            if match:
                cli_version = match.group(1)
                cli_name = 'labservices-{}-py2.py3-none-any.whl'.format(cli_version)

version = f'v{cli_version}'

download_url = f'https://github.com/colbylwilliams/az-labservices/releases/download/{version}' if ci else assets_dir

index = {}

index['extensions'] = {
    'labservices': [
        {
            'downloadUrl': f'{download_url}/{cli_name}',
            'filename': f'{cli_name}',
            'metadata': {
                'azext.isPreview': True,
                'azext.isExperimental': True,
                'azext.minCliCoreVersion': '2.10.0',
                'azext.maxCliCoreVersion': '3.0.0',
                'classifiers': [
                    'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.6',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    'Programming Language :: Python :: 3.9',
                    'License :: OSI Approved :: MIT License',
                ],
                'extensions': {
                    'python.details': {
                        'contacts': [
                            {
                                'email': 'colbyw@microsoft.com',
                                'name': 'Microsoft Corporation',
                                'role': 'author'
                            }
                        ],
                        'document_names': {
                            'description': 'DESCRIPTION.rst'
                        },
                        'project_urls': {
                            'Home': 'https://github.com/colbylwilliams/az-labservices'
                        }
                    }
                },
                'generator': 'bdist_wheel (0.30.0)',
                'license': 'MIT',
                'metadata_version': '2.0',
                'name': 'labservices',
                'summary': 'Microsoft Azure Command-Line Tools Lab Services Extension',
                'version': f'{cli_version}'
            }
        }
    ]
}

with open(f'{assets_dir}/index.json', 'w') as f:
    json.dump(index, f, ensure_ascii=False, indent=4, sort_keys=True)

with os.scandir(assets_dir) as s:
    for f in s:
        if f.is_file():
            print(f.path)
            name = f.name.rsplit('.', 1)[0]
            assets.append({'name': f.name, 'path': f.path})

if not ci:
    with open(f'{assets_dir}/assets.json', 'w') as f:
        json.dump(assets, f, ensure_ascii=False, indent=4, sort_keys=True)

print("::set-output name=assets::{}".format(json.dumps(assets)))
