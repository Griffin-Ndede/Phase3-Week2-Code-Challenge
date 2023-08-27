class customer:
    def __init__(self, first_name, last_name, family_name):
        self.first_name = first_name
        self.last_name = last_name
        self.family_name = family_name
        
        # returns full name of the customer 
    def __str__(self):
        return f"Customer Name: {self.first_name} {self.last_name} {self.family_name}"

#  setting customer first, last and family names
customer1 = customer("Griffin","Omondi", "Ndede")
customer2 = customer("Gerald", "Ochieng", "Ndede")
customer3 = customer()

# changing customer first, last and family name using dot notation
customer1.first_name = "Kinuthia"
customer1.last_name = "Peter"
customer1.family_name = "Otieno"
