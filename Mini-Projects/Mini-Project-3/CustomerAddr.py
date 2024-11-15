from Addr import Addr
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

    def get_buseo(self):
        return self.item
    
    def set_buseo(self, value):
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