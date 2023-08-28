from Customer import customer
from Restaurants import restaurant

# importing instances of the customers
from Customer import customer1
from Customer import customer2
from Customer import customer3
from Customer import customer4
from Customer import customer5

# importing instances of restaurants
from Restaurants import restaurant1
from Restaurants import restaurant2
from Restaurants import restaurant3
from Restaurants import restaurant4
from Restaurants import restaurant5


class review:
    all_reviews = []
    def __init__ (self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        review.all_reviews.append(self)

    def __str__(self):
        return f"Customer review: {self.customer}, {self.restaurant}, Rating: {self.rating}"

# Creating instances of reviews
review1 = review(customer1, restaurant1, 4.5)
review2 = review(customer2, restaurant2, 3.8)
review3 = review(customer3, restaurant3, 5.0)
review4 = review(customer4, restaurant4, 4.2)
review5 = review(customer5, restaurant5, 3.5)
review6 = review(customer1, restaurant3, 4.0)
review7 = review(customer2, restaurant4, 4.8)
review8 = review(customer3, restaurant5, 3.7)
review9 = review(customer4, restaurant1, 4.7)
review10 = review(customer5, restaurant2, 3.2)


# iterating through the all_review list to get all the reviews 
for review in review.all_reviews:
    print(review)

# printing a single review
# print(review1)