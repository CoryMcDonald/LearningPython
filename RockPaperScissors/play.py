import random

#Eh, probably a better way to do this, with dict mappings and such but i'm not quite sure what data structure would be best for it

userChoice = input('Please enter Rock/Paper/Scissor/Lizard/Spock: ')

computerChoice = random.choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
print('Computer chose: ' + computerChoice)

userWon = True
description = ""
if computerChoice == userChoice:
    print('Draw!')
else:
    if computerChoice == 'Rock':
        if userChoice == 'Lizard':
            description = 'crushes'
            userWon = False
        if userChoice == 'Scissors':
            description = 'crushes'
            userWon = False
    elif computerChoice == 'Paper':
        if userChoice == 'Spock':
            description = 'disproves'
            userWon = False
        if userChoice == 'Rock':
            description = 'covers'
            userWon = False
    elif computerChoice == 'Scissors':
        if userChoice == 'Paper':
            description = 'cuts'
            userWon = False
        if userChoice == 'Lizard':
            description = 'decapitates'
            userWon = False
    elif computerChoice == 'Lizard':
        if userChoice == 'Spock':
            description = 'poisons'
            userWon = False
        if userChoice == 'Paper':
            description = 'eats'
            userWon = False
    elif computerChoice == 'Spock':
        if userChoice == 'Scissor':
            description = 'smashes'
            userWon = False
        if userChoice == 'Rock':
            description = 'vaporizes'
            userWon = False
    
    if userWon == True:
        print('You won!')
    else:
        print(computerChoice + ' ' + description + ' ' + userChoice)
        print('You lost!')