string = input("Please enter your own sentence : ")
str1 = ""
for i in string:
    str1 = i + str1  
if(string == str1):
   print(str1,end="@")
print()
