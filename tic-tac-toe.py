import random
from time import sleep

def main():
    print("So here is TicTacToe game")
    sleep(1)
    while True:
        choice = input("Would you like to play against the computer or do you have friends?\n"\
                       "Just type 1 or 2\n")
        if choice == '1':
            against_ai()
       # elif int(choice) >= 2:
        #    with_friend()
        else:
            sleep(1)
            print("You are weird")
            sleep(1)


def against_ai():
    while True:
        sleep(1)
        chars = ["X", "O"]
        numbers = "123456789"
        board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |"
        choice = input("Ok, do you want to be X or O?\n").upper()
        if choice == "X" or choice == "O":
            chars.remove(choice)
        else:
            sleep(1)
            print("You are weird")
            sleep(1)
            continue
        print("Fine by me")
        while True:
            sleep(1)
            print(board)
            place = input(f"Type a number which you want to replace with {choice}\n")
            if place not in numbers:
                sleep(1)
                print("You are weird")
            else:
                numbers.replace(place, '')
                ai = numbers[random.randint(0, len(numbers) - 1)]
                numbers.replace(ai, '')
                board = board.replace(place, choice)
                board = board.replace(ai, chars[0])


against_ai()
