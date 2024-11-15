from CompanyAddr import CompanyAddr
from CustomerAddr import CustomerAddr

class SmartPhone:

    def __init__(self):
        self.contacts = []

    def input_data(self, contact_type="company"):
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        birthday = input("생일을 입력하세요: ")
    
        if contact_type == "company":
            company_name = input("회사명을 입력하세요: ")
            buseo = input("부서명을 입력하세요: ")
            clevel = input("직급을 입력하세요: ")
            return CompanyAddr(name, phone, email, address, birthday, company_name, buseo, clevel)
        else:
            trans_name = input("거래처명을 입력하세요: ")
            item = input("품목명을 입력하세요: ")
            tlevel = input("직급을 입력하세요: ")
            return CustomerAddr(name, phone, email, address, birthday, trans_name, item, tlevel)
    
    def add_data(self, addr):
        self.contacts.append(addr)

    def print_all_data(self):
        for i in self.contacts:
            i.print_info()

    def remove_data(self, name):
        for i in self.contacts:
            if i.get_name() == name:  
                self.contacts.remove(i)
                break  
        else:
            print("잘못 입력하셨습니다.")

 
    def update_data(self, name, new_addr):
        for i in self.contacts:
            if i.get_name() == name:
                self.contacts[self.contacts.index(i)] = new_addr
                break
        else:
            print(f"{name}에 해당하는 연락처가 없습니다.")

    def search_data(self, name):
        for i in self.contacts:
            if i.get_name() == name:
                i.print_info()
