# Python Language Overview

## The `os` Module

Reference: https://docs.python.org/3/library/os.html.

Use the `os` module perform command-line-style file and directory operations, and to access system environment variables.

### Directory Operations

Get current working directory:

```python
os.getcwd() # for scripts, reflects the dir where the command is being run
```

Get directory of current file:

```py
os.path.dirname(__file__)) # for scripts, reflects the dir where the script file exists
```

Change directory:

```py
os.chdir("/path/to/Desktop")
```

Make a new directory:

```py
os.mkdir("/path/to/Desktop/my-dir")
```

List all files in a given directory:

```python
os.listdir("/path/to/Desktop")
```


### File Operations

Detect whether a specific file exists:

```py
os.path.isfile("/path/to/Desktop/some_file.txt") #> returns True or False
```

Compile file paths by joining a directory with a relative file path:

```py
os.path.join(os.path.dirname(__file__), "../../some_upstream_file.txt")
```










### Accessing Environment Variables

To setup the following examples, follow the [Environment Variables Overview](/notes/software/environment-variables.md) and/or [the `dotenv` package](/notes/programming-languages/python/packages/dotenv.md) notes to set an environment variable named `NYU_INFO_2335`.

Get the entire environment:

```py
import os

my_env = os.environ

print("------------")
print(type(my_env)) #> <class 'os._Environ'>
print(my_env)

print("------------")
print(type(dict(my_env))) #> <class 'dict'>
print(dict(my_env)) #> 'dict'
```

Get a specific environment variable (e.g. `NYU_INFO_2335`, only after you have set it):

```py
# using a dictionary-like approach:
my_var = os.environ["NYU_INFO_2335"]
print(my_var) #> SecretPassword123

# using a getter function approach:
my_var = os.environ.get("NYU_INFO_2335")
print(my_var) #> SecretPassword123
```
