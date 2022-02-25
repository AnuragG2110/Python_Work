import random
randNumber = random.randint(1,100)
# 34print(randNumber)
userGuess = None
guesses = 0


while(userGuess != randNumber):
    userGuess = int(input("Enter your guess:"))
    guesses += 1
    if(userGuess == randNumber):
        print("You Guessed it Right!!!")
    else:
        if(userGuess>randNumber):
            print("You Guessed it Wrong!! . Enter a smaller number.")
        else:
            print("You Guessed it Wrong!! . Enter a larger number.")

       

print(f"You gusseed the number in {guesses} guesses")
with open  ('hiscore.txt', "r") as f:
    hiscore  = int(f.read)


if(guesses<hiscore):
    print("You have just BROKEN the hiscore:")
    with open ("hiscore.txt", "w") as f:
        f.write(str(guesses))