print("ENTER ANY TWO ELEMENTS YOU WANT TO CALCULATE")

a=int(input("ENTER A NUMBER"))
b=int(input("Enter a number"))
ch=0
while ch>5:
    print("MENU OF THE CALCULATOR")
    print('1. ADD')
    print('2. SUBTRACT')
    print('3. MULTIPLY')
    print('4. DIVIDE')
    print('5. EXIT')

ch=int(input("Enter your choice : "))
if ch==1:
    c=a+b
    print("SUM = ",c)
elif ch==2:
    c=a-b
    print("Result = ",c )
elif ch==3:
    c=a*b
    print("the reult is : ",c)
elif ch==4:
    c=a/b
    print("the result is : ",c)
elif ch==5:
    exit



