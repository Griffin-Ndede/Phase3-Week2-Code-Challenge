from Review import Review

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
    
    def reviews(self):
        # Returns a list of all reviews for the restaurant
        return [review for review in Review.all_reviews_list if review.restaurant == self]
    def customers(self):

        # Returns a unique list of all customers who have reviewed the restaurant
        reviewing_customers = set()
        for review in Review.all_reviews_list:
            if review.restaurant == self:
                reviewing_customers.add(review.customer)
        return list(reviewing_customers)

    def average_star_rating(self):
        # Returns the average star rating for the restaurant based on its reviews
        total_rating = 0
        num_reviews = 0
        for review in Review.all_reviews_list:
            if review.restaurant == self:
                total_rating += review.rating
                num_reviews += 1
        if num_reviews == 0:
            return 0  
        return total_rating / num_reviews

# for restaurant in Restaurant.restaurant_lists:
#     print(restaurant)

# testing to see if the @property decorator works
# restaurant1.restaurant_name = "New restaurant"

# print(restaurant1)
