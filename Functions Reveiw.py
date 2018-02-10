def hello(inputName):
    print("Hello "+ inputName)
    
def multiply(x,y):
    for i in range(y):
        total = 0
        print("i: " + str(i))
        total+=x
    return total

def lineMaker(z):
    print("-"*z)
    
def isThisALetter(a):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if a in letters: 
        return True
    else:
        return False

 
Name = input("Enter your name ==> ")
hello(Name)

print(multiply(3,5))
 
print(isThisALetter("A")) 