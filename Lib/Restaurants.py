
class Restaurant:
    restaurant_lists = []

    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        Restaurant.restaurant_lists.append(self)
    
    # add a decorator to make the restaurant name read only
    # @property
    # def restaurant_name(self):
    #     return self._restaurant_name
    
    # returns a string of the restaurant name instead object
    def __str__(self):
        return f"Restaurant Name: {self.restaurant_name}"
    

for restaurant in Restaurant.restaurant_lists:
    print(restaurant)

# testing to see if the @property decorator works
# restaurant1.restaurant_name = "New restaurant"

# print(restaurant1)
