import random
import time
import check_number as check

print("I'm thinking of a number between 1 and 100. Give me a Second")
goal = int(random.random()*100)
#print(goal)
time.sleep(1)

print("Got it. Try to find out which!")

number = 0

while number != goal:
    number = input("Guess my Number between 1 and 100\n")
    if check.check_number(number) :
        number = int(number)
        if number > goal:
            print("Your Number was bigger than mine.\n")
        if number < goal:
            print("Your Number was smaller than mine.\n")
        if number == goal:
            print("You found it!")
            break
    number = int(0)

