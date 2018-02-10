firstname = input("Please Enter your first name: ")
lastname = input("Please Enter your last name: ")
hello = "Hello,"

if len(firstname) > len(lastname):
    length = len(firstname)
if len(lastname) > len(firstname):
    length = len(lastname)
if len(hello) > len(firstname) or  len(hello) > len(lastname):
    lenth = len(hello)
print(length)
hellospace = length - len(hello)
firstnamespace = length -len(firstname)
lastnamespace = length - len(lastname)


print("@"*(length + 5))
print("@"*2 +" "+ hello  + " "*hellospace + "@"*2)
print("@"*2 +" "+ firstname +" "*firstnamespace  +"@"*2)
print("@"*2 +" "+ lastname +" "*lastnamespace +"@"*2)
print("@"*(length + 5))

