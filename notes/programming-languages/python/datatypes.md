# Python Language Overview

## Datatypes

Common Python datatypes include:

  + [None](datatypes/none.md)
  + [Booleans](datatypes/booleans.md)
  + [Strings](datatypes/strings.md)
  + [Numbers](datatypes/numbers.md)
  + [Dates and Times](datatypes/dates.md)
  + [Lists and Sets](datatypes/lists.md) (Intermediate Concept)
  + [Dictionaries](datatypes/dictionaries.md) (Intermediate Concept)

### Detection

Use the `type()` function to detect the datatype of any object:

```python
type("Hello") #> <type 'str'>
type("100") #> <type 'str'>
type(100) #> <type 'int'>
type(0.45) #> <type 'float'>
type(True) #> <type 'bool'>
type(False) #> <type 'bool'>
type(None) #> <type 'NoneType'>
type({"a":1, "b":2, "c":3}) #> <type 'dict'>
type([1,2,3]) #> <type 'list'>
```

Alternatively call `.__class__.__name__` on any object to detect its class name:

```py
"Hello".__class__.__name__ #> 'str'
{"a":1, "b":2, "c":3}.__class__.__name__ #> 'dict'
[1,2,3].__class__.__name__ #> 'list'
```

Use the `isinstance` function when comparing datatypes:

```py
isinstance("Hello", str) #> True
isinstance([1,2,3], list) #> True
isinstance([1,2,3], str) #> False
```

### Conversion

Here are a few examples of how to convert between datatypes:

```python
# convert strings to numbers:
int("500") #> 500
float("0.45") #> 0.45

# convert numbers to strings:
str(100) #> "100"
str(0.45) #> "0.45"
```
