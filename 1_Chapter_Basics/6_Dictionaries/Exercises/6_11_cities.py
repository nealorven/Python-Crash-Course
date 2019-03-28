cities = {
    'rio de janeiro': {
        'country': 'brazil',
        'population': 6.32,
        'fact': 'guanabara bay',
        },
    'florence': {
        'country': 'italy',
        'population': 382.347,
        'fact': 'cattedrale di santa maria del fiore',
        },
    'venice': {
        'country': 'italy',
        'population': 261.358,
        'fact': 'shuttle trams',
        },
    }
for city, description in cities.items():
    country = description['country']
    population = description['population']
    fact = description['fact']
    print(f"City: {city.title()}.")
    print(f"Country: {country.title()}.")
    print(f"Population: {population} people.")
    print(f"Interesting places: {fact.capitalize()}.\n")

# City: Rio De Janeiro.
# Country: Brazil.
# Population: 6.32 people.
# Interesting places: Guanabara bay.

# City: Florence.
# Country: Italy.
# Population: 382.347 people.
# Interesting places: Cattedrale di santa maria del fiore.

# City: Venice.
# Country: Italy.
# Population: 261.358 people.
# Interesting places: Shuttle trams.
