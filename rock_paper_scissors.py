#!/usr/bin/env python3

def r_p_s():

    import random
    options = {"1": "rock", "2": "paper", "3": "scissors"}
    win = [["paper", "rock"], ["rock", "scissors"], ["scissors", "paper"]]
    number = str(random.randint(1, 3))

    user = input()
    computer = options[number]
    choice = [user, computer]

    def game(c):
        win = [["paper", "rock"], ["rock", "scissors"], ["scissors", "paper"]]
        if c[0] == c[1]:
            return "Draw"
        elif c in win:
            return "You won!"
        else:
            return "You lose!"

    print(computer)
    print(game(choice))

    restart = input("Do you want to play again?(y/n)")
    if restart == "y" or restart == "Y":
        r_p_s()

if __name__ == "__main__":
    r_p_s()
