"""Put the functions for the example printing_models.py
in a separate file called printing_functions.py.
Write an import statement at the top of printing_models.py,
and modify the file to use the imported functions."""

from module_printing_functions import print_models as pm
from module_printing_functions import show_completed_models as scm

pm.unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
scm.completed_models = []

pm(pm.unprinted_designs, scm.completed_models)
scm(scm.completed_models)
