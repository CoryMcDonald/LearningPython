import random

userChoice = ""
while userChoice == "" and (userChoice != 'heads' or userChoice != "tails"):
    userChoice = input('Enter heads or tails:')

headsOrTails = random.choice(['heads','tails'])
print('Flipping Coin - ' + headsOrTails)
if userChoice == headsOrTails:
    print('You win! :D')
else:
    print('You lost :(')