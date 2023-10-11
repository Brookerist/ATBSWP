# python3
# creates a sandwich from user input and prices it. Validates input.

import pyinputplus as pyip


# menu selections and pricing
breadDict = {'wheat':0.50, 'white':0.75, 'sourdough':1.00}
proteinDict = {'chicken':1.00, 'turkey':1.15, 'ham':0.95, 'tofu':2.35}
cheeseDict = {'cheddar':0.50, 'Swiss':0.75, 'mozzarella':0.85}

# list of toppings selected
sandwichDressings = []

# sandwich price
sandwichPrice = 00
while True:
    bread = pyip.inputMenu(['wheat','white','sourdough'], numbered=True)
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
    cheese = pyip.inputYesNo('Do you want cheese? y/n ')
    if cheese == 'yes':
        cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    mayo = pyip.inputYesNo('Do you want mayo? y/n ')
    if mayo == 'yes':
        sandwichPrice += 0.20
        sandwichDressings.append('mayo')
    mustard = pyip.inputYesNo('Do you want mustard? y/n ')
    if mustard == 'yes':
        sandwichPrice += 0.20
        sandwichDressings.append('mustard')
    lettuce = pyip.inputYesNo('Do you want lettuce? y/n ')
    if lettuce == 'yes':
        sandwichPrice += 0.20
        sandwichDressings.append('lettuce')
    tomato = pyip.inputYesNo('Do you want tomato? y/n ')
    if tomato == 'yes':
        sandwichPrice += 0.20
        sandwichDressings.append('tomato')
    noSandwich = pyip.inputInt('How many sandwiches? ')

    if len(sandwichDressings) > 1:
        sandwichDressings.insert(-1, 'and ')
        sandwichDressingStr = ', '.join(sandwichDressings[:-1]) + ' '.join(sandwichDressings[-1:])
    else:
        sandwichDressingStr = str(sandwichDressings[0])

    if cheese == 'yes':
        sandwichPrice += breadDict[bread] + proteinDict[protein] + cheeseDict[cheeseType]
    else:
        sandwichPrice += breadDict[bread] + proteinDict[protein]
    if noSandwich == 1:
        print(f'\n\nYou selected a {protein} sandwich on {bread} bread', end='')
    else:
        print(f'\n\nYou selected {protein} sandwiches on {bread} bread', end='')
    if cheese == 'yes':
        print(f' with {cheeseType} cheese')
    else:
        print('.')
    if sandwichDressingStr != '':
        if noSandwich == 1:
            print(f'You wanted {sandwichDressingStr} on it.')
        else:
            print(f'You wanted {sandwichDressingStr} on them.')
    if noSandwich > 1:
        print(f'That\'ll run you about ${sandwichPrice:.2f} per sandwich.')
        print(f'You wanted {noSandwich} of them, so your total is ${(noSandwich * sandwichPrice):.2f}')
    else:
        print(f'That\'ll run you about ${sandwichPrice:.2f}.\n\n')
    input('Press any key to run again')


