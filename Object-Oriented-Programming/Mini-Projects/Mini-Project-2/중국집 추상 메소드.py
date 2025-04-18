from abc import ABC, abstractmethod

class Chinese(ABC):
    
    def __init__(self):
        self.자장면 = "8000원"
        self.짬뽕 = "8000원"
        self.탕수육 = "12000원"
        self.군만두 = "3000원"
        self.공기밥 = "1000원"
    
    @abstractmethod
    def price(self):
        pass  # 하위 클래스에서 구현해야 하는 추상 메서드

class First(Chinese):
   
    def __init__(self):
        super().__init__()  # 상위 클래스의 __init__ 호출
        self.자장면 = "7000원"
        self.짬뽕 = "8000원"
        self.탕수육 = "12000원"
        self.군만두 = None  # 판매 안 함
        self.공기밥 = "1000원"
    
    def price(self):
        print(f"1호점 가격표입니다.\n{self.자장면} 입니다.\n{self.짬뽕} 입니다.\n{self.탕수육} 입니다.\n{'판매 안함'}\n{self.공기밥} 입니다.")

class Second(Chinese):
    
    def __init__(self):
        super().__init__()  # 상위 클래스의 __init__ 호출
        self.자장면 = "5000원"
        self.짬뽕 = "5000원"
        self.탕수육 = "10000원"
        self.군만두 = "3000원"
        self.공기밥 = "무료"
    
    def price(self):
        print(f"2호점 가격표입니다.\n{self.자장면} 입니다.\n{self.짬뽕} 입니다.\n{self.탕수육} 입니다.\n{self.군만두} 입니다.\n{self.공기밥} 입니다.")

class Third(Chinese):
    
    def __init__(self):
        super().__init__()  # 상위 클래스의 __init__ 호출
        self.자장면 = "7000원"
        self.짬뽕 = "7000원"
        self.탕수육 = "12000원"
        self.군만두 = "3000원"
        self.공기밥 = "1000원"
    
    def price(self):
        print(f"3호점 가격표입니다.\n{self.자장면} 입니다.\n{self.짬뽕} 입니다.\n{self.탕수육} 입니다.\n{self.군만두} 입니다.\n{self.공기밥} 입니다.")