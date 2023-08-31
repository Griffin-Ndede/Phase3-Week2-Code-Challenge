
class Review:
    all_reviews_list = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews_list.append(self)

    def get_restaurant(self):
        return self.restaurant

    def get_customer(self):
        return self.customer

    def get_rating(self):
        return self.rating

    @classmethod
    def all_reviews(cls):
        return cls.all_reviews_list

    def __str__(self):
        return f"Customer review: {self.customer.full_name}, reviewed {self.restaurant.restaurant_name}, Rating: {self.rating}"
    
# iterating through the all_review list to get all the reviews 
for review in Review.all_reviews_list:
    print(review)