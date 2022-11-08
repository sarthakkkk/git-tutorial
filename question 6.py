str=input("enter the string ")
even_str=[]
odd_str=[]
for i in range(len(str)):
    if(i%2==0):
        even_str.append(str[i])
    else:
        odd_str.append(str[i])
print(even_str)
print(odd_str)