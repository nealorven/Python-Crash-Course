from printing_function \
    import print_models as printing, \
    show_completed_models as completed

# Объявляем списки
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing(unprinted_designs, completed_models)
completed(completed_models)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case
#
# The following models have been printed:
# dodecahedron
# robot pendant
# iphone case
