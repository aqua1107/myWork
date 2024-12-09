from SmartPhone import SmartPhone

class SmartPhoneMain:

    def __init__(self):
        self.smartphone = SmartPhone()

    def print_menu(self):
        print("\n주소관리 메뉴")
        print("1. 연락처 등록(회사)")
        print("2. 연락처 등록(거래처)")
        print("3. 모든 연락처 출력")
        print("4. 연락처 검색")
        print("5. 연락처 삭제")
        print("6. 연락처 수정")
        print("7. 프로그램 종료")
        print("-------------------")

    def start(self):
        while True:
            self.print_menu()
            choice = input("원하는 작업을 선택하세요 (1~7): ")

            if choice == '1':
                addr = self.smartphone.input_data(contact_type="company")
                self.smartphone.add_data(addr)
            elif choice == '2':
                addr = self.smartphone.input_data(contact_type="customer")
                self.smartphone.add_data(addr)    
            elif choice == '3':
                self.smartphone.print_all_data()
            elif choice == '4':
                name_to_search = input("검색하고 싶은 연락처의 이름을 입력해주세요: ")
                self.smartphone.search_data(name_to_search)
            elif choice == '5':
                name_to_delete = input("삭제하고 싶은 연락처의 이름을 입력해주세요: ")
                self.smartphone.remove_data(name_to_delete)
            elif choice == '6':
                name_to_update = input("수정하고 싶은 연락처의 이름을 입력하세요: ")
                print("새로운 연락처 정보를 입력하세요.")
                new_addr = self.smartphone.input_data()
                self.smartphone.update_data(name_to_update, new_addr)
            elif choice == '7':
                print("종료 중...")
                break
            else:
                print("오류! 다시 입력하세요.")
if __name__ == '__main__':

    smartphone = SmartPhoneMain()
    smartphone.start()