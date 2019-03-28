# Улучшение предыдущего кода.

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
    print(f"City: {city}:")

    # Работаем со вторым вложенным кортежем
    for key, value in description.items():
        population = description['population']
        print(f"Population:{population}")
