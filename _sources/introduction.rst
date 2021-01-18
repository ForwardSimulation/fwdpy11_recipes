Background information
==========================================

.. jupyter=execute::
   :hide-code:

    import sys
    sys.path.append("../") 

Modern Python
------------------------------------------------------

The examples in this book use several modern Python features:

* Functions are defined with `type hints <https://docs.python.org/3/library/typing.html>`_.
* Class definitions usually use `attrs <https://www.attrs.org>`_.

Key imports
------------------------------------------------------

The following imports will be used throughout the book:

.. jupyter-execute::

    import typing

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns

    import attr
    import fp11recipes
    import fwdpy11

The `fp11recipes` is a small Python module included with the `source code <https://github.com/ForwardSimulation/fwdpy11_recipes>`_ for this book.
