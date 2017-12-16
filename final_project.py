
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
loss = False
random_num = random.randint(1, 10)
while (loss == False):
    for i in range(3):
        choice = int(input("Enter a number 1 through 10 => "))
        if choice == random_num:
            print("You gussed the right number")
            user_wins = user_wins + 1
            break
        if choice < random_num:
            print("Too low")
        if choice > random_num:
            print("Too high")
    if choice is not random_num:
        print("You Lose")
        print("Points:" + str(user_wins))
        print("The random number was " + str(random_num))
        loss = True
    random_num = random.randint(1, 10)
        

