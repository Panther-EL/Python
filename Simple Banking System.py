class BankAccount:
    
    def __init__(self,account_number,owner,balance=0):
        #Assign to self object
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self,amount): #The balance increases
        self.balance += amount
        print('Deposit successful')
        print('Your currrent balance is',self.balance)
    
    def withdraw(self,amount): #The balance reduces
        if self.balance >= amount:
           self.balance -= amount
        else:
            print('Balance is insufficient') 
            print('Withdrawal failed')

    def check_balance(self):
        print(f'Your new balance is {self.balance}')


#Test cases
account_1 = BankAccount('001','John')
account_2 = BankAccount('002','Ama')
account_3 = BankAccount('003','Ariana')

account_1.deposit(500)
account_1.withdraw(2000)
account_1.check_balance()
        
