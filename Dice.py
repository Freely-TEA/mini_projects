import random

# chest of dice
def dice(selected):
    if selected == 1:
        print("-----------")
        print("|         |")
        print("|    ○    |")
        print("|         |")
        print("-----------")
        print("")

    if selected == 2:
        print("-----------")
        print("|      ○  |")
        print("|         |")
        print("|  ○      |")
        print("-----------")
        print("")

    if selected == 3:
        print("-----------")
        print("|      ○  |")
        print("|    ○    |")
        print("|  ○      |")
        print("-----------")
        print("")

    if selected == 4:
        print("-----------")
        print("| ○     ○ |")
        print("|         |")
        print("| ○     ○ |")
        print("-----------")
        print("")

    if selected == 5:
        print("-----------")
        print("| ○     ○ |")
        print("|    ○    |")
        print("| ○     ○ |")
        print("-----------")
        print("")

    if selected == 6:
        print("-----------")
        print("| ○     ○ |")
        print("| ○     ○ |")
        print("| ○     ○ |")
        print("-----------")
        print("")

# randomize chose of dice
def randomize(count):
    for i in range(count):
        num_dice = random.randint(1,6)
        dice(num_dice)
        
# input validation
def testing_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# rerolling chose of dice
def reroll(count):
    while True:
        randomize(count)
        break
    chose = input("Press inter to reroll or insert any key to go to the menu ")
    if not chose:
        reroll(count)
    else:
        entering()
        initilizations()

# i don't know, why i do it, but this make more enter
def entering():
    for i in range(4):
        print("")   

# init the dice counts
def initilizations():
    print("DICE roller")
    count = input("Chose count of dice (not more 4): ")
    while True:
        while True:
            if testing_input(count):    # test convert to int
                count = int(count)
                break
            else:
                count = input("Not the right input. Try again (use a numeric representation): ")
        
        if (count >= 1) and (count <= 4):      # test to min & max count of dice
            break           
        else:
            count = input("Please select count from 1 to 4: ")

    randomize(count)

    # chose reroll or restart
    chose = input("Press inter to reroll or insert any key to go to the menu ")
    if not chose:
        reroll(count)
    else:
        entering()
        initilizations()

initilizations()