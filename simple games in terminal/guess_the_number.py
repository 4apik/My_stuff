import random
import time

def main():
    time.sleep(0.5)
    print("Welcome to guess the number game")
    while True:
        time.sleep(1)
        choice = input("If you want to guess numbers type 'me'\n"\
                       "If you want the computer to guess your numbers type 'it'\n"\
                       "If you want to leave type 'bye'\n").strip().lower()
        if choice == 'me':
            guess()
        elif choice == 'it':
            computer_guess()
        elif choice == 'bye':
            time.sleep(1)
            print("Ok, bye")
            break
        else:
            print("That's not what I asked for...")


def guess():
    time.sleep(1)
    print("So be it. You will be guessing a number between 1 and the number of your choice.")
    time.sleep(2)
    while True:
        try:
            upper_limit = int(input("What should the upper limit be this time?\n"))
        except ValueError:
            time.sleep(1)
            print("It should've been a number... Digits, you know those, right?")
            time.sleep(1)
            continue
        the_number = random.randint(1, upper_limit)
        time.sleep(1)
        guess = 0
        while guess != the_number:
            try:
                guess = int(input("Ok, what's your guess?\n"))
            except ValueError:
                print("It should've been a number... Digits, you know those, right?")
                continue
            time.sleep(1)
            if guess < the_number:
                print("Nope. Too low")
            elif guess > the_number:
                print("Nope. Too high")
        end = input("Yep. That's it. Wanna play again?(yes/no)\n").strip().lower()
        if end == 'yes':
            continue
        elif end == 'no':
            time.sleep(1)
            print("Ok, bye")
            break
        else:
            time.sleep(2)
            print("I'll take it as 'yes'")


def computer_guess():
    time.sleep(1)
    print("So be it. Computer will be guessing a number between 1 and the number of your choice.")
    time.sleep(2)
    while True:
        lower_limit = 1
        guess = ''
        try:
            upper_limit = int(input("What should the upper limit be this time?\n"))
        except ValueError:
            time.sleep(1)
            print("It should've been a number... Digits, you know those, right?")
            time.sleep(1)
            continue
        time.sleep(0.5)
        print("Fine by me")
        time.sleep(1)
        if checking := input("Now imagine a number computer will need to guess\n"\
                             "Type anything whenever you are ready\n"):
            time.sleep(1)
            print("Ok, after my every guess type 'L' if it was too low, 'H' if it was too high or 'C' for 'correct'")
            time.sleep(1)
            while guess != 'c' and lower_limit != upper_limit:
                the_number = random.randint(lower_limit, upper_limit)
                guess = input(f"Is it {the_number}?\n").strip().lower()
                time.sleep(1)
                if guess == 'l':
                    lower_limit = the_number + 1
                elif guess == 'h':
                    upper_limit = the_number - 1
                elif guess != 'c':
                    print("Ok, I'll just try again")
                    time.sleep(1)
            end = input("Easy. Go again?(yes/no)\n")
            if end == 'yes':
                continue
            elif end == 'no':
                time.sleep(1)
                print("Ok, bye")
                break
            else:
                time.sleep(2)
                print("I'll take it as 'yes'")

        
main()
        
