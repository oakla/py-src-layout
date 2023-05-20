# $package_name
A template for the src-layout of a Python project.

## src-layout
The containg folder of this readme is a template for the 'src-layout', a popular layout for python projects and can be detected by *setuptools* for automatic package discovery. 

Read about package discovery in the setuptools docs [here](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#), including the advantages and disadvantages of [src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout).

### Quick Description 
From the setuptools docs:
> The project should contain a src directory under the project root and all modules and packages meant for distribution are placed inside this directory:
```
project_root_directory
├── pyproject.toml  # AND/OR setup.cfg, setup.py
├── ...
└── src/
    └── mypkg/
        ├── __init__.py
        ├── ...
        ├── module.py
        ├── subpkg1/
        │   ├── __init__.py
        │   ├── ...
        │   └── module1.py
        └── subpkg2/
            ├── __init__.py
            ├── ...
            └── module2.py
```

> This layout is very handy when you wish to use automatic discovery, since you don’t have to worry about other Python files or folders in your project root being distributed by mistake. In some circumstances it can be also less error-prone for testing or when using [**PEP 420**](https://peps.python.org/pep-0420/)-style packages. On the other hand you cannot rely on the implicit `PYTHONPATH=`. to fire up the Python REPL and play with your package (you will need an [editable install](https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs) to be able to do that)