# Installing Python

Before you can execute Python programs on your machine, you need to install the Python command-line utility. In the recent past, there has been a movement from Python version 2 (2.x) to Python version 3 (3.x). Previous semesters have accommodated both versions of Python, but this semester we are going to be using Python 3.x exclusively.

If after following the "detection" section below, you find Python version 2.x is installed and you're not sure how to install version 3.x without conflicting, ask the professor for guidance.

## Detecting Installations

First thing's first. Let's see if Python is already installed on your machine:

```` sh
# Mac Terminal:
which python #> /usr/bin/python (or nothing if not installed)

# Windows Command Prompt:
where python #> _______ (or "Could not find files..." if not installed)
````

## Detecting Versions

If you see a filepath-looking output, it means Python is installed at the specified location. Now let's see which version is installed:

```shell
python --version #> Python 3.x.x
pip --version #> pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
```

If Python is not installed, follow the OS-specific instructions below to install it.

## Installation

## Windows OS

Download Python 3 from the [Python website](https://www.python.org/downloads/).

Note: Make sure you check the option, "Add Python 3.6 to PATH" when you are installing Python from the downloaded installer.

Once Python is installed, you should see the filepath and version outputs noted in the "detection" section above, and you should also be able to execute `python` and `pip` commands. Try `python --help` to see a list of available .












## Mac OS

You may download Python 3 from the [Python website](https://www.python.org/downloads/), but you are encouraged to use the [Homebrew](https://brew.sh/) package manager to install it.

Check to see if Homebrew is installed:

```` sh
which brew
````

Install Homebrew if necessary:

```` sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

[Use Homebrew to install Python 3.x](http://docs.brew.sh/Homebrew-and-Python.html) and follow any post-installation instructions:

To install Python 2.x (not recommended):

```` sh
brew install python
brew linkapps python
````

To install Python 3.x (recommended):

```` sh
brew install python3
````

> NOTE: If you choose to install Python 3 on a Mac using Homebrew, be aware that if you see references to running `python` you should instead run `python3`, and if you see references to `pip` you should instead run `pip3`.
