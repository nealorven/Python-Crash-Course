def get_components(*ingredients):
    print("\nSandwich ingredients:")
    for ingredient in ingredients:
         print("- " + ingredient)


get_components('bun')
get_components('cutlet', 'spices')
get_components('bun', 'cutlet', 'egg',)

# Sandwich ingredients:
# - bun
#
# Sandwich ingredients:
# - cutlet
# - spices
#
# Sandwich ingredients:
# - bun
# - cutlet
# - egg
