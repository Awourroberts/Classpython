class Banker:
    location_="Malaba"
    def __init__(self,name,age,account,balance):
       self.name=name
       self.age=age
       self.account=account
       self.balance=balance
    def balance(self):
        return f"Hello people, my balance is{self.balance}"
    def current_balance(self):
        return f"Hello my bank name is {self.name} and my current balance is {200000-self.balance}"
        
