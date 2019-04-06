def describe_city(city, country='iceland'):
    print(f"{city.title()} is {country.title()}.")


describe_city('reykjavik')
describe_city('akureyri')
describe_city('tokyo', 'japan')

# Reykjavik is Iceland.
# Akureyri is Iceland.
# Tokyo is Japan.

describe_city(country='japan', city='kyoto')

# Kyoto is Japan.
