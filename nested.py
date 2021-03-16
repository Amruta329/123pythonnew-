no=int(input("enter no"))
if no.isdigit():
    print("you have entered positive no")

    if(no==0):
        print("you have entered o")            #nested if else syntax

    else:
        print("you have entered negative value")

else:
    print("you have entered something else")