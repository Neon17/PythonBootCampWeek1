import random
i = 1; Win1 = 0; Win2 = 0
Player1 = input("Enter your name: ")
Player2 = "Computer"
print("Rules of Game: ")
print("You should choose any of these in number!")
print("1. Rock")
print("2. Paper")
print("3. Scissor")
#Result 0 for No Win, 1 for Player1 Win, 2 for Player2 Win
def Check(a,b):
    if (a==1) and (b==3):
        return 1
    elif (a==3) and (b==2):
        return 1
    elif (a==2) and (a==1):
        return 1
    
    elif (a==2) and (b==3):
        return 2
    elif (a==1) and (b==2):
        return 2
    elif (a==3) and (b==1):
        return 2

    return 0
while i<6:
    print(Player1,"'s Turn")
    Choose1 = int(input("Enter your choice in number: "))
    Choose2 = random.randint(1,3)
    result = Check(Choose1,Choose2)
    if result==1:
        Win1 = Win1+1
        print(Player1, "wins")
    elif result==2:
        Win2 = Win2+1
        print(Player2, "wins")
    i = i+1
print(Player1, "VS", Player2)
print("Win: ", Win1, "   ", Win2)
if Win1>Win2:
    print(Player1," has won the game")
elif Win1<Win2:
    print(Player2, "has won the game")
else:
    print("The game is tie")
