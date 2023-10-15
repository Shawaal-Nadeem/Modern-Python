def performOperations(n1,n2,operation)->int:
    if(operation=='+'):
        return n1+n2
    elif(operation=='-'):
        return n1-n2
    elif(operation =='*'):
        return n1*n2
    else:
        return n1/n2


num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
operation=input("Enter Operation [+,-,*,/] : ")     #By default python takes value as string.
result=performOperations(num1,num2,operation)
print("Answer is : ",result)
