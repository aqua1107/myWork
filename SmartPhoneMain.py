from SmartPhone import SmartPhone

class SmartPhoneMain:

    def __init__(self):
        self.smartphone = SmartPhone()

    def print_menu(self):
        print("\n주소관리 메뉴")
        print("-------------------")
        print("1. 연락처 등록")
        print("2. 모든 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 수정")
        print("5. 연락처 삭제")
        print("6. 프로그램 종료")
        print("-------------------")

    def start(self):
        while 1:
            self.print_menu()
            choice = input("원하는 작업을 선택하세요 (1~6): ")
        
            if choice == '1':
                addr = self.smartphone.input_addr_address()
                self.smartphone.add_addr_address(addr)
            elif choice == '2':
                self.smartphone.print_all_addr()
            elif choice == '3':
                name_to_search = input("검색하고 싶은 연락처의 이름을 입력해주세요: ")
                self.smartphone.search_addr(name_to_search)
            elif choice == '4':
                name_to_update = input("수정하고 싶은 연락처의 이름을 입력하세요: ")
                print("새로운 연락처 정보를 입력하세요.")
                new_addr = self.smartphone.input_addr_address()
                self.smartphone.update_addr(name_to_update, new_addr)
            elif choice == '5':
                name_to_delete = input("삭제하고 싶은 연락처의 이름을 입력해주세요: ")
                self.smartphone.delete_addr(name_to_delete)
            elif choice == '6':
                print("종료 중...")
                break
            else:
                print("오류! 다시 입력하세요.")


if __name__ == "__main__":
    
    smart_phone_main = SmartPhoneMain()
    smart_phone_main.start()