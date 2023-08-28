class customer:
    customer_list = []

    def __init__(self, first_name, last_name, family_name):
        self.first_name = first_name
        self.last_name = last_name
        self.family_name = family_name
        customer.customer_list.append(self)
        
        # returns full name of the customer 
    def __str__(self):
        return f"Customer Name: {self.first_name} {self.last_name} {self.family_name}"

#  setting customer first, last and family names
customer1 = customer("Griffin","Omondi", "Ndede")
customer2 = customer("Gerald", "Ochieng", "Ndede")
customer3 = customer("Enock", "Kamuta", "Harrison")
customer4 = customer("Eunice", "Nyang'or", "Mwabe")
customer5 = customer("Precious", "Manyara", "Nyaboke")


# changing customer first, last and family name using dot notation
customer1.first_name = "Kinuthia"
# customer2.last_name = "Peter"
# customer3.family_name = "Otieno"

# store the customer names in a list
# customer_list = [customer1, customer2, customer7]

# printing the names of all the customers
for customer in customer.customer_list:
    print(customer)

# printing individual customer names
print(customer1)
print(customer5)