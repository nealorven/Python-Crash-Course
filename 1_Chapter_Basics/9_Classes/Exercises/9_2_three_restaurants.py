class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print("Restaurant {}, cuisine {}."
              .format(self.name.title(), self.cuisine))

    def open_restaurant(self):
        print("Restaurant {} is open today."
              .format(self.name.title()))


restaurant_gellini = Restaurant('gellini', 'italian')
restaurant_tavaki = Restaurant('tavaki', 'japanese')
restaurant_tarono = Restaurant('tarono', 'greek')

restaurant_gellini.describe_restaurant()
restaurant_tavaki.describe_restaurant()
restaurant_tarono.describe_restaurant()

# Restaurant Gellini, cuisine italian.
# Restaurant Tavaki, cuisine japanese.
# Restaurant Tarono, cuisine greek.
