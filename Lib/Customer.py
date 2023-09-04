from Review import Review
class Customer:
    customer_list = []

    def __init__(self, first_name, last_name, family_name):
        self.first_name = first_name
        self.last_name = last_name
        self.family_name = family_name
        Customer.customer_list.append(self)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.family_name}"
        
    # returns a list of unique list of all restaurants the customer has reviewed

    def restaurants(self):
        reviewed_restaurants = set()
        for review in Review.all_reviews_list:
            if review.customer == self:
                reviewed_restaurants.add(review.restaurant)
        unique_restaurants = list(reviewed_restaurants)
        print(f"{self.full_name} has reviewed the following restaurants: {', '.join([restaurant.restaurant_name for restaurant in unique_restaurants])}")
        return unique_restaurants

    # Creates a new review and associates it with the customer and restaurant

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)

     # Returns the total number of reviews that the customer has authored
    def num_reviews(self):
        return len([review for review in Review.all_reviews_list if review.customer == self])
    
    @classmethod
    def find_by_name(cls, name):
        # Given a full name, returns the first customer whose full name matches
        for customer in cls.customer_list:
            if customer.full_name == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls, name):
        # Given a given name, returns a list containing all customers with that given name
        matching_customers = []
        for customer in cls.customer_list:
            if customer.first_name == name:
                matching_customers.append(customer)
        return matching_customers
    

   