from Addr import Addr
class SmartPhone:

    def __init__(self):
        self.contacts = []

    def input_addr_address(self):
        name = input("Name: ")
        phone_number = input("Phone number: ")
        email = input("Email: ")
        address = input("Address: ")
        group = input("Group: ")
        return Addr(name, phone_number, email, address, group)

    def add_addr_address(self, addr):
        if len(self.contacts) < 10:
            self.contacts.append(addr)
        else:
            print("저장공간이 다 찼습니다.")

    def print_all_addr(self):
        for contact in self.contacts:
            contact.print_info()
        
    def search_addr(self, name):
        for contact in self.contacts:
            if contact.get_name() == name:
                contact.print_info()
                return 
        print(f"'{name}'이란 결과를 찾을 수 없습니다.")

    def delete_addr(self, name):
        for contact in self.contacts:
            if contact.get_name() == name:
                self.contacts.remove(contact)
                print(f"{contact.name}의 연락처가 삭제되었습니다.")
                return
        print(f"에러: {name}을 찾을 수 없습니다.")

    def update_addr(self, name, new_addr):
        for i, addr in enumerate(self.contacts):
            if addr.get_name() == name:
                self.contacts[i] = new_addr
                print(f"{name}의 연락처가 수정되었습니다.")
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")