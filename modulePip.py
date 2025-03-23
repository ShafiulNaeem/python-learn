'''
pip install <package_name>  # install package
pip uninstall <package_name>  # uninstall package
pip list  # list all installed packages
pip show <package_name>  # show package details
pip freeze  # list all installed packages with version
pip freeze > requirements.txt  # save all installed packages with version to a file
pip install -r requirements.txt  # install all packages from a file
pip install --upgrade <package_name>  # upgrade package
pip install --upgrade pip  # upgrade pip
module is packege and pip is packege manager
what is module and pip?
module is a file containing python code. It may contain functions, classes, etc.
pip is a package manager used to install and manage software packages written in Python.
'''

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
