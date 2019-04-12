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
