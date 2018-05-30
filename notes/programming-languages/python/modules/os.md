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

Prerequisite: follow the [Environment Variables Overview](/notes/environment-variables/notes.md) to set an environment variable called `NYU_INFO_2335`, then reference it:

```python
os.environ["NYU_INFO_2335"] #> SecretPassword123
```
