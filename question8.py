str = input("enter a string")
l1=len(str)
if(l1%2==0):
    print("You have entered correct string")
elif(l1%2 != 0 and l1>1):
    print("you have entered wrong string ")
elif(l1 == 0 or l1 == 1):
    print("please enter string of length greater than one")
else:
    pass