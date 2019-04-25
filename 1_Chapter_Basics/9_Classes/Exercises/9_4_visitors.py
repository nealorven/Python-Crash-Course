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


restaurant = Restaurant('gellini', 'italian')

restaurant.read_number_served()
# Number of served is: 0
restaurant.number_served = 30
restaurant.read_number_served()
# Number of served is: 30

restaurant.set_number_served(35)
restaurant.read_number_served()
# Number of served is: 35

restaurant.increment_number_served(10)
restaurant.read_number_served()
# Number of served is: 45
