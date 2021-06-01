
from datetime import datetime  
class Bank_account :
    
    def __init__(self,name, phone_number,loan):
        self.name=name
        self.balance=0
        self.phone_number=phone_number
        self.loan=loan
        self.statement=[]

    def show_balance(self):
        return f"Hello this is my {self.balance}"   

    def deposit(self,amount):
        if amount<=0:
            return f"you cannot deposit {amount}"
        else:
            self.balance+=amount 
            now=datetime.now()   
            transaction={
                "amount":amount,
                "time":now,
                "narration":"you deposited"
            }
            self.statement.append(transaction)
       
    def withdraw(self,amount):
        if amount>self.balance:    
            return f" your balance is {self.balance} you cannot withdraw {amount}"
        else:
                self.balance-=amount
                now=datetime.now() 
                withdrawal={
                    "amount":amount,
                    "time":now,
                    "narration":"you withdrew"
            }
                self.statement.append(withdrawal)   
        return self.show_balance()    

    def borrow_loan(self,amount):
        return f"congratulation you have borrowed {amount}"
    def repay_loan(self,amount):
        return f"You have  repaid {amount}"
    
    def show_statement(self):
        for transacation in self.statement:
                amount= transacation["amount"]
                narration=transacation["narration"]
                time=transacation["time"]
                date=time.strftime["%d/%m/%y"]
                print( f"{date}:{narration} {amount}")
        return
        




            
