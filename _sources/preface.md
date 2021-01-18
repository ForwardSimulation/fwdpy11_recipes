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

# Preface

```{code-cell}
:tags: ["hide-input"]
from myst_nb import glue
import fwdpy11
fp11_version = fwdpy11.__version__
glue("fwdpy11_version", fp11_version, display=False)
```

This book provides additional recipes for the [fwdpy11](https://github.com/molpopgen/fwdpy11) simulation software.
The recipes complement examples found in the [primary documentation](https://fwdpy11.readthedocs.io).
Some recipes may be repeated here.

The contents of this book are generated using `fwdpy11` version {glue:}`fwdpy11_version`.
