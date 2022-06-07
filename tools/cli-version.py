from pathlib import Path
from re import search

with open(Path(Path.cwd() / 'labservices') / 'setup.py', 'r') as f:
    for line in f:
        if line.startswith('VERSION'):
            txt = str(line).rstrip()
            match = search(r'VERSION = [\'\"](.*)[\'\"]$', txt)
            if match:
                print("::set-output name=version::{}".format(match.group(1)))
