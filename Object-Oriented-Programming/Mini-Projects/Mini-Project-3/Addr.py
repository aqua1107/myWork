class Addr:

    def __init__(self, name, phone, email, address, birthday):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday

    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value

    def get_phone(self):
        return self.phone
    
    def set_phone(self, value):
        self.phone = value

    def get_email(self):
        return self.email
    
    def set_email(self, value):
        self.email = value

    def get_address(self):
        return self.address
    
    def set_address(self, value):
        self.address = value

    def get_birthday(self):
        return self.birthday
    
    def set_birthday(self, value):
        self.birthday = value

    def print_info(self):
        print(f"이름: {self.name}")
        print(f"전화번호: {self.phone}")
        print(f"이메일: {self.email}")
        print(f"주소: {self.address}")
        print(f"생일: {self.birthday}")


class CompanyAddr(Addr):
    def __init__(self, name, phone, email, address, birthday, company_name, buseo, clevel):
        super().__init__(name, phone, email, address, birthday)
        self.company_name = company_name
        self.buseo = buseo
        self.clevel = clevel

    def get_company_name(self):
        return self.company_name

    def set_company_name(self, value):
        self.company_name = value

    def get_buseo(self):
        return self.buseo

    def set_buseo(self, value):
        self.buseo = value

    def get_clevel(self):
        return self.clevel

    def set_clevel(self, value):
        self.clevel = value

    def print_info(self):
        super().print_info()
        print(f'회사명: {self.company_name}')
        print(f'부서명: {self.buseo}')
        print(f'직급: {self.clevel}')


class CustomerAddr(Addr):
    def __init__(self, name, phone, email, address, birthday, trans_name, item, tlevel):
        super().__init__(name, phone, email, address, birthday)
        self.trans_name = trans_name
        self.item = item
        self.tlevel = tlevel

    def get_trans_name(self):
        return self.trans_name

    def set_trans_name(self, value):
        self.trans_name = value

    def get_item(self):
        return self.item

    def set_item(self, value):
        self.item = value

    def get_tlevel(self):
        return self.tlevel

    def set_tlevel(self, value):
        self.tlevel = value

    def print_info(self):
        super().print_info()
        print(f'거래처명: {self.trans_name}')
        print(f'품목명: {self.item}')
        print(f'직급: {self.tlevel}')