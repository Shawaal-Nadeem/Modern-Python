uInputName: str = input("Enter Username")
uPassword: str = input("Enter Password")
dataBase: list[tuple[str, str]] = [("Shawaal", '123'), ("Nancy", '456')]
flag:bool=False
for x in dataBase:
    user, password = x
    if user == uInputName and uPassword == password:
        flag=True
        break
if flag==True:
    print('Valid User')
else:
    print('Invalid User')