a=int(input("enter a number"))
b=int(input("enter a second number"))
if(a>0):
    print("ok")

elif a==0:
    print("you have entered o")
else:
    print("print another number")

def addition():
    c=int(a)+int(b)
    print(c>20)          #here we it will print if it is true or false
    if(c>20):            #here we have checked the condition
        print(c)

    else:
        print("the addition is less than 20")


    print(c)

addition()