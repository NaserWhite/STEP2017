import random
import math
def youwin(r, p, s):
 print("You Win!")
 user_wins = user_wins + 1

def youlose():
 print("You Lose!")
 computer_wins = computer_wins + 1
 
 def youtie():
  print("It's a tie")
 

user_wins = 0
computer_wins = 0
for i in range (5):
 random_num = random.randint (1, 3)
 
choice = input("Enter Rock,Paper, or Scissors ==>")

if choice == "rock":
  choice =(1)
if choice == "paper":
  choice =(2)
if choice == "scissors":
  choice =(3)
  
 
  