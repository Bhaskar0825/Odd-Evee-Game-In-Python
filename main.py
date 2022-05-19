import random
User_input = input("Take Odd Or Evee: ")
Match_making = int(input("Enter Number: "))
Comp = random.randint(1,10)
Match_final = (Comp+Match_making)
Your_Score = 0
Computer_Score = 0
Player_while = True
i = 1
i2 = 1
Player_chance_done = 0
Computer_chance_done = 0
if User_input=='odd': #checks wheather user take odd/evee
    if Match_final%2!=0: # check if user win
        print("You Got Chance Choose Bat/Ball",Comp)
        Bat_Ball = input()
    elif Match_final%2==0: #check if bot win as user take odd
        Player_while=False
        if Comp%2==0: # now comp choose bat or ball on basis of number he choose
            print("Computer got the Chance And he choose Bat")
        else:
            print("Computer got the Chance And he choose Ball")
else: # here checks for evee
    if Match_final%2!=0:
        Player_while=False
        if Comp%2==0:
            print("Computer got the Chance And he choose Bat")
        else:
            print("Computer got the Chance And he choose Ball")
    elif Match_final%2==0:
        print("You Got Chance Choose Bat/Ball")
        Bat_Ball = input()
if Player_while==True:
    if Bat_Ball=='bat':
        Player_chance_done+=1
        while i>0:
            Number = int(input("Enter Number: "))
            Comp_Choose = random.randint(1,10)
            if Number == Comp_Choose:
                break
            print(f"You Choose {Number} and Computer Choose {Comp_Choose}")
            Your_Score+=Number
        print(f"Your Score is {Your_Score}")
    elif Bat_Ball=='ball':
        Computer_chance_done+=1
        while i>0:
            Number = int(input("Enter Number: "))
            Comp_Choose = random.randint(1,10)
            if Number == Comp_Choose:
                break
            print(f"You Choose {Number} and Computer Choose {Comp_Choose}")
            Computer_Score+=Comp_Choose
        print(f"Computer Score is {Computer_Score}")
elif Player_while==False:
    if Comp%2==0:
        Computer_chance_done+=1
        while i>0:
            Number = int(input("Enter Number: "))
            Comp_Choose = random.randint(1,10)
            if Number == Comp_Choose:
                break
            print(f"You Choose {Number} and Computer Choose {Comp_Choose}")
            Computer_Score+=Comp_Choose
        print(f"Computer Score is {Computer_Score}")
    else:
        Player_chance_done+=1
        while i>0:
            Number = int(input("Enter Number: "))
            Comp_Choose = random.randint(1,10)
            if Number == Comp_Choose:
                break
            print(f"You Choose {Number} and Computer Choose {Comp_Choose}")
            Your_Score+=Number
        print(f"Your Score is {Your_Score}")
if Player_chance_done>0:
    while i2>0:
        Number = int(input("Enter Number: "))
        Comp_Choose = random.randint(1,10)
        if Number == Comp_Choose:
            break
        print(f"You Choose {Number} and Computer Choose {Comp_Choose}")
        Computer_Score+=Comp_Choose
    print(f"Computer Score is {Computer_Score}")
else:
    while i2>0:
        Number = int(input("Enter Number: "))
        Comp_Choose = random.randint(1,10)
        if Number == Comp_Choose:
            break
        print(f"You Choose {Number} and Computer Choose {Comp_Choose}")
        Your_Score+=Number
    print(f"Your Score is {Your_Score}")
if Your_Score>Computer_Score:
    print(f"You Won Your Score is {Your_Score} and Computer Score is {Computer_Score}")
elif Your_Score<Computer_Score:
    print(f"Computer Won Your Score is {Your_Score} and Computer Score is {Computer_Score}")
else:
    print(f"That Was A hard match we got draw, Your Score {Your_Score} and Computer Score {Computer_Score}")
