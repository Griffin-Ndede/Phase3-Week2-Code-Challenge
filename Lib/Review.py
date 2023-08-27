from Customer import customer
from Restaurants import restaurant

from Customer import customer1
from Restaurants import restaurant1
from Restaurants import restaurant3

class review:
    all_reviews = []
    def __init__ (self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        review.all_reviews.append(self)

    def __str__(self):
        return f"Customer review: {self.customer}, {self.restaurant}, Rating: {self.rating}"

review1 = review(customer, restaurant1, 4.5)
review1 = review(customer1, restaurant3, 5)


# iterating through the all_review list to get all the reviews 
for review in review.all_reviews:
    print(review)

# printing a single review
# print(review1)