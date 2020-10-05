import random

# input validation
def testing_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# generating rage of numbers
def make_range():
    # start range of numbers
    user_range_start = input("Enter the beginning of the range of numbers for the game: ")
    while True:
        if testing_input((user_range_start)):
            break
        else:
            user_range_start = input("Not the right input. Try again (use a numeric representation): ")

    # end randge of numbers
    user_range_end = input("Enter the end of the range of numbers for the game: ")
    while True:
        if testing_input(user_range_end):
            if user_range_end <= user_range_start:
                user_range_end = input("Error entering a segment. The initial number is greater than the final number, or they are equal. Repeat the entry: ")
            else:
                break
        else:
            user_range_start = input("Not the right input. Try again (use a numeric representation): ") 
    number = generate(user_range_start, user_range_end)
    game(number)


# generator of random number
def generate(min,max):
    min = int(min)
    max = int(max)
    return random.randint(min,max)

# i don't know, why i do it, but this make mor enter
def entering():
    for i in range(4):
        print("")

# game body
def game(num):
    trying = 1
    answer = input("The game is ready. Try to guess the number: ")
    while True:
        while True:
            if testing_input(answer):
                answer = int(answer)
                break
            else:
                answer = input("Not the right input. Try again (use a numeric representation): ")
        if (answer == num):
            print("Yahoooo. You guessed the number in ",trying ,"attempts")
            entering()
            break
        elif (answer < num):
            print("Not true. The hidden number is greater")
        elif (answer > num):
            print("Not true. The hidden number is less")
        answer = input("Retry to guess the number: ")
        trying = trying + 1
    # ending game process
    a = input("Press ENTER to back in menu. Or insert 'Q' to quit ")
    if not a:
        entering()
        menu()
    else:
        quit()

# game menu       
def menu():
    print('Welcome to the game "guess the number".')
    print('Please select the difficulty level:')
    print('1. From 1 to 10')
    print('2. From 1 to 100')
    print('3. From 1 to 1000')
    print('4. User array')
    print()
    print('Or print "Q" to exit the game')
    
    chose = input()
    
    # quit
    if (chose == "q") or (chose == "Q"):
        quit()
    
    # to integer testing
    while True:
        if testing_input(chose):
            chose = int(chose)
            break
        else:
            chose = input("Not the right input. Try again (use a numeric representation): ")

    # selection processing
    while True:
        if chose == 1:
            game(generate(1, 10))
            break
        elif chose == 2:
            game(generate(1, 100))
            break
        elif chose == 3:
            game(generate(1, 1000))
            break
        elif chose == 4:
            make_range()
            break
        else:
            chose = input("Not the right input. Try again (use a numeric representation): ")

menu()