import random
# Snake water gun or stone paper .
def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you =='w':
            return False
        elif you=='g':
             return True
    elif comp == 'w':
        if you =='g':
            return False
        elif you=='s':
             return True
    elif comp == 's':
        if you =='g':
            return False
        elif you=='w':
             return True



print("Computer Turn: Snake(s) water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("your Turn : Snake() Water(w) or Gun(g)?")

a = game(comp,you)

print(f"Comp choose {comp}")
print(f"Your choose {you}")


if a == None:
    print("The  game is a tie!")
elif a:
    print("You win!")
else:
    print("You Loose")






