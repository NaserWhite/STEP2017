import random

#1 == rock
#2 == paper
#3 == scissors

choice = random.randint(1,3)
## Declare variabls up top

userinput = input("Rock,Paper, or Scissors =====> ")

if choice == 1 and userinput == "Rock":
    print("It's a tie!")
if choice == 2 and userinput == "Rock":
    print("You lose!")
if choice == 3 and userinput == "Rock":
    print("You win!")
    
if choice == 1 and userinput == "Paper":
    print("You win!")
if choice == 2 and userinput == "Paper":
    print ("It's a Tie!")
if choice == 3 and userinput == "Paper":
    print("You lose!")

if choice == 1 and userinput == "Scissors":
    print("You lose!")
if choice == 2 and userinput == "Scissors":
    print("You win!")
if choice == 3 and userinput == "Scissors":
    print("It's a tie")
if userinput !="Rock" and userinput != "Paper" and userinput != "Scissors":
    print(" Make sure you spelt everything right and used a uppercase letter fot the first letter of the word try again") 