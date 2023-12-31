import random



numberOfStreaks = 0
coinFlip = []
streak = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for flips in range(100):
        coinFlip.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.

    for i in range(len(coinFlip)):
        if i == 0:
            pass
        elif coinFlip[i] == coinFlip[i-1]:  # checks if current list item is the same flip as before
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1

    coinFlip = []


print('Chance of streak: %s%%' % (numberOfStreaks / (100 *10000)))
