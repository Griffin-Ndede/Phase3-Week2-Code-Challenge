from Customer import customer
from Restaurants import restaurant

# from Customer import customer1
# from Restaurants import restaurant1

# from Customer import customer2

class review:
    def __init__ (self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def __str__(self):
        return f"Customer review: {self.customer}, {self.restaurant}, Rating: {self.rating}"

review1 = review(customer, restaurant, 4.5)

print(review1)