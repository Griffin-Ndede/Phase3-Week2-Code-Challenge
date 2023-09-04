
from Customer import Customer
from Restaurants import Restaurant
from Review import Review

# Creating customer instances
customer1 = Customer("Griffin", "Omondi", "Ndede")
customer2 = Customer("Gerald", "Ochieng", "Ndede")
customer3 = Customer("Enock", "Kamuta", "Harrison")
customer4 = Customer("Eunice", "Nyang'or", "Mwabe")
customer5 = Customer("Precious", "Manyara", "Nyaboke")

# Creating restaurant instances
restaurant1 = Restaurant("The Savory Spoon")
restaurant2 = Restaurant("Green Leaf Cafe")
restaurant3 = Restaurant("Villa Rosa Kempinski")
restaurant4 = Restaurant("Bella Italia Trattoria")
restaurant5 = Restaurant("Ocean's Edge Seafood Grill")

# Creating review instances
review1 = Review(customer1, restaurant1, 4.5)
review2 = Review(customer1, restaurant3, 4.5)
review3 = Review(customer5, restaurant2, 3.8)
review4 = Review(customer2, restaurant1, 4.0)
review5 = Review(customer3, restaurant3, 4.7)
review6 = Review(customer4, restaurant4, 4.2)


# # display customers
# for customer in Customer.customer_list:
#     print(f"Customer '{customer.full_name} created.'")
    
# # display restaurants
# for restaurant in Restaurant.restaurant_lists:
#     print(restaurant)

# # Display reviews
# for review in Review.all_reviews():
#     print(review)

# display the list of retaurants that a customer has reviewed
for customer in Customer.customer_list:
    print(f"Customer: {customer.full_name}")
    customer.restaurants()
    print(f"Number of reviews: {customer.num_reviews()}\n")

# # displaying the restaurants and the number of customers who reviewed it
# for restaurant in Restaurant.restaurant_lists:
#     print(f"Restaurant: {restaurant.restaurant_name}")
#     restaurant.reviews()
#     print(f"Number of customers who reviewed: {len(restaurant.customers())}\n")
name = input("Enter your symptoms")

# Querying db, and printing data according to the met condition

print("Below are the results of possible disease")