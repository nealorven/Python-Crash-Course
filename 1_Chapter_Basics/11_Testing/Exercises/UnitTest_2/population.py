
def get_format_city(city, country, population=''):
    if population:
        out_format = f"{city}, {country}: {population}"
    else:
        out_format = f"{city}, {country}"
    return out_format.title()
