
class restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
    
    # add a decorator to make the restaurant name read only
    # @property
    def restaurant_name(self):
        return self._restaurant_name
    
    # returns a string of the restaurant name instead object
    def __str__(self):
        return f"Restaurant Name: {self.restaurant_name}"
    
restaurant1 = restaurant("Hotel Bilha")
restaurant2 = restaurant("The mark")
restaurant3 = restaurant("Villa Rosa Kempinski")


# testing to see if the @property decorator works
# restaurant1.restaurant_name = "New restaurant"

print(restaurant1)