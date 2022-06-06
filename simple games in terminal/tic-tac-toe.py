import random
from time import sleep

def main():
    print("So here is TicTacToe game")
    sleep(1)
    while True:
        choice = input("Would you like to play against the computer or do you have friends?\n"\
                       "Just type 1 or 2\n")
        if choice == 'exit':
            break
        elif choice == '1':
            against_ai()
        elif int(choice) >= 2:
            with_friend()
        else:
            sleep(1)
            print("You are weird")
            sleep(1)
        sleep(1)
        print("Welcome back to main menu, hehe\n"\
              "Type 'exit' whenever you get tired of this")
        sleep(2)


def against_ai():
    while True:
        sleep(1)
        chars = ["X", "O"]
        numbers = "123456789"
        board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |"
        choice = input("Ok, do you want to be X or O?\n").upper()
        if choice in chars:
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
                numbers = numbers.replace(place, '')
                if len(numbers) == 0:
                    print("It's a tie")
                    break
                ai = numbers[random.randint(0, len(numbers) - 1)]
                numbers = numbers.replace(ai, '')
                board = board.replace(place, choice)
                if winning(board, choice) == True:
                    print(f"{choice} wins! Game over!\n"\
                          "Congrats if that was you")
                    break
                board = board.replace(ai, chars[0])
                if winning(board, chars[0]) == True:
                    print(f"{chars[0]} wins! Game over!\n"\
                          "Congrats if that was you")
                    break
        sleep(1.5)
        newgame = input("Wanna go again?(yes/no)\n").strip().lower()
        if newgame == 'no':
            sleep(1)
            print("Ok, bye")
            break


def with_friend():
    while True:
        sleep(1)
        chars = ["X", "O"]
        numbers = "123456789"
        board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |"
        choice = input("Ok, do you want to be X or O?\n").upper()
        if choice in chars:
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
                numbers = numbers.replace(place, '')
                if len(numbers) == 0:
                    print("It's a tie")
                    break
                board = board.replace(place, choice)
                if winning(board, choice) == True:
                    print(f"{choice} wins! Game over!")
                    break
                print(board)
            place_2 = input(f"Ok, now {chars[0]} does the same\n")
            if place_2 not in numbers:
                sleep(1)
                print("You are weird")
            else:
                numbers = numbers.replace(place_2, '')
                board = board.replace(place_2, chars[0])
                if winning(board, chars[0]) == True:
                    print(f"{chars[0]} wins! Game over!")
                    break
        sleep(1.5)
        newgame = input("Wanna go again?(yes/no)\n").strip().lower()
        if newgame == 'no':
            sleep(1)
            print("Ok, bye")
            break


def winning(board, char):
    if board[0:12].count(char) == 3 or board[12:26].count(char) == 3 or board[26:].count(char) == 3:
        return True
    elif board[2::14].count(char) == 3 or board[6::14].count(char) == 3 or board[10::14].count(char) == 3:
        return True
    elif board[2::18].count(char) == 3 or board[10::10].count(char) == 3:
        return True

if __name__ == "__main__":
    main()
