# Python Language Overview

## The `pytest` Package

Reference:

  + https://github.com/pytest-dev/pytest/
  + https://docs.pytest.org/en/latest/
  + https://docs.pytest.org/en/latest/getting-started.html#our-first-test-run
  + https://docs.pytest.org/en/latest/goodpractices.html
  + https://docs.pytest.org/en/latest/usage.html#dropping-to-pdb-python-debugger-on-failures
  + http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/#py-test

### Installation

If you are using Pip to manage software packages, install `pytest`, as necessary:

```sh
# For Pipenv users (Mac or Windows), run from a project's root directory:
pipenv install pytest --dev

# For Homebrew-installed Python 3.x on Mac OS:
pip3 install pytest

# All others:
pip install pytest
```

Otherwise, if you are using Pipenv, you will want to first navigate inside your repository's root directory before installing `pytest`:

```sh
cd path/to/my-repo/
pipenv install pytest --dev # optionally use the --dev flag to denote this package will be used in development only
```

### Usage

You can use this package from the command line or from within a script. The examples below depict usage from the command-line by invoking `pytest` from a repository's root directory.

##### Testing Python Scripts

To setup this first example, create a new directory on your Desktop called "testing-123" and navigate there from your command line, then create files called `my_script.py` and `my_test.py` and place inside the following contents, respectively:

```python
# testing-123/my_script.py

def enlarge(i):
    return i * 100
```

```python
# testing-123/my_test.py

from my_script import enlarge # load the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # name this function anything, but hopefully something related to the name of the function it is testing
    result = enlarge(3)
    assert result == 300
```

Once you have setup the example, run `pytest` from the "testing-123" directory.









##### Testing Python Applications

When testing larger applications, conventions suggest we should separate the application files and test files into their own respective directories, perhaps called "app", and either "test" or "tests".

For example, let's say you have a script called `app/my_script.py` and a corresponding test called either `tests/test_my_script.py` or `tests/my_script_test.py`.

Let's set up this example.

First, move your application file:

```python
# testing-123/app/my_script.py

def enlarge(i):
    return i * 100
```

Then, move your test file, and modify it to load the application's code:

```python
# testing-123/tests/my_script_test.py

from app.my_script import enlarge # load the enlarge() function from the `app/my_script.py` file

def test_enlarge():
    result = enlarge(3)
    assert result == 300
```

If your repository structure looks like this, there are a few more things you need to do to configure `pytest` to run your tests.

For your test to properly load application code, you need to also create a new empty file called `app/__init__.py` to indicate that code inside the "app" directory can be loaded/imported for use in other program files.

> NOTE: you may also need to add a `tests/__init__.py` file to resolve the error "ImportError while importing test module"

Once you have finished setting up this example, run `pytest` from the repository's root directory.

### Caveats

When testing a script, you may need to refactor all code inside it such that nothing is automatically executed when the file is loaded, but the desired functionality is still executed when the file is run from the command-line.

Use the convention `if __name__ == "__main__": ...` to perform a check to determine whether the file is being loaded (e.g. from a test) or whether it is being invoked from the command-line. Your application script should end up looking like this:

```python
# testing-123/my_script.py OR testing-123/app/my_script.py, depending on the example

def enlarge(i):
    return i * 100

if __name__ == "__main__": # "if this script is run from the command-line, then ..."
    enlarge()
```
