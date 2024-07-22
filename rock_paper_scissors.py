import random

def play():
  user = input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors\n")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return "It's a tie!"
  
  if is_win(user, computer):
    return "You won!"
  
  if is_win(computer, user):
    return "You lost!"
  
  return "You lost!"

def is_win(user, opponent):
  if(user == 'r' and opponent == 's') or (user == 'p' and opponent == 'r') or (user == 's' and opponent == 'p'):
    return True
  
print(play())

