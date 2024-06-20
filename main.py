import random

pencils = 0


def remove_pencils():
    global pencils
    int_to_remove = check_value()
    if 1 <= int_to_remove <= 3 and pencils > 0 and (pencils - int_to_remove) > 0:
        pencils -= int_to_remove
    elif (pencils - int_to_remove) == 0:
        pencils -= int_to_remove
    elif int_to_remove > pencils:
        print("Too many pencils were taken")
        int_to_remove = int(input())
        pencils -= int_to_remove
    return pencils


def check_value():
    while True:
        int_to_remove = input()
        try:
            int_to_remove = int(int_to_remove)
            if int_to_remove <= 0 or int_to_remove >= 4:
                print("Possible values: '1', '2' or '3'")
            else:
                return int_to_remove
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def start_game():
    global pencils
    while True:
        try:
            init_pencils = int(input('How many pencils would you like to use: \n'))
            if init_pencils == 0:
                print("The number of pencils should be positive")
            elif init_pencils < 0:
                print("The number of pencils should be numeric")
            else:
                pencils = init_pencils
                break
        except ValueError:
            print("The number of pencils should be numeric")


def win_or_lose():
    global pencils
    n = pencils
    if n % 4 == 1:
        if pencils == 1:
            pencils -= 1
            return 1
        else:
            maxr = min(3, pencils)
            j = random.randrange(1, maxr)
            pencils -= j
            return j
    else:
        remainder = n % 4
        sub = (3 + remainder) % 4
        pencils -= sub
        return sub


start_game()
name = input("Who will be the first (John, Jack):\n")

while True:
    if name == "John" and pencils != 0:
        if pencils != 0:
            print('|' * pencils)
        print("John's turn!")
        remove_pencils()
#        if pencils != 0:
#            print('|' * pencils)
        name = "Jack"
    elif name == "Jack" and pencils != 0:
        if pencils != 0:
            print('|' * pencils)
        print("Jack's turn:")
        k = win_or_lose()
        print(k)
#        if k != 0:
#            print('|' * pencils)
        name = "John"
    elif pencils == 0 and name == "John":
        print("John won!")
        break
    elif pencils == 0 and name == "Jack":
        print("Jack won!")
        break
    elif name != "John" or name != "Jack":
        print("Choose between 'John' and 'Jack'")
        name = input()
    else:
        remove_pencils()
