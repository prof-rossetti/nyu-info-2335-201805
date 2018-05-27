# Python Language Overview

## The `pdb` Module

Reference: https://docs.python.org/3/library/pdb.html.

If using the `pdb` module, drop an interactive break-point on any line of code by inserting a `pdb.set_trace()` statement. Once you run the script, it will stop at the break-point to allow further investigation:


```py
import pdb

v = 1

pdb.set_trace()

v = 2

#> (Pdb) v
#> 1
#> (Pdb)
```

```py
import pdb

for i in [1, 2, 3, 4, 5]:
    print(i)
    if i == 4:
        pdb.set_trace()

#> 1
#> 2
#> 3
#> 4
#> > /Users/mjr/Desktop/my_script.py(3)<module>()
#> -> for i in [1, 2, 3, 4, 5]:
#> (Pdb) i
#> 4
#> (Pdb)
```
