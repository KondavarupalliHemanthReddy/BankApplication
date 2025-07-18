class Bank:
    def __init__(self):
        self.pin=1234
        self.acno=1111
        self.balance=1000
    def checkDetails(self,entered_pin,entered_acno):
        if self.acno==entered_acno and self.pin==entered_pin:
            return True
        else:
            return False
    def checkBalance(self):
        print('current balance-',self.balance)
    def deposit(self,amount):     
        self.balance+=amount
        print('**succesfully deposited')
    def withdraw(self,amount):
        if amount>self.balance:
            print('**insufficient balance pls check your bank balance')
        else:
            self.balance-=amount
            print('**succesfully you withdrawn money')
abc=Bank()
# entered_pin=int(input('enter pin:'))
# entered_accno=int(input('enter account no:'))
# abc.checkBalance(entered_pin,entered_accno)
print('****Welcome to the Application*****')
entered_pin=int(input('enter pin:'))
entered_accno=int(input('enter account no:'))
if abc.checkDetails(entered_pin,entered_accno) is True:
    print(' login successful')
    a=1
else:
    print('enter correct details & login again')
    a=0
while(a):
    print()
    print('1.**display total balance\n2.**deposit money\n3.**withdraw money\n4.**exit')
    opt=int(input('enter your option:'))
    if opt==1:
        abc.checkBalance()
    elif opt==2:
        amount=int(input('enter amount you want to deposit:'))
        abc.deposit(amount)
    elif opt==3:
        amount=int(input('enter amount you want to withdraw:'))
        abc.withdraw(amount)      
    else:
        print('thank you for using application')
        a=0
        
        
    
        
            
        

            
        
        
        
        
        