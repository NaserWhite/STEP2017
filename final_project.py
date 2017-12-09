username = input("Enter Your Name => ")
print("Your name is " + username + " correct?")
anwser = input("Answer yes or no => ")
while anwser != "yes":
    Name = username = input("Enter Your Name => ")
    print("Your name is " + username + " correct?")
    anwser = input("Answer yes or no => ")

if anwser == "yes":
    print("Lets Continue")

import random
username = 0
user_wins = 0
for i in range (10):
    random_num = random.randint (1, 10)
    choice = int(input("Enter a number 1 through 10 => "))
    if choice == random_num:
        print("You gussed the right number")
        user_wins = user_wins + 1
    if choice < random_num:
        print("Too high")
    if choice > random_num:
        print("Too low")