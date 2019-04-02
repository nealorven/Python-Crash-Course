def city_country(city, country):
    title = f"\n{city}, {country}"
    return title.title()

capital = city_country('vienna', 'austria')
capital += city_country('buenos aires', 'argentina')
capital += city_country('nassau', 'bahamas')

print(capital)

# Vienna, Austria
# Buenos Aires, Argentina
# Nassau, Bahamas
