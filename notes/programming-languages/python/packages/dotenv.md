# Python Language Overview

## The `dotenv` Package

> Prerequisite: [Environment Variables](/notes/software/environment-variables.md)

The `dotenv` package allows a program to reference environment variables from a project-specific `.env` file. This makes environment variables much easier to manage, especially for Windows users.

Reference: https://github.com/theskumar/python-dotenv.

### Installation

First install the package, if necessary:

```` sh
# For Pipenv users (Mac or Windows), run from a project's root directory:
pipenv install python-dotenv # note: not just `dotenv`

# For Homebrew-installed Python 3.x on Mac OS:
pip3 install python-dotenv # note: not just `dotenv`

# All others:
pip install python-dotenv # note: not just `dotenv`
````

### Usage


To setup this example, create a new directory on your Desktop named "my-project". Then navigate there from the command-line:

```sh
cd Desktop/my-project/
```

Create two files in the "my-project" directory named `.env` and `my_script.py`, respectively, and place inside the following contents:

```sh
# my-project/.env

NYU_INFO_2335="SecretPassword123"
```

```py
# my-project/my_script.py

from dotenv import load_dotenv
import os

load_dotenv()

my_var = os.environ.get("NYU_INFO_2335")

print(my_var) #> SecretPassword123
```
