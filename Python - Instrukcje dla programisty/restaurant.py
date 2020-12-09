class Restaurant:

    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restauracja {self.restaurant_name}, to restauracja {self.cuisine}.'
              f'\nObsłużyła {self.number_served} gości.')

    def set_number_served(self, guests):
        self.number_served = guests

    def increment_number_served(self, add_guests):
        self.number_served += add_guests


favourite_restaurant = Restaurant('Heritage', 'włoska')
# kasia_restaurant = Restaurant('Pepperoni', 'włoska')
# madzia_restaurant = Restaurant("Papa John's", 'włoska')

favourite_restaurant.increment_number_served(50)

print(favourite_restaurant.describe_restaurant())
# print(kasia_restaurant.describe_restaurant())
# print(madzia_restaurant.describe_restaurant())
