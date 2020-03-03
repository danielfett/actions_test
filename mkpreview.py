#!/usr/bin/python3

import pathlib

p = Path('.')

print(list(p.glob('*')))
