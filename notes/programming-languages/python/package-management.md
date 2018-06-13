# Pyhon Language Overview

## Package Management

Reference:

  + https://docs.python.org/3/installing/index.html#installing-index
  + https://packaging.python.org/tutorials/installing-packages

When you install Python, you also get Python's package manager, `pip`. Use `pip` to install and manage third-party Python packages.

List packages currently installed:

```shell
# For Homebrew-installed Python 3.x on Mac OS:
pip3 list

# All others:
pip list
```

Install a package (where `my_package` is the name of the package you want to install):

```shell
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install my_package

# All others:
pip install my_package
```

### Project-specific Package Management

You can specify and manage project-specific package dependencies by listing them in a file called `requirements.txt` in the project's root directory.

To specify a project's dependencies, first create a new `requirements.txt` file in your repository's root directory:

```shell
cd /path/to/your/project

# Mac Terminal:
touch requirements.txt

# Windows Command Prompt:
type nul > requirements.txt
```

Then revise the `requirements.txt` file. Write the name of each required Python package dependency on a new line, save the file, and exit. For example:

    ipython
    pytest
    requests

> NOTE: if you need to install a package from its Github source, use an entry like the following: `git+https://github.com/eskerda/pybikes.git`.

Finally, install package dependencies, as necessary:

```shell
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

If you are experiencing installation or versioning errors when using Pip, you might consider using [Pipenv](/notes/programming-languages/python/packages/pipenv.md) instead, for project-specific package management.
