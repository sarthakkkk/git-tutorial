str=input("enter the string ")
str1= ""
for x in str:
    str1=x+str1
print(str1)

#using   inbuilt function
def my_function(x):
  return x[::-1]

mytxt = my_function("python is good language")

print(mytxt)