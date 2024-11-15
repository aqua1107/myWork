from Addr import Addr
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