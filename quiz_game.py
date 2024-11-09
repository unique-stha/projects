print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("OK! Lets play :)")

answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does RAM stand for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does PSU stand for?")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got "+str(score)+" question correct!")
print("you got "+str((score/4)*100)+"%")