import os
from sys import argv

package_name = argv[1]

FILES_WITH_PACKAGE_NAME = [
    'pyproject.toml',
]

FILES_TO_DELETE = [
    'setup.cfg',
    'MANIFEST.in',
    'pyproject-uncommented.toml',
    r"src\$src-template\data_files\example.txt",
    r"src\$src-template\another_data_file.html",
    r"src\$src-template\example2.json",

]

with open('README.md', 'w') as f:
    f.write(f'# {package_name}\n')

def rename_top_level_module_folder():
    os.rename('src/$src-template', package_name)

def clean_pyproject():
    with open('pyproject-uncommented.toml', 'r') as f:
        content = f.read()
    with open('pyproject.toml', 'w') as f:
        f.write(content)
        
def replace_place_holder_name_in_file(file_name, new_string):
    with open(file_name, 'r') as f:
        content = f.read()
    content = content.replace('$src-template', new_string)
    with open(file_name, 'w') as f:
        f.write(content)

clean_pyproject()
rename_top_level_module_folder()

for file_name in FILES_WITH_PACKAGE_NAME:
    replace_place_holder_name_in_file(file_name, package_name)

for file_name in FILES_TO_DELETE:
    os.remove(file_name)

# delete this file
os.remove('clean.py')