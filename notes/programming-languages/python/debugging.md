# Python Language Overview

## Debugging

Use the `help()` function to view documentation for a given object or datatype:

```py
help(str)
```


Use the `dir()` function to see what methods you can call on a given object.

```py
dir("Hello")
```

### Interactive Console

Use the built-in `code` module or the third-party `ipython` package for interactive debugging capabilities:

  + [`code`](modules/code.md)
  + [`ipython`](packages/ipython.md)

> NOTE: the `ipython` interactive console is superior, so try to install that package and get familiar with using its script-debugging breakpoint capabilities as soon as you feel comfortable. One major advantage to the `ipython` shell is that it enables you to press the "tab" key to auto-complete variable names.
