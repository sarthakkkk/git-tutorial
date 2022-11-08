str ="python is good language"
count=0
for x in str:
    if(x == " "):
        count = count + 1
print(count)

#inbuilt
for x in str:
    if(str.isspace()):
        count = count + 1
print(count)
