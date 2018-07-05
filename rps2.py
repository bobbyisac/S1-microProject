import time
from random import randint
 
def comp_play():
    val = randint(1,3)
    if val == 1:
        hand = 'rock'
    elif val == 2:
        hand = 'paper'
    elif val == 3:
        hand = 'scissors'
    return hand
   
def play_hand(comp, you):
    if comp == you:
        winner = "tie"
    elif comp == ('rock' and you == 'scissors') or (comp == 'scissors' and you == 'paper')\
        or (comp == 'paper' and you == 'rock'):
        winner = 'computer'
    else:
        winner = 'you'
    return winner
 
def play_game():
    playing = True
    comp_wins = 0
    you_wins = 0
    tie_wins = 0
    print("Let's play Rock, Paper, Scissors!")
    while playing:
        print("----------------------------")
        print()
        try:
            you = input("Type 'rock', 'paper', 'scissors' or 'quit' to end game ")
        except:
            print('Invalid entry, please try again')
            print()
            continue
        you = you.lower()
        if you == 'quit':
            if you_wins > comp_wins:
                print("You beat the computer! you: %d / computer: %d, ties: %d" % (you_wins, comp_wins, tie_wins))
            elif comp_wins > you_wins:
                print("The computer beat you! computer: %d / you: %d, ties: %d" % (comp_wins, you_wins, tie_wins))
            break
        elif you == 'paper' or you == 'scissors' or you == 'rock':
            comp = comp_play()
            winner = play_hand(comp, you)
            print("The computer played %s, and you played %s" % (comp, you))
        else:
            print('Invalid entry, please try again')
            print()
            continue
        if winner == 'tie':
            print("It's a tie!!")
            tie_wins += 1
        elif winner == 'computer':
            print("The computer wins!!")
            comp_wins += 1
        elif winner == 'you':
            print("You won!!!")
            you_wins += 1
        print()
    print()
play_game()
