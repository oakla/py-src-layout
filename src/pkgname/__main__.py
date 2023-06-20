"""
This module is the default starting point of your package after installation.
"""

import sys
# importlib_resources is a backport of importlib.resources which provides
# the newest features of importlib.resources to older Python versions.

# You could just use importlib_resources regardless of the Python version.
# Go ahead and change it, but remember to update the dependencies list.
if sys.version_info >= (3, 10):
    from importlib.resources import files
else: 
    from importlib_resources import files

example_text = files('pkgname.data_files').joinpath('example.txt').read_text()
print(example_text)

import json
example_map = json.loads(files('pkgname').joinpath('example2.json').read_text())
print(f"Hello {example_map['Hello']} from json file")

example_path = files('pkgname').joinpath('another_data_file.html')
print(example_path)