class Bank :
    def __init__(self,initial_amt =0.00):
        self.balance =initial_amt

    def log_transcation(self, trans):
        f = open("transaction.txt","a")
        f.write(f"{trans}\t\t\tBalance {self.balance}\n")

    def withdrawal(self, amount):
        try:
            amount=float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance =self.balance - amount
            self.log_transcation(f"Withdrew {amount}")
            
    def deposite(self , amount):
        try:
            amount =float(amount)
        except ValueError:
            amount =0
        if amount:
            self.balance =self.balance + amount
            self.log_transcation(f"Deposited {amount}")

account =Bank(100)
        
while True:
    try:
        action =input("Enter your choice \n 1.Withdrawl \n 2.Deposite \n 3.Balance Enquiry \n 4.Exit\n")
    except KeyboardInterrupt :
        print("\n Leaving the ATM .")
        break
    if(int(action) == 1):
        amount =input("How much do you want to WithDraw :")
        account.withdrawal(amount)
        print("Your balance is ",account.balance)
    elif(int(action) == 2):
        amount =input("How much do you want to Deposite :")
        account.deposite(amount)
        print("Your balance is ",account.balance)
    elif(int(action)== 3):
        print("Your balance is ",account.balance)
    elif(int(action)== 4):
        break
    else:
        print("invalid Command .")