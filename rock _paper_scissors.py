import random

user_wins = 0
cpu_wins = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("please enter a rock/paper/scissors!!")
        continue
    random_number = random.randint(0,2)
    #rock:0, paper:1, scissors: 2
    cpu_pick = options[random_number]
    print("Computer picked",cpu_pick + ".")

    if user_input == "rock" and cpu_pick == "scissors":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and cpu_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and cpu_pick == "paper":
        print("You won!")
        user_wins += 1
        
    else:
        print("You loss!")
        cpu_wins += 1

print("You won",user_wins, "times.")
print("The Computer won",cpu_wins, "times.")
print("Goodbye")

