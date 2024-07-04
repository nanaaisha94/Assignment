'''QUESTION 1'''

class BankAccount:
    def __init__(self,AcctName,AcctNumber,Balance):
        self.AcctName=AcctName
        self.AcctNumber=AcctNumber
        self.Balance=Balance

    def deposit(self,amount):
        if amount>0:
            self.Balance+=amount
            print(f' your acct has been credited with ₦{amount} and your balance is ₦{self.Balance}')
        
    def withdraw(self,amount):
        self.Balance-=amount
        if self.Balance<amount:
            print('insufficient fund')
        else:
            print(f'your acct has been debited of ₦{amount} and your balance is ₦{self.Balance}')

    def CheckBalance(self):
        print(f' your account balance is ₦{self.Balance}')
       
Account=BankAccount('Imran',2233445566,200000)

print(Account.Balance)
Account.withdraw(50000)
Account.CheckBalance()

Account.deposit(20000)
Account.CheckBalance()

'''QUESTION 2'''
class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def describe(self):
        print(f"my name is {self.name}, I'm {self.age} years old and I'm {self.height} inches tall")

class Student(Person):
    def __init__(self,name,age,height,kg):
        super().__init__(name,age,height)
        self.kg=kg
    def describe(self):
        print(f"my name is {self.name}, I'm {self.age} years old,{self.height} inches tall, I'm in nur {self.kg}")

class Teacher(Person):
    def __init__(self,name,age,height,TeachersName):
        super().__init__(name,age,height)
        self.TeachersName=TeachersName
    def describe(self):
        print(f"my name is {self.name}, I'm {self.age} years old and I'm {self.height} inches tall, I call my teacher aunty {self.TeachersName}")
        
person=Person('Sumayyah',4,28)
student=Student('Sumayyah',4,28,2,)
teacher=Teacher('Sumayyah',4,28,'Muslimah')

person.describe()
student.describe()
teacher.describe()










        







