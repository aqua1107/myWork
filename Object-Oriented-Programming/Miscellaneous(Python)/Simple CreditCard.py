class CreditCard:

    def __init__(self, customer, bank, account, limit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0 

    def get_customer(self):
        return self.customer

    def get_bank(self):
        return self.bank

    def get_account(self):
        return self.account
        
    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self.balance

    def charge(self, price):
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        if amount > self.balance:
            raise ValueError("결제 금액이 현재 잔액보다 많습니다!")
        self.balance -= amount
        return self.balance

YJS = CreditCard("Ji Sang You", "Hanabank", "123", 1000)

print(YJS.charge(1200))

try:
    print(YJS.make_payment(100))
except ValueError:
    print("잔액은 0보다 커야합니다.")

ABC = CreditCard("Alice", "Shinhan", '106', 2000)

print(ABC.charge(1500))

try:
    print(ABC.make_payment(500))
except ValueError:
    print("잔액은 0보다 더 커야합니다.")