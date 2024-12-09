class Addr:
     
    def __init__(self, name, phone_number, email, address, group):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.group = group

    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value
    
    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number(self, value):
        self.phone_number = value

    def get_email(self):
        return self.email
    
    def set_email(self, value):
        self.email = value

    def get_address(self):
        return self.address
    
    def get_group(self):
        return self.group

    def print_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Phone Number: {self.get_phone_number()}")
        print(f"Email: {self.get_email()}")
        print(f"Address: {self.get_address()}")
        print(f"Group: {self.get_group()}")