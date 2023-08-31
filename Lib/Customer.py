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

