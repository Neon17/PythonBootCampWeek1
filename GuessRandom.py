#Program to guess generated random number for 1 to 10
#Importing random module
import random
RN = random.randint(1,10)
PN = input("Enter your name: ")
i = 1
while i<6:
    GN = int (input("Enter the number: "))
    if GN==RN:
        print(PN,"you have guessed correctly")
        print("Attempt: ",i)
        break
    else:
        diff = abs(GN - RN)
        if GN>RN:
            print("High")
        else:
            print("Low")

        print("Attempt",i)

        if diff>7:
            print("Hint: Too far")
        elif diff>4:
            print("Hint: Far")
        elif diff>3:
            print("Hint: Not far Not Near")
        else:
            print("Hint: Nearer")
    i=i+1
if i>5:
    print("Sorry ",PN,"Correct Number is ", RN)