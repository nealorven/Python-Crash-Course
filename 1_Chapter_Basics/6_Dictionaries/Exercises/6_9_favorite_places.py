places = {
    'cities': {
        'misha': ['budapest', 'florence', 'istanbul'],
        'yana': ['paris', 'venice', 'new york'],
        'dima': ['prague', 'rio de janeiro', 'rome']
        },
    'seas': {
        'dana': ['bali', 'mediterranean', 'red'],
        'roma': ['coral', 'andaman', 'philippine'],
        'sveta': ['caribbean', 'tasman', 'white']
        },
    'rivers': {
        'irina': ['kenai', 'niel', 'neretva'],
        'karina': ['yangtze', 'irrawaddy', 'rhine'],
        'olga': ['brahmaputra', 'cano', 'douro']
        },
    }
for key_info, vol_info in places.items():
    print(f"\nkey: {key_info}")

    for name, list_info in vol_info.items():
        print(f"Name: {name}")

        for place in list_info:
            print(f"Places: {place}")
