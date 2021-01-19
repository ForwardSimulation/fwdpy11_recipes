---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Background information

```{code-cell} python
:tags: ["remove-cell"]
# Make sure we can import fp11recipes
import sys
sys.path.append("..")
```

Modern Python
------------------------------------------------------

The examples in this book use several modern Python features:

* Functions are defined with [type hints](https://docs.python.org/3/library/typing.html).
* Class definitions usually use [attrs](https://www.attrs.org).

Key imports
------------------------------------------------------

The following imports will be used throughout the book:

```{code-cell} python
import typing

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import attr
import fp11recipes
import fwdpy11
```

The `fp11recipes` is a small Python module included with the [source code](https://github.com/ForwardSimulation/fwdpy11_recipes) for this book.
