# Automated Testing Exercise

## Objectives

Practice writing and executing automated tests for your Python applications.

## Prerequisites

To setup these examples, create a new directory on your Desktop called "testing123" and navigate there from your command line.

If you haven't already, you will need to install [the `pytest` package](/notes/programming-languages/python/packages/pytest.md), using either Pip or Pipenv, whichever works for you:

```sh
# For Pipenv users (Mac or Windows):
pipenv install pytest --dev

# For Homebrew-installed Python 3.x on Mac OS:
pip3 install pytest

# All others:
pip install pytest
```

## Instructions

### Testing Python Scripts

To finish setting up the first example, create files in the "testing123" directory called `my_script.py` and `my_test.py`, and place inside the following contents:

```python
# my_script.py

def enlarge(i):
    return i * 100
```

```python
# my_test.py

from my_script import * # load application code from the `my_script.py` file into the test for further use

def test_enlarge(): # name this function anything, but hopefully something corresponding to the function it is testing
    result = enlarge(3)
    assert result == 300
```

Once you have setup the example, run `pytest` from the "testing123" directory. If you are using Pipenv, you should first enter into a `pipenv shell` before running `pytest`.

### Testing Python Applications

For larger applications, it's a best practice to separate application files and test files into their own respective directories (e.g. "app", and either "test" or "tests").

To set up this next example, create two new directories in your "testing123" directory, named "app" and "tests", respectively. Then move your existing files into new locations: `app/my_script.py` and `tests/test_my_script.py`. Once your repository structure looks like this, there are a few more things you need to do to configure `pytest` to run your tests.

First, modify `tests/test_my_script.py` to load the application's code from its new location:

```python
from app.my_script import * # <-- load application code from the `app/my_script.py` file into the test for further use

#def test_enlarge():
# ... the same code as before
```

Next, create a new empty file called `app/__init__.py` to indicate that code inside the "app" directory can be loaded/imported by other program files.

> NOTE: you may also need to add a `tests/__init__.py` file to suppress load errors like "ImportError while importing test module"

At this time, you should be ready to t

Be aware, in other circumstances, if your script file has code in the global scope, in order to import the file's contents without invoking it, you will also need to refactor/reorganize the code

















And in some cases you may need to refactor code inside `app/my_script.py` such that it is not automatically executed when the file is loaded, but is still automatically executed when the file is run from the command-line.

Use the convention `if __name__ == "__main__": ...` to perform a check to determine whether the file is being loaded (e.g. from a test) or whether it is being invoked from the command-line (e.g. when it is run by a user). Your application script should end up looking like this:

```python
#
# assume this file contains some functions, variables, classes, or other code
#

def run(): # use `run()` or some other similar name for this invocation function
  # so some stuff here
  # ... like invoke other functions which have been defined previously in this file
  # ... and since the code inside this function is removed from the global scope,
  # ... it will only be executed when the function is invoked

# only invoke the `run()` function if this script is executed from the command line.
# this strategy allows us to test the app's component functions
if __name__ == "__main__": # "if this script is run from the command-line"
    run() # use `run()` or whatever the name of your invocation function is
```

After your repository meets these conventions, you should be able to load application from within your test without invoking parts of it what would prompt users for input.
