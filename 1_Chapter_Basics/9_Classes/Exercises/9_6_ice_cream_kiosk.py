class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant {}, cuisine {}."
              .format(self.name.title(), self.cuisine))

    def open_restaurant(self):
        print("Restaurant {} is open today."
              .format(self.name.title()))

    def set_number_served(self, num_serv):
        self.number_served = num_serv

    def increment_number_served(self, num_incr):
        self.number_served += num_incr

    def read_number_served(self):
        print(f"Number of served is: {self.number_served}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'nuts', 'baby', 'waffles']

    def get_ice_ream_flavors(self):
        flavors = self.flavors
        for flavor in flavors:
            print(f"Flavors: {flavor.title()}")


my_icecream = IceCreamStand('Gargo', 'italian')
my_icecream.get_ice_ream_flavors()

# Flavors: Vanilla
# Flavors: Chocolate
# Flavors: Nuts
# Flavors: Baby
# Flavors: Waffles
