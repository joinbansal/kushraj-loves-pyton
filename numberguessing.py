import random
playing = True
number = str(random.randint(0,9))

print("i will generate a number from 0 to 9, and you have to gues the number on digit at a ")
print("The game endws when you get 1 hero!")

while playing:
    guess = input("Give me you best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("Your geuss isn't quite right, try again. /n")