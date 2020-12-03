class Restaurant:

    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f'Restauracja {self.restaurant_name}, to restauracja {self.cuisine}.')


favourite_restaurant = Restaurant('Heritage', 'włoska')
kasia_restaurant = Restaurant('Pepperoni', 'włoska')
madzia_restaurant = Restaurant("Papa John's", 'włoska')

print(favourite_restaurant.describe_restaurant())
print(kasia_restaurant.describe_restaurant())
print(madzia_restaurant.describe_restaurant())