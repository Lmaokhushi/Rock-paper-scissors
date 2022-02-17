import random

def play():
    player = input("What's your choice? \n 'r' for rock, 's' for scissors and 'p' for paper \n ")
    computer = random.choice(['r', 'p', 's'])
    
    if player == computer:
        return "It\'s a tie!"

    if winner(player, computer):
         return "You won!!"
    
    return "You lost :("

def winner(opponent1, opponent2):
    if (opponent1 == 'r' and opponent2 == 's') or (opponent1 == 's' and opponent2 == 'p') \
        or (opponent1 == 'p' and opponent2 == 'r'):
        return True

print(play())



    