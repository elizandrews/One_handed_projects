# Imports functions from printing_models.py to test functions

import printing_functions as pf

unprinted_designs = ['dodecahedron', 'robot pendant', 'phone case']
completed_models = []

pf.printing_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)