#!python3
'''
This module contains a function to roll and keep dice
for the 4th edition of the Legends of the Five Rings (L5R) RPG
'''
import random


def roll(rolled, keep, emphasis=False, keepbest=True, unskilled=False):

    '''Rolls 'rolled' d10s, and asks user to keep 'keep' number of dice.
    returns the sum of the value of the dice kept.
    A die resulting in a 10 is exploded.
    A new d10 is rolled, and its result is added to the die that was a 10.
    10 dice rule: if rolled > 10, for each 2 extra dice, add a kept dice
    instead.
    Dice values of 10 are exploded (and extra die is rolled and added to them),
    unless the unskilled parameter is set to True.
    '''

    if rolled > 10:
        extraDice = rolled - 10
        keep += extraDice // 2
        rolled = 10
    
    print(f'We will keep {keep} dice for this roll.')

    rawResult = []

    for die in range(rolled):
        dieFace = random.randint(1, 10)
        print(f"You rolled a {dieFace}.")
        # let's reroll ones if we have emphasis
        if emphasis:
            if dieFace == 1:
                print("Let's reroll that nasty 1…")
                dieFace = random.randint(1, 10) 
                print(f"You rolled a {dieFace}.")
        # we'll explode the dieFace if we get a 10, and keep going if we get
        # another 10, unless this is an unskilled roll.
        if not unskilled:
            while dieFace % 10 == 0:
                print("You got a 10 ! Automatic explosion…")
                dieFace += random.randint(1, 10)

        rawResult.append(dieFace)
    
    rawResult.sort(reverse=True)

    print(f'The raw result is {rawResult}')

    # let's keep some dice
    if keep >= rolled:
        print('Keeping all the dice.')
        keepbest = True

    if keepbest:
        keptDice = rawResult[0:keep]

    else:
        keptDice = []
        for diceToKeep in range(keep):
            response = 0
            while int(response) not in rawResult:
                response = input(f'Please chose a dice to keep among {rawResult}.\n')
                response = int(response)
            keptDice.append(response)
            rawResult.remove(response)
            print(f'Keeping a {response}…')  
    
    print(f'You kept {keptDice}')
    print(f'Your final result is {sum(keptDice)}.')
    return sum(keptDice)

