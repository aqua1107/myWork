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
    
    def __str__(self):
        return f"{self.name},{self.phone_number},{self.email},{self.address},{self.group}"

class SmartPhone:
    def __init__(self):
        self.contacts = []

    def input_addr_address(self):
        name = input("이름을 입력하세요: ")
        phone_number = input("휴대폰 번호를 입력하세요: ")
        email = input("이메일주소를 입력하세요: ")
        address = input("주소를 입력하세요: ")
        group = input("그룹을 입력하세요: ")
        return Addr(name, phone_number, email, address, group)

    def add_addr_address(self):
        if len(self.contacts) < 10:
            addr = self.input_addr_address()
            self.contacts.append(addr)
        else:
            print("연락처가 최대 수에 도달했습니다.")

    def print_all_addr(self):
        if len(self.contacts) > 0:
            for i in self.contacts:
                i.print_info()
        elif len(self.contacts) == 0:
            print("연락처가 없습니다.")

    def search_addr(self, name):
        for contact in self.contacts:
            if contact.get_name() == name:
                return contact.print_info()
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

    def save_addr(self):
        with open('contacts.txt', 'w') as file:
            for i in range(len(self.contacts)):
               file.write(f"{self.contacts[i]}\n")
        print("연락처가 저장되었습니다.")
    
    def load_addr(self):
        try:
            with open('contacts.txt', 'r') as file:
                for line in file:
                    name, phone_number, email, address, group = line.strip().split(',')
                    addr = Addr(name, phone_number, email, address, group)
                    self.contacts.append(addr)
            print("연락처를 불러왔습니다.")
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")

class SmartPhoneMain:

    def __init__(self):
        self.smartphone = SmartPhone()

    def print_menu(self):
        print("\n주소관리 메뉴")
        print("-------------------")
        print("1. 연락처 등록")
        print("2. 연락처 검색")
        print("3. 연락처 수정")
        print("4. 연락처 삭제")
        print("5. 모든 연락처 보기")
        print("6. 파일 저장")
        print("7. 파일 불러오기")
        print("8. 종료")
        print("-------------------")

    def start(self):
        while True:
            self.print_menu()
            choice = input("원하는 작업을 선택하세요 (1~8): ")
        
            if choice == '1':
                self.smartphone.add_addr_address()
            elif choice == '2':
                name_to_search = input("검색하고 싶은 연락처의 이름을 입력해주세요: ")
                self.smartphone.search_addr(name_to_search)
            elif choice == '3':
                name_to_update = input("수정하고 싶은 연락처의 이름을 압력하세요: ")
                print("새로운 연락처 정보를 입력하세요.")
                new_addr = self.smartphone.input_addr_address()
                self.smartphone.update_addr(name_to_update, new_addr)
            elif choice == '4':
                name_to_delete = input("삭제하고 싶은 연락처의 이름을 입력해주세요: ")
                self.smartphone.delete_addr(name_to_delete)
            elif choice == '5':
                self.smartphone.print_all_addr()
            elif choice == '6':
                self.smartphone.save_addr()
            elif choice == '7':
                self.smartphone.load_addr()
            elif choice == '8':
                print("종료 중...")
                break
            else:
                print("오류! 다시 입력하세요.")


if __name__ == "__main__":
    
    smart_phone_main = SmartPhoneMain()
    smart_phone_main.start()