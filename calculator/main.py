print("             Calculator              ")

# Simple Method

# def performOperations(n1,n2,operation)->int:
#     if(operation=='+'):
#         return n1+n2
#     elif(operation=='-'):
#         return n1-n2
#     elif(operation =='*'):
#         return n1*n2
#     else:
#         return n1/n2


# num1=int(input("Enter First Number : "))
# num2=int(input("Enter Second Number : "))
# operation=input("Enter Operation [+,-,*,/] : ")     #By default python takes value as string.
# result=performOperations(num1,num2,operation)
# print("Answer is : ",result)


# OOP Method


class Calculator:
    n1 = 0
    n2 = 0
    op = ""

    def getNum1(self) -> int:
        return self.n1

    def getNum2(self) -> int:
        return self.n2

    def getOperator(self):
        return self.op

    def performOperations(self):
        if self.getOperator() == "+":
            result = self.getNum1() + self.getNum2()
            print("Answer is : ", result)
        elif self.getOperator() == "-":
            result = self.getNum1() - self.getNum2()
            print("Answer is : ", result)
        elif self.getOperator() == "*":
            result = self.getNum1() * self.getNum2()
            print("Answer is : ", result)
        else:
            result = self.getNum1() / self.getNum2()
            print("Answer is : ", result)


obj = Calculator()
obj.n1 = int(input("Enter First Number : "))
obj.n2 = int(input("Enter Second Number : "))
obj.op = input("Enter Operation [+,-,*,/] : ")
obj.performOperations()
